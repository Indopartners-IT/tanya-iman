# AGENTS.md

Guidance for AI coding agents and new contributors working in this repository.

## Project overview

**Tanya Iman** is an Indonesian-language theology Q&A assistant for Muslim seekers. Users ask about Allah, Isa Al-Masih, the Holy Scripture, or a faith-related question, and receive a 25–250 word Indonesian answer **drawn only from the crawled corpus of approved religious-dialogue websites** (five to start, designed to grow), with 1–2 links back to the source articles.

Every chat is handled by the AI. There is no human agent and this is not a counselling product. It ships through two channels — an **Android app** on the Play Store and an **embedded widget** on WordPress — from one Nuxt codebase, with an editorial admin portal behind it.

All planning specifications live in [`docs/`](docs/README.md). Start there — the code exists to serve those documents, not the other way round.

**Implementation status:** Phase 1 (skeleton) and Phase 2 (chat path on a stub engine) are scaffolded. The answer engine returns a fixed response; there is no corpus, no LLM call, no real auth. Phases 3–5 are specified in [`docs/project-implementation-plan.md`](docs/project-implementation-plan.md) and not yet built.

## The one rule that shapes everything

**No content reaches a user that did not come from the approved corpus.** This is not a quality goal, it is the product's central promise, and it is enforced structurally rather than by prompting:

- The model never sees a URL, so it cannot invent a citation
- Citations can only come from the retrieval result for that request
- Five deterministic validators check every answer *after* generation and can reject it
- If retrieval finds nothing above threshold, the assistant says we have not written about it rather than answering

If a change makes any of those weaker, it is the wrong change regardless of what it improves.

## Tech stack

- **Frontend:** **Nuxt 3 (Vue 3) + Tailwind CSS, SPA mode (`ssr: false`)**, built to static files with `nuxt generate`. Two apps: `web/app/` (seeker) and `web/admin/` (editorial), plus `web/shared/`. Tailwind is wired through Nuxt's built-in PostCSS, **not** `@nuxtjs/tailwindcss` — that module emits a `postcss.mjs` loaded outside ESM context and fails
- **Android:** Capacitor wrapping the same static build. Native phone auth via `@capacitor-firebase/authentication`
- **Backend:** Python 3.12 + FastAPI + Uvicorn on Cloud Run; dependencies via **`uv`**
- **Database:** Firestore, including vector search over `article_chunks`
- **Auth:** Firebase Auth (phone + anonymous); WhatsApp OTP via a provider, converted to a Firebase custom token
- **LLM:** Claude Sonnet class primary on a Zero Data Retention tier, Gemini fallback, behind `backend/providers/llm.py`
- **Embeddings:** Vertex AI `text-multilingual-embedding-002`

## Architecture in one paragraph

A static Nuxt SPA talks to a stateless FastAPI service. Every question runs a fixed pipeline: input bounds → crisis guard → rate limiter → relevance classifier → topic resolver → curated-answer override → vector retrieval → LLM composition → five compliance validators → response assembly. Four of the eight exit paths never call an LLM for composition at all. There is no agent, no tool-calling loop, and no state machine — the model writes one paragraph from passages it was handed, and deterministic code decides whether it ships.

Full detail: [`docs/tdd.md`](docs/tdd.md) and [`docs/ai-answer-engine-specification.md`](docs/ai-answer-engine-specification.md).

## Repository layout

```
backend/
  config/        settings, YAML config, prompt templates   ← editorial sign-off applies here
  models/        Pydantic schemas and enums                ← the wire contract
  storage/       Storage protocol + memory and Firestore backends
  providers/     LLM and OTP adapters                      ← the only place a vendor SDK appears
  services/      guards, sessions, users, auth, text
  engine/        answer engines behind one interface       ← stub today, RAG in Phase 5
  routers/       FastAPI endpoints
  tests/
web/
  shared/        wire types, API client, word counter      ← imported by both frontends
  app/           seeker Nuxt SPA + embed.js
  admin/         editorial Nuxt SPA
```

Two boundaries carry weight. `providers/` is the only place a vendor SDK is imported, which is what makes swapping an LLM a one-adapter change (PRD risk R5). `engine/` sits behind a single `answer()` call, which is what lets Phase 5 replace the stub with the RAG pipeline without touching a router.

## Development commands

**All backend commands use `uv`. Never `pip`, never bare `python`.**

