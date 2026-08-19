# **Product Requirements Document (PRD)**

**Project:** Tanya Iman \- Indonesian Theology Q&A for Muslim Seekers

**Version:** 1.0

**Date:** August 2026

Requirements F-1–F-23 originated in the Aug 2026 product brief. This PRD is the authoritative requirement set.

---

## **1\. Product Vision & Objective**

Tanya Iman is an Indonesian-language **theology Q&A assistant**, written for Muslim seekers. A user asks about Allah, Isa Al-Masih, the Quran, the Holy Scripture, or a faith-related struggle, and receives a 25–250 word Indonesian answer drawn **only** from an approved corpus of religious-dialogue websites. Every conversation is handled entirely by the AI. There is no human agent, no volunteer, and no live counsellor in the loop.

The wording of every answer is part of the product. The assistant uses only **"Allah"** and **"Isa Al-Masih"**. The words **"Tuhan"** and **"Yesus"** must never appear. That is not style preference — it is how the answer stays readable and respectful to a Muslim reader.

The corpus starts at **five approved sites** and is designed to grow. Articles are crawled, stored, chunked, and embedded so retrieval — not the model's training data — is what the answer is composed from. Each answer points to one or two source articles for further reading.

The product ships through two channels: an **Android app on the Google Play Store**, and an **embedded widget on the existing WordPress sites**. Behind both sits an editorial admin panel: editors review questions after the fact, see which topics recur, and write canonical answers. They never join the chat.

**What this product is not**

* Not a counselling or pastoral-care service. It does not listen over many turns to "walk with" someone, and it does not hand anyone to a human.
* Not a debate engine. It answers once from the corpus, kindly, and stops.
* Not a general chatbot. Off-topic questions are refused.

**Why "Tanya Iman"?**

*Tanya* means "to ask"; *iman* means "faith". The name is the product promise: a place to ask about faith and receive a sourced answer. It does not promise a verdict, a conversion, a counsellor, or an argument.

---

## **2\. Background & Problem**

The approved sites — starting with isadanislam.org, isadanalquran.com, isadanalfatihah.com, isaislamdankaumwanita.com, and takutneraka.com — have published years of Indonesian religious dialogue written for Muslim readers. That library is real and substantial, but it has three structural problems:

1. **It is scattered.** A reader with one specific theology question must guess which site holds the answer, then search within it.
2. **It is static.** The articles answer the questions their authors anticipated, not the question a particular reader has at 2 a.m.
3. **It is silent about demand.** The editorial team cannot see which questions visitors asked and did not find. Content strategy is driven by intuition rather than evidence.

Tanya Iman crawls that library into a retrieval index, turns a question into a sourced answer, and turns the questions themselves into an evidence stream the editorial team can act on. As more sites are approved, they are added to the same crawl-and-index path — the product does not grow by giving the model more freedom; it grows by giving retrieval more corpus.

---

## **3\. Product Goals & Guiding Principles**

### **3.1 Goals**

| # | Goal | How we will know it worked |
|---|---|---|
| G1 | Answer theology questions quickly, relevantly, and traceably from the approved corpus | ≥85% of relevant questions answered without refusal; 100% of answers carry 1–2 valid source links |
| G2 | Lower the barrier to asking | Guest path requires zero personal data; OTP paths complete in under 60 seconds |
| G3 | Give the editorial team visibility into real demand | Admin panel shows topic distribution and similar-question frequency from day one |
| G4 | Hold Muslim-facing terminology constant across every answer | 100% terminology compliance ("Allah", "Isa Al-Masih"); 0 occurrences of "Tuhan" or "Yesus" in shipped answers |
| G5 | Reach users on both the Play Store and the existing WordPress properties | One codebase, two distribution targets, no feature divergence |
| G6 | Keep the corpus current and expandable | Weekly crawl of every approved site; adding a site is a product change, not a prompt change |

### **3.2 Guiding principles**

