# AI Answer Quality Report — Tanya Iman

**Reviewer:** _________________ · **Date:** _________________
**Batch:** _____ answers · **Date range reviewed:** _________________
**`prompt_version`:** _________________ · **Model:** _________________

> This review measures whether the answers are **good**, not whether they passed validation. The validators already guarantee word count, terminology, citations, and grounding. Only a person can judge whether an answer was true, kind, and worth sending. Where this report and the automated metrics disagree, this report is the one that matters.

---

## Per-answer scoring

Score each sampled answer. Use `question_id` only — no personal detail.

| # | `question_id` | Topic | Accurate | Grounded | Tone | Addressed the question | Would publish as-is | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | | | 1–5 | 1–5 | 1–5 | 1–5 | Yes / No | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

**Scale:**

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Accurate** | Theologically wrong | Defensible but imprecise | Correct and well expressed |
| **Grounded** | Says things the sources do not | Mostly traceable, some drift | Every claim traceable to a cited source |
| **Tone** | Cold, preachy, or argumentative | Neutral | Warm, unhurried, meets the person where they are |
| **Addressed the question** | Answered a different question | Answered partly | Answered exactly what was asked |

---

## Aggregate

| Metric | Value |
|---|---|
| Answers reviewed | |
| Mean accuracy | |
| Mean grounding | |
| Mean tone | |
| Mean relevance to question | |
| Share the reviewer would publish as-is | % |
| Answers with a **theological error** | |
| Answers that **drifted from the sources** | |
| Answers that **argued rather than answered** | |

---

## Theological errors found

Any answer scoring 1 or 2 on accuracy. These are the highest-priority findings in this document.

| # | `question_id` | What was wrong | Which cited source it came from, if any | Suggested fix |
|---|---|---|---|---|
| | | | | |

**Was the error caused by the model, or by the source article it cited?** This distinction determines whether the fix is a prompt change or a corpus change, and it is the most useful thing this report can establish.

---

## Tone findings

| Pattern observed | How often | Example `question_id` |
|---|---|---|
| Preached instead of answering | | |
| Ignored the emotion in the question | | |
| Opened with theology before acknowledgement | | |
| Felt templated across different questions | | |
| Ended with pressure rather than invitation | | |

---

## Terminology and scripture balance

Validators enforce the rules mechanically. This section captures whether the *result* reads well.

| Question | Response |
|---|---|
| Did the required terminology ever make an answer read awkwardly? | |
| Were Quranic references used appropriately, or bolted on? | |
| Did Bible references support the point, or decorate it? | |
| Any answer where a rule produced a worse answer than breaking it would have? | |

The last question matters. If a rule is consistently producing worse answers, that is a finding for the PRD, not something for the engine to work around.

---

## Refusals and gaps reviewed

| # | `question_id` | Should it have been answered? | Comment |
|---|---|---|---|
| | | Yes / No | |

**False refusals found:** _____ of _____ refusals reviewed.
**Questions that should have been refused but were answered:** _____

---

## Curated answer opportunities

Topics where the reviewer believes a curated answer would be materially better than what the engine produced.

| Topic | Why | Priority |
|---|---|---|
| | | High / Medium / Low |

---

## Reviewer's judgment

**Are these answers acceptable to publish to the public?** Yes / Yes with changes / No

**If "with changes", what must change first:**

**If "No", the specific reason:**

**Recommended prompt or corpus changes:**

**Signed:** _________________ **Date:** _________________
