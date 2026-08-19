# Tanya Iman — Documentation

Planning and specification documents for **Tanya Iman**, an Indonesian-language theology Q&A assistant for Muslim seekers. Answers come only from a crawled corpus of approved religious-dialogue websites (five to start, designed to grow). Every chat is handled by the AI — there is no human agent and this is not a counselling product. It ships as a WordPress widget and an Android app, with an editorial admin portal behind it.

**Frontend stack:** Nuxt 3 (Vue 3) + Tailwind CSS in SPA mode, built to static files — one artefact serving web, widget, and Android.

---

## Where to start

| If you are… | Read, in this order |
|---|---|
| **New to the project** | [PRD](./prd.md) → [TDD](./tdd.md) → [Project Implementation Plan](./project-implementation-plan.md) |
| **Building the frontend** | [Frontend Framework Decision — Nuxt](./frontend-framework-decision-nuxt.md) → [Chat UX Specification](./chat-ux-specification.md) → [Admin UX Specification](./admin-ux-specification.md) |
| **Building the answer engine** | [AI Answer Engine Specification](./ai-answer-engine-specification.md) → [Content Ingestion & RAG Runbook](./content-ingestion-and-rag-runbook.md) |
| **Deploying or operating** | [Deployment Guide](./deployment-guide.md) → [Android & WordPress Distribution Runbook](./android-and-wordpress-distribution-runbook.md) → [Branching and Deployment Workflow](./branching-and-deployment-workflow.md) |
| **Picking up work today** | [Project Implementation Plan](./project-implementation-plan.md) — phases and tasks |
| **Running the pilot** | [pilot/Pilot Plan](./pilot/pilot-plan.md) |

---

## Document map

### Product

| Document | What it decides |
|---|---|
| [Product Requirements Document (PRD)](./prd.md) | Scope, requirements F-1 – F-43, user stories, KPIs, risks, release plan. **The authoritative requirement set** |

### Architecture & design

| Document | What it decides |
|---|---|
| [Technical Design Document (TDD)](./tdd.md) | Components, Firestore data model, API surface, environments, security |
| [Frontend Framework Decision — Nuxt](./frontend-framework-decision-nuxt.md) | Nuxt 3 SPA, why not SSR, how one build serves web + widget + Android |
| [AI Answer Engine Specification](./ai-answer-engine-specification.md) | The answer pipeline, Indonesian prompts, the five compliance validators, the benchmark and its release gates |

### Experience

| Document | What it decides |
|---|---|
| [Chat UX Specification](./chat-ux-specification.md) | Seeker screens, every response state, embed and Android behaviour, copy inventory |
| [Admin UX Specification](./admin-ux-specification.md) | Editorial portal: question list, topics, clusters, gaps, curated answer editor |

### Build & operate

| Document | What it decides |
|---|---|
| [Project Implementation Plan](./project-implementation-plan.md) | Nine phases, tasks, per-phase tests, blocking dependencies |
| [Content Ingestion & RAG Runbook](./content-ingestion-and-rag-runbook.md) | Crawl, chunk, embed, refresh, monitor, troubleshoot the corpus |
| [Deployment Guide (Google Cloud & Firebase)](./deployment-guide.md) | Projects, secrets, deploys, rollback, pre-launch checklist |
| [Android & WordPress Distribution Runbook](./android-and-wordpress-distribution-runbook.md) | Widget embed and QA; Play Store build, listing, tracks, device matrix |
| [Branching and Deployment Workflow](./branching-and-deployment-workflow.md) | Branch naming, PR flow, what may deploy from where |

### Pilot

| Document | Purpose |
|---|---|
| [pilot/Pilot Plan](./pilot/pilot-plan.md) | Scenarios, schedule, exit criteria |
| [pilot/Pilot Session Log Template](./pilot/pilot-session-log-template.md) | Per-session record |
| [pilot/UX Feedback Report Template](./pilot/ux-feedback-report-template.md) | Per-participant experience |
| [pilot/AI Answer Quality Report Template](./pilot/ai-answer-quality-report-template.md) | Editorial review of answer quality |

---

## The things that block everything else

Several dependencies are owned outside engineering and are listed in [PIP §6](./project-implementation-plan.md). The two that matter most:

1. **The crisis script and its helpline numbers** must be written and verified by the editorial team before Phase 5. A wrong number is a P0 safety defect. This is a safety rail, not a counselling feature — there is still no human in the chat.
2. **Zero Data Retention terms** must be confirmed in writing before a single real user question reaches a model provider.

Crawl permission for the approved sites is the third: Phase 4 cannot index what we are not allowed to store.

---

## Conventions used across these documents

- **Requirement IDs** — `F-1` through `F-43`, defined in [PRD §6](./prd.md) and referenced everywhere else. F-1 – F-23 originated in the Aug 2026 product brief; F-24 onward are new, with traceability in PRD Appendix B.
- **KPI IDs** — `K1` – `K9`, in PRD §11. `K4` (content-rule compliance) and `K9` (crisis routing) are gates, not trends.
- **Open decisions** — `OD-1` – `OD-6` in the PRD; `OI-1` – `OI-7` in the AI Answer Engine Specification; `B1` – `B9` blocking dependencies in the PIP.
- **Cross-references** — by document name and section, e.g. *AI Spec §8.2*, *TDD §3.7*.
- **Indonesian** — all user-facing copy is Indonesian and lives in one catalogue per surface. These documents are in English; the strings they specify are not.