* **Grounded or silent.** If the approved corpus does not support an answer, the assistant declines rather than improvises. There is no acceptable rate of invented theology.
* **Traceable by construction.** Every answer carries links back to the articles it came from. A reader who wants to check us can.
* **AI handles every chat.** Editors work offline — reviewing questions, writing canonical answers, expanding the corpus. They never enter the conversation.
* **Speak the reader's language.** "Allah" and "Isa Al-Masih" only. "Tuhan" and "Yesus" are forbidden because they are the Christian register this audience does not use, and using them would make the answer feel like it was written for someone else.
* **Low friction, low data.** Guest access is a first-class path, not a degraded one. We collect a phone number only when the user chooses a channel that requires it.
* **Editorially governable.** Where the editorial team has written a canonical answer for a topic, that answer wins over anything the model would generate.
* **Safe before answering.** Self-harm signals receive a scripted helpline response, not theology and not a human chat. That is a safety rail, not a counselling feature.

---

## **4\. Target Audience**

### **4.1 Primary — the Seeker**

Indonesian-speaking individuals, predominantly from a Muslim background, with theology questions: who is Isa Al-Masih, what the Quran and the Holy Scripture say, the path of salvation, fear of hell, sin and forgiveness, worship and fasting, the search for truth. Faith-related inner struggle that the corpus covers (grief, guilt, anxiety) is in scope as a *question to answer from the writings*, not as a counselling case. They access the internet primarily by mobile phone, may be cautious about being identified, and expect a chat interface to behave like the messaging apps they already use.

### **4.2 Secondary — the Equipper**

Indonesian Christians who want to understand how to talk about faith with Muslim friends or family. They ask the same questions but for a different reason: to learn the answer well enough to give it themselves. The product does not need a separate mode for them, but answer quality and source links matter more to this group.

### **4.3 Tertiary — the Editorial Admin**

IndoPartners editorial staff who review incoming questions, curate the canonical answer per topic, and monitor demand for content strategy. They work on desktop, in bulk, and need throughput more than polish.

---

## **5\. Scope**

### **5.1 In scope — Version 1.0**

* Welcome screen with **Log in with SMS**, **Log in with WhatsApp**, and **Continue as Guest**.
* Privacy Policy link in the footer of every screen.
* Chat screen with a persistent note that answers are based on the Holy Scripture, free-text input, and multi-turn conversation.
* Relevance classification, with a polite standard refusal for questions that are not theology or faith-related.
* Grounded answers of 25–250 words using only "Allah" and "Isa Al-Masih", an optional opening Quranic reference, a Bible-majority body, and 1–2 source article links.
* Crawl, store, chunk, and embed every approved-site article into a retrieval index (RAG). The five sites are the starting allowlist; the list may grow.
* **Like** on every answered response.
* Rate limiting at 30 messages per user per rolling hour.
* Crisis routing for self-harm and acute mental-health signals.
* Admin panel: question list, topic grouping, similar-question frequency, per-topic curated answers, like counts.
* Distribution as an Android app (Google Play Store) and as an embedded widget on WordPress.

### **5.2 Out of scope — Version 1.0**

* iOS app / Apple App Store. The Nuxt + Capacitor architecture keeps this a build-target decision rather than a rewrite, but it is not delivered in 1.0.
* Automated moderation of abusive language and spam on user input. Admins can flag and delete entries manually; automated detection is deferred.
* Live human handover, volunteer chat, or any counselling / pastoral-care session. Every chat is handled by the AI. Crisis responses (F-30) are a scripted helpline message, not a person.
* Multi-language answers, or answers that use "Tuhan" / "Yesus" even when quoting a source that uses those words — the composer must rephrase; the validator must reject.
* Voice input or audio answers.
* User accounts with persisted cross-device history. Sessions are device-local in 1.0; a signed-in user's questions are recorded for admin analytics but are not replayed to them as history on a new device.
* Any language other than Indonesian.

### **5.3 Source-of-truth note — five sites to start, designed to grow**

The Aug 2026 product brief mentioned "6 source websites" in one place and enumerated five in another. **Version 1.0 starts with five**, per the enumerated list in §6.8. The reference to six was a transcription artefact.

