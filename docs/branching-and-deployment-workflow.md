# Branching and Deployment Workflow

This document defines the **branching and deployment standard** for Tanya Iman. It exists to keep `main` releasable and deployments predictable. It is not a project-management process.

## Core rules (at a glance)

1. **Never commit directly to `main` or `dev`.** All work happens on a branch.
2. **Branches exist only for a feature or an issue.**
3. **Push the branch to GitHub before opening a PR.**
4. **PRs merge into `dev`, not `main`.** `dev` is the integration branch.
5. **QA on staging from `dev` before promoting to `main`.**
6. **Production deploys come from `main` only, never from a branch and never from `dev`.**

## Branch naming

| Purpose | Format | Example |
|---|---|---|
| Feature work | `feature/short-name` | `feature/whatsapp-otp-provider` |
| Issue / bug fix | `issue/number-short-name` | `issue/212-citation-validator` |

Formatting: lowercase, hyphen-separated after the prefix. No other prefixes.

## Workflow

```
1. Branch off the latest dev, using the naming convention.
2. Do the work. Commit as you go. Tests alongside the code, not after.
3. Push the branch to GitHub.                      ← before any PR
4. Open a PR into dev. CI must be green.
5. Merge to dev after review.
6. Deploy dev to STAGING. QA there.
7. Only after staging QA passes: PR dev → main.
8. Deploy to PRODUCTION from main only.            ← never from a branch, never from dev
```

### 1. Create the branch

```bash
git checkout dev
git pull origin dev
git checkout -b feature/whatsapp-otp-provider
```

### 2. Work and commit

Tests are written alongside the code. Before considering anything complete:

```bash
cd backend && uv run pytest -v
```

If the change touches a prompt, a validator, a retrieval parameter, or a model identifier, the **answer benchmark must also pass** — see [AI Answer Engine Specification](ai-answer-engine-specification.md) §13.2. Its gates are release-blocking, not advisory.

### 3. Push before opening a PR

```bash
git push -u origin feature/whatsapp-otp-provider
```

Not optional. It backs the work up, makes it reviewable, and lets CI run against it.

### 4. Open a PR into `dev`

The PR description states what changed, why, and how it was verified. If a `docs/` file needed updating and was not, that is a review comment, not a follow-up ticket.

### 5. Merge to `dev`

After review and green CI. Squash or merge commit — either is fine; consistency within a PR is not worth arguing about.

### 6. QA on staging

Deploy `dev` to staging and QA it there. The manual E2E cases in [Project Implementation Plan](project-implementation-plan.md) §4.4 are the baseline; add cases specific to the change.

### 7. Promote to `main`

Once staging QA passes, open a PR from `dev` to `main`. This is the release decision and it is made deliberately, not by accident of merge order.

### 8. Deploy production from `main`

```bash
./deploy.sh          # production, from main
```

## Environment / target summary

| Target | Deploys from | When |
|---|---|---|
| **Local** | The working branch | Continuously |
| **Staging** | `dev` | After merge to `dev` |
| **Production** | `main` **only** | After staging QA and a `dev` → `main` PR |

> Rule: a branch may be tested locally, and `dev` may be deployed to staging, but neither may ever be the source of a production deploy. Production is fed exclusively by `main`.

## Special rules for this project

**Prompt and copy changes.** A change to `backend/config/prompts/`, `backend/config/responses.id.yml`, or `backend/config/crisis_scripts.id.yml` requires **editorial sign-off recorded in the PR** before merge (AI Spec §14). An engineer approving their own wording change to the crisis script is a process failure, not a shortcut.

**`approved_sites.yml` changes.** Changing the source allowlist changes the product's central promise. It requires a PRD update in the same PR, plus a full re-crawl and a review of curated answers citing a removed site.

**Benchmark-affecting changes.** Any change to prompts, validators, retrieval parameters, or model identifiers runs the answer benchmark in CI. A gate failure blocks the merge; it is not overridable by a reviewer.

**Migrations.** Firestore is schemaless, which makes it easy to ship a read of a field that half the documents do not have. Schema changes follow the four-step sequence in the [Deployment Guide](deployment-guide.md) §8, across separate PRs.

## Checklist before merging to `dev`

- [ ] Branch name follows the `feature/…` or `issue/…` convention
- [ ] `cd backend && uv run pytest -v` passes
- [ ] Both frontends build (`npm run generate`)
- [ ] Answer benchmark passes, if the change touches prompts, validators, retrieval, or models
- [ ] Editorial sign-off recorded, if the change touches prompts or user-facing copy
- [ ] Affected `docs/` files updated in the same PR
- [ ] No secret, `.env`, or credential file in the diff
- [ ] Branch pushed to GitHub

## Checklist before promoting to `main`

- [ ] The change is on `dev` and deployed to staging
- [ ] Staging QA passed, including the relevant PIP §4.4 manual cases
- [ ] `/api/health` on staging reports the expected `prompt_version` and a non-zero `corpus_chunk_count`
- [ ] No open P0 or P1 defect against the change

## Checklist before deploying to production

- [ ] The change is merged into `main`
- [ ] Deploy source is `main` — **not** `dev`, **not** a branch
- [ ] Rollback path confirmed for this specific change (Deployment Guide §9)
- [ ] Someone is watching the validator failure rate and latency for the first hour