```bash
# Backend
cd backend && uv sync
cd backend && uv run uvicorn main:app --reload
cd backend && uv run pytest -v
cd backend && uv run pytest tests/test_pipeline_order.py -v
cd backend && uv add <package>

# Firestore emulators — dev and test are separate, deliberately
# Not needed while STORAGE_BACKEND=memory, which is the Phase 2 default.
firebase emulators:start --only firestore --config firebase.json        # dev,  UI :4000
firebase emulators:start --only firestore --config firebase.test.json   # test, UI :4001

# Frontends — npm workspaces, so install once at the repo root
npm install
npm run dev:app                                   # http://localhost:3000
npm run dev:admin                                 # http://localhost:3001
npm run build:app                                 # → web/app/.output/public
npm test                                          # web/shared unit tests

# Android
cd web/app && npm run generate && npx cap sync android
cd android && ./gradlew bundleRelease

# Ingestion
cd backend && uv run python -m ingestion.run --dry-run
```

Copy `backend/.env.example` → `backend/.env` before the first run.

**Emulator isolation:** dev uses `127.0.0.1:8080` with `GCLOUD_PROJECT=tanya-iman-local`; tests use `127.0.0.1:8081` with `tanya-iman-local-test`. Never point tests at the dev project — test fixtures wipe all documents between tests.

## Testing requirements

Tests are written alongside the code, not after. Nothing is complete until `cd backend && uv run pytest -v` is green.

- New backend module → `backend/tests/test_<module>.py`
- New endpoint → integration test covering the full request path
- DB-touching code → the test emulator, never a real database

**Additionally:** any change to a prompt, a validator, a retrieval parameter, or a model identifier must pass the 120-question answer benchmark in CI. Its gates — 100% crisis recall, 100% validator pass rate, zero fabricated citations — are release-blocking and not overridable by a reviewer.

## Content rules the engine enforces

| Rule | Requirement | Validator |
|---|---|---|
| 25–250 words | F-11 | V1 |
| Only "Allah" and "Isa Al-Masih"; never "Tuhan" or "Yesus" | F-12 | V2 |
| At most one Quran reference, leading; Bible majority | F-13 | V3 |
| 1–2 citations, all from the approved five domains | F-14 | V4 |
| Every claim traceable to a retrieved passage | F-15 | V5 |

V2 rejects; it never auto-substitutes. Replacing "Tuhan" with "Allah" inside a quoted scripture passage would silently rewrite scripture, which is the one failure this product must never commit.

## Safety constraints

- **Crisis guard runs first**, before the rate limiter. Someone in crisis who has exhausted their quota still gets the helpline
- **Crisis responses come from configuration**, never from the model, and contain no scripture
- **A wrong helpline number is a P0 defect.** No placeholder may reach staging
- **Zero Data Retention** is a hard constraint. A provider that cannot contract for it is disqualified
- **Phone numbers** are encrypted at rest, looked up by HMAC, masked in every admin view, and never exported
- **Guest anonymity is real** — the anonymous identity is not derived from device attributes and is never linked to a phone identity without explicit user conversion

## Assistant persona constraints

The composer must always:

- Acknowledge what the user said before explaining anything
- Answer only from the retrieved passages
- Use only "Allah" and "Isa Al-Masih"
- Stay within 25–250 words
- Never write a URL — the assembler adds links
- Never criticise Islam, Muslims, or the Quran
- Never state a person's salvation status
- Never promise an outcome
- Never ask for personal information
- Never argue. Answer once, kindly, and stop

## Branching

Full rules in [`docs/branching-and-deployment-workflow.md`](docs/branching-and-deployment-workflow.md).

- Never commit directly to `main` or `dev`
- Branches: `feature/…` or `issue/…` only
- PRs merge into `dev`; `dev` deploys to staging; **production deploys from `main` only**
- A change to prompts, response copy, or crisis scripts requires editorial sign-off recorded in the PR
- A change to `approved_sites.yml` requires a PRD update in the same PR

Build order lives in [`docs/project-implementation-plan.md`](docs/project-implementation-plan.md). There is no separate wave / backlog SOP.

## Key reference documents

| Document | Purpose |
|---|---|
| [`docs/README.md`](docs/README.md) | Documentation index and reading order |
| [`docs/prd.md`](docs/prd.md) | Requirements F-1 – F-43, KPIs, risks |
| [`docs/tdd.md`](docs/tdd.md) | Architecture, data model, API, security |
| [`docs/ai-answer-engine-specification.md`](docs/ai-answer-engine-specification.md) | Pipeline, prompts, validators, benchmark |
| [`docs/frontend-framework-decision-nuxt.md`](docs/frontend-framework-decision-nuxt.md) | Nuxt SPA, and how one build serves three targets |
| [`docs/project-implementation-plan.md`](docs/project-implementation-plan.md) | Phases, tasks, tests, blocking dependencies |
| [`docs/chat-ux-specification.md`](docs/chat-ux-specification.md) | Seeker experience and response states |
| [`docs/admin-ux-specification.md`](docs/admin-ux-specification.md) | Editorial portal |