The allowlist is expected to grow. Adding or removing a domain is a product decision, not a configuration tweak: it requires updating this section, `backend/config/approved_sites.yml`, a full re-crawl, and a review of any curated answer whose citations point at a removed site. The crawler, the retriever, and the citation validator all read the same file.

---

## **6\. Functional Requirements**

Requirements **F-1** through **F-23** originated in the Aug 2026 product brief, with their original identifiers preserved. Requirements **F-24** and above are new in this PRD; Appendix B records the full traceability.

### **6.1 Onboarding & Authentication**

| ID | Requirement |
|---|---|
| **F-1** | On first open, the app displays an Indonesian welcome screen with three options: "Masuk dengan SMS", "Masuk dengan WhatsApp", and "Lanjutkan sebagai Tamu". |
| **F-2** | The SMS and WhatsApp flows collect a mobile number, send a one-time verification code over the chosen channel, and verify the code before granting access to the chat screen. |
| **F-3** | "Lanjutkan sebagai Tamu" grants immediate access to the chat screen and collects no personal data. |
| **F-4** | Every screen displays a footer link to the Privacy Policy. |
| **F-5** | The user can log out at any time and return to the welcome screen. |
| **F-24** | OTP entry is limited to 5 attempts per code and 3 code requests per number per hour. Exceeding either limit shows an Indonesian cooldown message with the time remaining. |
| **F-25** | A Guest user can convert to an SMS or WhatsApp account without losing the current on-screen conversation. |

### **6.2 Q&A Screen (Chat)**

| ID | Requirement |
|---|---|
| **F-6** | After sign-in, the app shows a greeting asking how it can help, with a small persistent note that answers are based on the Holy Scripture. |
| **F-7** | The user can type a free-form question and send it. |
| **F-8** | The user can ask repeatedly within one session; every question and answer is appended to a single scrolling conversation view. |
| **F-9** | The system classifies each question as relevant (theology or faith-related) or irrelevant before generating an answer. |
| **F-26** | While an answer is being generated the app shows a typing/progress indicator, and the input remains usable but send is disabled until the answer resolves. |
| **F-27** | If answer generation fails or times out, the app shows an Indonesian error state with a **Coba lagi** action that resubmits the same question without the user retyping it. |

### **6.3 Answer Content Rules**

| ID | Requirement |
|---|---|
| **F-10** | If a question is not theology or faith-related, the app returns a standard Indonesian apology and does not attempt to answer the content of the question. |
| **F-11** | Every non-refusal answer is at least 25 and at most 250 words. |
| **F-12** | Answers use only the terms "Allah" and "Isa Al-Masih". The terms "Tuhan" and "Yesus" (and "Jesus") must not appear, including inside quoted scripture. The validator rejects; it never auto-substitutes. |
| **F-13** | Where relevant, an answer may open with a brief reference from the Quran; the substantial majority of scriptural quotation must come from the Bible. |
| **F-14** | Every non-refusal answer includes 1–2 links to related articles from the currently approved sites. |
| **F-15** | All answer content must derive from the crawled corpus of approved sites. No information from outside that corpus may appear in an answer. |
| **F-16** | A single user may send at most 30 messages per rolling hour. |
| **F-28** | An answer that fails any content rule (F-11 through F-15) must not be shown to the user. The system repairs and revalidates it; if it still fails, the user receives a graceful fallback and the failure is logged for admin review. |
| **F-29** | If retrieval finds no corpus passage above the relevance threshold, the system returns a "we do not have material on this yet" response rather than answering from model knowledge, and records the gap as a content opportunity for the editorial team. |

### **6.4 Safety & Crisis Handling**

| ID | Requirement |
|---|---|
| **F-30** | Messages containing self-harm, suicide, or acute mental-health crisis signals bypass the answer engine entirely and return a pre-approved Indonesian crisis response containing at least one national helpline. |
| **F-31** | Crisis responses are authored and approved by the editorial team before launch. They are served from configuration, never generated by the model, and never open a human chat. |
| **F-32** | Crisis events are recorded (without answer generation) so admins can see frequency and review the handling, and are excluded from ordinary topic analytics. |

### **6.5 "Like" Interaction**

| ID | Requirement |
|---|---|
| **F-17** | Every answered response (never a refusal or crisis response) shows a Like control the user can press to mark the answer helpful. |
| **F-18** | Like counts are persisted per answer and per topic and are visible to admins. |
| **F-33** | Like is idempotent per user per answer and can be undone. Guest likes are attributed to the anonymous session identity. |

### **6.6 Admin Panel**

| ID | Requirement |
|---|---|
| **F-19** | The admin panel is reachable only through authentication that is separate from end-user accounts. |
| **F-20** | Admins can browse every question asked, with timestamp, assigned topic, and like count. |
| **F-21** | Admins can view questions grouped by topic with a count per topic. |
| **F-22** | Admins can see how frequently semantically similar questions are asked. |
| **F-23** | Admins can add or edit the canonical answer for a topic, with automatic validation that the answer stays within 25–250 words. |
| **F-34** | Admin edits to a curated answer are validated against the same content rules as generated answers (F-11 through F-14) before they can be saved. |
| **F-35** | Admins can filter the question list by date range, topic, refusal status, crisis flag, and "no grounding found". |
| **F-36** | Admins can export the filtered question list as CSV for offline analysis. |
| **F-37** | Destructive admin actions (delete a question, delete a curated answer, change a system setting) are written to an audit log before execution. |

### **6.7 Distribution**

| ID | Requirement |
|---|---|
| **F-38** | The web build is embeddable on a WordPress page as a widget that does not require the host page to be rebuilt, and adapts to the host container width. |
| **F-39** | The Android build is produced from the same frontend codebase and passes Google Play's pre-launch checks for a religious-content application. |
| **F-40** | Both distributions talk to the same backend API; there is no channel-specific answer logic. |

### **6.8 Content Sources**

Every answer must be traceable to a site on the approved allowlist. Version 1.0 starts with these five:

* `isadanislam.org`
* `isadanalquran.com`
* `isadanalfatihah.com`
* `isaislamdankaumwanita.com`
* `takutneraka.com`

The list may grow. `backend/config/approved_sites.yml` is the single allowlist used by the crawler (write time), the retriever (query time), and the citation validator (display time). See **Content Ingestion & RAG Runbook**.

### **6.9 Corpus ingestion (crawl → RAG)**

| ID | Requirement |
|---|---|
| **F-41** | The system crawls every domain on the allowlist, extracts article text, chunks it, embeds it, and stores it for vector retrieval. Answers are composed only from retrieved chunks. |
| **F-42** | Adding a site to the allowlist triggers a crawl of that site and makes its articles eligible for retrieval and citation. Removing a site retires its chunks and requires a review of curated answers that cited it. |
| **F-43** | Ingestion is resumable and idempotent. Unchanged articles produce no writes. A weekly scheduled run keeps the index current; an admin can trigger a run on demand. |

---

## **7\. Non-Functional Requirements**

### **7.1 Platform & distribution**

* A responsive web application that can be embedded as a widget on WordPress pages **and** wrapped as an Android app for the Play Store, from one codebase.
* Mobile-first. The majority of traffic will be mobile; desktop is a secondary layout, not the design baseline.
* The web build must be fully static (no server-rendered HTML at request time), so that it can be served from a CDN and packaged into an Android binary without a Node runtime. See **Frontend Framework Decision — Nuxt**.

### **7.2 Language & localisation**

* The entire interface, every answer, and all system messaging are in Indonesian.
* Strings live in a single message catalogue so that copy can be revised by non-engineers.

### **7.3 Performance**

| Measure | Target |
|---|---|
| Answer returned to the user (p50) | < 5 s |
| Answer returned to the user (p95) | < 9 s |
| First contentful paint on 3G mobile | < 3 s |
| Initial JS bundle (widget entry) | < 250 KB gzipped |
| Refusal / crisis response | < 1 s (no LLM call in the path) |

### **7.4 Security & data privacy**

* Mobile numbers collected via SMS or WhatsApp are stored encrypted at rest, used only for authentication and session recognition, and never displayed in full in the admin panel.
* Guest users generate no personally identifiable data. The anonymous identifier must not be derivable from device fingerprinting.
* The admin panel is protected by real authentication with per-account credentials — never a shared static password — and access control is enforced at the data layer, not only in the UI.
* LLM calls use a Zero Data Retention tier. No user question may be retained by a model provider for training.
* Question text is retained for editorial analytics; the retention window is configurable and defaults to 12 months.

### **7.5 Scalability**

* The data model for questions, answers, users, and article chunks must absorb growth in question volume without schema redesign.
* Retrieval latency must stay within the p95 budget as the corpus grows from the initial ~68 articles to several thousand chunks.
* The admin question list must remain usable at 100,000+ records via server-side pagination and filtering.

### **7.6 Accessibility**

* WCAG 2.1 AA contrast minimum.
* Full keyboard operability of the chat and admin interfaces.
* No information conveyed by colour alone.
* Text resizes to 200% without loss of function.

---

## **8\. User Stories**

### **8.1 Seeker**

* **US-1** — As someone with a question I am embarrassed to ask a person, I want to ask anonymously, so that I can explore without being identified.
* **US-2** — As a reader who wants to verify what I am told, I want links to the source articles, so that I can read further myself.
* **US-3** — As a Muslim asking about Isa Al-Masih, I want the answer to use "Allah" and "Isa Al-Masih", so that it reads as written for me rather than as a church tract.
* **US-4** — As a user on a slow connection, I want to see that my question was received, so that I do not send it three times.
* **US-5** — As a returning user, I want to sign in with the phone number I already use for WhatsApp, so that I do not have to remember a password.

### **8.2 Equipper**

* **US-6** — As a Christian preparing to talk with a Muslim friend, I want an answer that uses the terms my friend uses, so that the conversation does not stall on vocabulary.

### **8.3 Editorial Admin**

* **US-7** — As an editor, I want to see the twenty most-asked topics this month, so that I know what to write next.
* **US-8** — As an editor, I want to see questions where the system found no grounding, so that I can identify gaps in our corpus.
* **US-9** — As an editor, I want to write the definitive answer for "Path of Salvation" once, so that every user asking about it gets our approved wording rather than a fresh generation.
* **US-10** — As an editor, I want to know which answers were liked, so that I can learn what lands.

---

## **9\. Primary Use Cases**

* **UC-1 — Anonymous first question.** A user opens the app, taps *Lanjutkan sebagai Tamu*, reads the greeting, and asks "Apakah Isa Al-Masih benar-benar wafat?". The system classifies the question as relevant, retrieves passages from the corpus, composes a 180-word answer opening with a Quranic reference and citing two Bible passages, appends two article links, and displays it. The user taps Like.
* **UC-2 — Out-of-scope question.** A user asks for tomorrow's football scores. The classifier marks it irrelevant, and the standard Indonesian refusal is returned in under a second without an LLM call.
* **UC-3 — Curated answer served.** A user asks about the path of salvation. The topic resolves to a topic with an editor-curated answer, and that exact text is returned with its configured source links, bypassing generation.
* **UC-4 — Grounding gap.** A user asks a spiritual question about a subject the corpus does not cover. Retrieval returns nothing above threshold, so the system returns the "we do not have material on this yet" response and flags the question in the admin *Content Gaps* view.
* **UC-5 — Crisis signal.** A user writes that they want to end their life. The crisis guard fires before any other processing, and the pre-approved response with helpline numbers is returned. The event is logged and excluded from topic analytics.
* **UC-6 — Rate limit reached.** A user sends their 31st message within an hour. The system returns the Indonesian rate-limit message with the time until the window resets.
* **UC-7 — Editorial review cycle.** An admin logs in, filters the last 30 days by topic, sees "Fear of Hell" leading with 412 questions, reads a sample of the raw wording, and rewrites the curated answer for that topic. The word-count and terminology validators pass and the answer is saved with the admin's name and timestamp.
* **UC-8 — Widget on WordPress.** A visitor reading an article on isadanislam.org sees the Tanya Iman widget embedded below the article, asks a question inside it, and receives the same answer they would have received in the Android app.

---

## **10\. Data Model (Product View)**

The engineering-level schema lives in the **Technical Design Document** §3. This is the product's view of what the system remembers.

| Entity | What it holds | Why the product needs it |
|---|---|---|
| **User** | Identifier, auth method (`sms` / `whatsapp` / `guest`), phone number (only when provided), created and last-active timestamps | Session recognition, rate limiting, and the ability to say how many people use the product |
| **Session** | A conversation on one device, its user, and its messages | Multi-turn context (F-8) and the per-session engagement metric |
| **Question** | The question text, the answer text, assigned topic, similar-question cluster, source links, like count, refusal / crisis / no-grounding flags, latency, timestamp | The entire admin analytics surface (F-20 through F-22) and the KPI set |
| **Topic** | Name, curated answer, curated source links, last editor, last updated, aggregate question and like counts | Editorial governance (F-23) and topic grouping (F-21) |
| **Article** | Source site, title, URL, publication date, summary, assigned topics, crawl metadata | The corpus index and the citations shown to users (F-14) |
| **Article chunk** | A retrievable passage of an article, its embedding, and its parent article | Retrieval and grounding (F-15) |
| **Question cluster** | A canonical phrasing, a centroid, and the count of questions that map to it | Similar-question frequency (F-22) |
| **Admin user** | Identity, role, last login | Separate admin authentication (F-19) |
| **Audit log** | Actor, action, target, timestamp | Accountability for destructive actions (F-37) |

---

## **11\. Success Metrics (KPIs)**

| # | Metric | Definition | Initial target |
|---|---|---|---|
| K1 | Answer rate | Non-refused answers ÷ all in-scope theology / faith questions | Baseline in pilot; ≥85% by launch + 60 days |
| K2 | Like rate | Likes ÷ answers shown | Trend upward month over month |
| K3 | Questions per session | Mean questions in one session | 1–50, with a healthy median above 2 |
| K4 | Content-rule compliance | Answers passing all of F-11 to F-15 at display time | **100%** — this is a gate, not a trend |
| K5 | Answer latency | p50 and p95 time to display | p50 < 5 s, p95 < 9 s |
| K6 | Weekly active users | Distinct users with ≥1 question in a week | Set after launch baseline |
| K7 | Grounding-gap rate | Questions returning no-grounding ÷ relevant questions | < 10%, and falling as the corpus grows |
| K8 | Curated coverage | Share of answered questions served from a curated topic answer | Grows as the editorial team writes canonical answers |
| K9 | Crisis routing precision | Sampled crisis-flagged messages that were genuinely crisis | Reviewed monthly; false negatives are P0 defects |

K4 and K9 are safety and compliance gates. A regression in either blocks release regardless of other metrics.

---

## **12\. Assumptions & Dependencies**

* The five source sites stay reachable and permit periodic crawling for this purpose, and the ministry holds or has been granted the right to reuse that content in generated answers.
* Accounts exist or will be created before production launch for: Firebase / Google Cloud, a WhatsApp OTP provider, an LLM provider on a Zero Data Retention tier, and Google Play Developer.
* An editorial reviewer is available to approve the answer-engine system prompt, the refusal copy, and the crisis scripts **before** the pilot, not after.
* The chosen LLM handles Indonesian well and can be constrained to answer only from supplied context.
* The Phase 1 prototype (keyword engine, 68 seeded articles, full UI flow) exists and can be used as the reference for interaction behaviour, though not as the production codebase.

---

## **13\. Risks & Mitigations**

| # | Risk | Impact | Mitigation |
|---|---|---|---|
| R1 | Generated answers are theologically inaccurate or off-tone | Severe — reputational and theological | Strict grounding to retrieved passages, deterministic post-generation validators (including F-12), editorial curated answers that override generation, periodic manual review of sampled answers |
| R2 | Relevance classification is ambiguous at the edges | Medium — users refused unfairly, or off-topic questions answered | LLM-based classification rather than keywords, an explicit "ambiguous → answer with caution" band, and an admin review queue of borderline classifications used to refine the prompt |
| R3 | Google Play policy on religious and proselytising content | Severe — store rejection blocks a whole channel | Review the Play Developer Program policy before submission, prepare a clear listing describing purpose and audience, keep the app free of targeted or deceptive claims, budget for one rejection-and-resubmit cycle |
| R4 | Abuse of the question field (spam, abusive language) | Medium | Rate limiting at 30/hour in 1.0, admin flag-and-delete, automated moderation deferred to the next phase with a defined trigger |
| R5 | Third-party dependency change (OTP or LLM pricing, availability, terms) | Medium–high | Provider abstraction layer at the code level so a swap does not touch business logic; usage-cost monitoring with alerting; a documented fallback model |
| R6 | A user in genuine crisis receives a theological answer instead of help | Severe — safety | Crisis guard runs before classification and retrieval; scripted responses only; false negatives treated as P0; monthly sampled review (K9) |
| R7 | Corpus is too thin for the questions people actually ask | Medium | Grounding-gap tracking (K7) feeds the editorial content queue; refuse rather than invent |
| R8 | Phone numbers leak or are misused | Severe — privacy and user safety | Encryption at rest, masked display in admin, no export of raw numbers, access enforced at the data layer |
| R9 | Widget embedding conflicts with host WordPress themes | Low–medium | Iframe isolation with a documented embed snippet, height negotiation via `postMessage`, and a tested matrix of the five host sites |

---

## **14\. Phased Release Plan**

The engineering breakdown lives in the **Project Implementation Plan**. This is the product-level sequence.

| Phase | Outcome | Gate to the next phase |
|---|---|---|
| **P1 — Prototype & validation** *(complete)* | Keyword answer engine, ~68 seeded articles, full UI flow across onboarding, chat, and admin | Interaction model validated with real users |
| **P2 — Production foundation** | Nuxt frontend and backend skeleton, Firestore data model, Guest auth, ask endpoint at prototype parity | Guest can ask and receive an answer on staging |
| **P3 — Identity** | Firebase phone auth for SMS, WhatsApp OTP provider, session model, rate limiting, hardened admin auth | All three sign-in paths work end to end on staging |
| **P4 — Corpus** | Crawl of all five sites, chunking, embeddings, vector index, article metadata | Retrieval returns relevant passages for a benchmark question set |
| **P5 — Production answer engine** | Crisis guard, relevance classifier, RAG composition, compliance validators, curated-answer override | K4 = 100% on the benchmark set; editorial sign-off on prompts and refusal copy |
| **P6 — Editorial surface** | Admin portal: question list, topic grouping, similar-question clustering, curated answers, likes, export | Editorial team can complete one full review cycle unaided |
| **P7 — Distribution** | WordPress widget embed, Capacitor Android build, Play Store listing prepared | Widget live on one host site; internal Android build installs and works |
| **P8 — Pilot** | Supervised pilot on staging with real testers, per the **Pilot Plan** | Exit criteria in the Pilot Plan met; go / no-go recorded |
| **P9 — Launch** | Widget on all five WordPress sites, Play Store submission, post-launch monitoring | KPI baselines captured; K4 and K9 green |

---

## **15\. Open Product Decisions**

These need an owner and a date before the phase that depends on them.

| # | Decision | Needed by | Default if undecided |
|---|---|---|---|
| OD-1 | Which WhatsApp OTP provider (Twilio Verify vs alternative), and the per-message cost ceiling | P3 | Twilio Verify |
| OD-2 | Retention window for question text | P2 | 12 months |
| OD-3 | Whether a signed-in user's history follows them to a new device | P3 | No — device-local only in 1.0 |
| OD-4 | Which national helplines appear in the crisis script, and their verification date | P5 | Blocks P5 — no default |
| OD-5 | Whether the widget is embedded on all five sites at launch or staged | P9 | One site first, then the rest after 7 days |
| OD-6 | Who owns editorial sign-off on the system prompt, and the re-review cadence | P5 | Blocks P5 — no default |

---

## **Appendix A: Supported Topics**

The initial topic taxonomy. Each is a grouping key for admin analytics (F-21) and a slot for a curated answer (F-23).

| # | Topic (Indonesian) | Topic (English) | Slug |
|---|---|---|---|
| 1 | Kasih Allah | Love of Allah | `kasih-allah` |
| 2 | Jalan Keselamatan | Path of Salvation | `jalan-keselamatan` |
| 3 | Takut Neraka | Fear of Hell | `takut-neraka` |
| 4 | Ketenangan Hati | Peace of Mind | `ketenangan-hati` |
| 5 | Dosa & Pengampunan | Sin & Forgiveness | `dosa-pengampunan` |
| 6 | Duka & Kehilangan | Grief & Loss | `duka-kehilangan` |
| 7 | Kecemasan & Depresi | Anxiety & Depression | `kecemasan-depresi` |
| 8 | Pernikahan & Keluarga | Marriage & Family | `pernikahan-keluarga` |
| 9 | Jati Diri Isa Al-Masih | Identity of Isa Al-Masih | `jati-diri-isa-almasih` |
| 10 | Kematian Isa Al-Masih | Death of Isa Al-Masih | `kematian-isa-almasih` |
| 11 | Keaslian Kitab Suci | Authenticity of the Holy Scripture | `keaslian-kitab-suci` |
| 12 | Ibadah & Puasa | Worship & Fasting | `ibadah-puasa` |
| 13 | Pencarian Kebenaran | Search for Truth | `pencarian-kebenaran` |

A fourteenth pseudo-topic, `lainnya` (Other), catches relevant questions that do not map to any of the thirteen. A rising count in `lainnya` is a signal that the taxonomy needs extending.

---

## **Appendix B: Requirement Traceability**

| Requirement range | Origin | Notes |
|---|---|---|
| F-1 – F-5 | Aug 2026 product brief | Unchanged; Indonesian button copy specified |
| F-6 – F-9 | Aug 2026 product brief | Unchanged |
| F-10 – F-16 | Aug 2026 product brief | Unchanged; F-13 wording clarified ("substantial majority") |
| F-17 – F-18 | Aug 2026 product brief | Unchanged |
| F-19 – F-23 | Aug 2026 product brief | Unchanged |
| F-24 – F-27 | New | OTP throttling, guest conversion, loading and error states — implied by the original brief but not previously stated as requirements |
| F-28 – F-29 | New | Makes the enforcement of F-11 to F-15 a testable requirement rather than an aspiration |
| F-30 – F-32 | New | Crisis handling. Not present in the original brief; added because the in-scope topic list includes anxiety, depression, and grief |
| F-33 | New | Like idempotency and undo |
| F-34 – F-37 | New | Admin validation parity, filtering, export, and audit logging |
| F-38 – F-40 | New | Distribution requirements promoted from the original brief's platform prose into testable requirements |
| F-41 – F-43 | New | Crawl → store → embed → retrieve as a first-class product capability; allowlist designed to grow |

---

## **Related Documents**

| Document | Purpose |
|---|---|
| [Technical Design Document (TDD)](tdd.md) | Architecture, components, schema, security |
| [AI Answer Engine Specification](ai-answer-engine-specification.md) | Pipeline, prompts, validators, grounding rules |
| [Frontend Framework Decision — Nuxt](frontend-framework-decision-nuxt.md) | Why Nuxt SPA, and how one codebase serves three targets |
| [Chat UX Specification](chat-ux-specification.md) | Seeker-facing interaction and copy |
| [Admin UX Specification](admin-ux-specification.md) | Editorial portal interaction |
| [Project Implementation Plan](project-implementation-plan.md) | Phased build plan and test strategy |
| [Content Ingestion & RAG Runbook](content-ingestion-and-rag-runbook.md) | Crawling, chunking, embedding, refresh |
| [Pilot Plan](pilot/pilot-plan.md) | Supervised pilot and exit criteria |
