# Tanya Iman
**Original product brief**
*Version 1.0 — August 6, 2026*

> Historical. The authoritative requirement set is [`prd.md`](prd.md). This file is kept so later decisions can be traced. Do not implement from it.

## 1. Executive Summary
Tanya Iman is an Indonesian-language spiritual and emotional Q&A application that answers user questions solely based on content from five approved religious dialogue websites. The application greets users with login options via SMS, WhatsApp, or as a Guest, then allows them to ask questions repeatedly in a single conversation. Each answer is composed of 25–250 words, uses the terms "Allah" and "Isa Al-Masih", includes a Quranic reference at the beginning and more verses from the Bible, and links 1–2 reference articles. Questions outside spiritual/emotional topics will be politely declined. The product will be distributed as an Android application on the Google Play Store and as an embedded widget on WordPress sites, equipped with an internal admin panel to review questions, add/modify answers, and monitor frequently asked topics and question frequencies.

## 2. Background & Problem
Many people have deep spiritual and emotional questions but lack a safe, fast, and anytime-accessible space to explore them. The five source websites (isadanislam.org, isadanalquran.com, isadanalfatihah.com, isaislamdankaumwanita.com, takutneraka.com) have long provided rich religious dialogue and emotional support articles, but this content is scattered across many static sites and can only be found through manual search. There is no way for users to ask their specific questions directly and receive personalized answers while strictly adhering to the approved sources. The editorial team also lacks visibility into what questions visitors ask most frequently, making it difficult to prioritize new content.

## 3. Product Goals
* Provide fast, relevant, and trustworthy answers to users' spiritual/emotional questions, solely based on content from the five approved websites.
* Lower the barrier to entry with familiar login options (SMS/WhatsApp) as well as a Guest option without requiring registration.
* Give the editorial team visibility into the questions asked by users, including grouping by topic and frequency of similar questions, to prioritize new content.
* Ensure consistency in tone and theological terms (Allah, Isa Al-Masih) across all answers.
* Reach users across two main channels: a standalone app on the Google Play Store, and an embedded widget on existing WordPress sites.

## 4. Target Users

### 4.1 End Users
Indonesian-speaking individuals — mostly from a Muslim background — who have questions about faith, Isa Al-Masih, the Quran, the Bible, or emotional struggles (anxiety, grief, guilt, fear of hell, etc.) and are seeking easily accessible answers via their mobile phones. Users can choose to remain anonymous (Guest) or log in with their mobile number. But also Christians who want to learn how to reach out to their friends or family.

### 4.2 Internal Team / Admin
Editorial staff from IndoPartners responsible for reviewing incoming questions, adding or updating answers per topic, and monitoring question trends for content strategy purposes.

## 5. Product Scope

### 5.1 In Scope (Version 1.0)
* Welcome screen with SMS, WhatsApp, or Continue as Guest login options.
* Privacy Policy link in the footer, accessible from any screen.
* Q&A screen with a note that answers are based on the "Holy Scripture", free-text input, and multi-turn conversation support (users can ask multiple times).
* Polite refusal for questions outside spiritual/emotional topics.
* 25–250 word answers with the terms "Allah"/"Isa Al-Masih", a Quranic reference at the beginning (if relevant) and a majority of quotes from the Bible, as well as 1–2 reference article links from the 6 source websites. *(Note: Text mentions 5 sources elsewhere, but exactly translated as '6' from "6 situs sumber" in source text)*.
* "Like" button on every answer.
* Admin panel: list of all questions, grouping by topic, frequency of similar questions, and the ability to add/modify answers per topic.
* Distribution as an Android app (Google Play Store) and embedded WordPress widget.

### 5.2 Out of Scope (Version 1.0)
* iOS App / App Store (can be considered in the next phase using the same codebase).
* Automated moderation of abusive language/spam on user input (recommended for the next phase).

## 6. Functional Requirements

### 6.1 Onboarding & Authentication
| ID | Requirement |
| :--- | :--- |
| **F-1** | Upon opening for the first time, the app displays an Indonesian-language welcome screen with three options: "Log in with SMS", "Log in with WhatsApp", and "Continue as Guest". |
| **F-2** | The SMS/WhatsApp flow asks for a mobile number, sends a verification code (OTP) via the selected channel, then verifies the code before granting access to the chat screen. |
| **F-3** | The "Continue as Guest" option grants direct access to the chat screen without collecting any personal data. |
| **F-4** | The footer on the welcome screen (and all other screens) displays a link to the Privacy Policy page. |
| **F-5** | Users can "Log out" of their session at any time and return to the welcome screen. |

### 6.2 Q&A Screen (Chat)
| ID | Requirement |
| :--- | :--- |
| **F-6** | After logging in, the app displays a greeting asking how the app can help, accompanied by a small note that answers are based on the "Holy Scripture". |
| **F-7** | Users can type a free-form question in the text box and send it. |
| **F-8** | Users can ask questions multiple times in one session; each question and answer is displayed sequentially in a conversational view. |
| **F-9** | The system classifies each question as relevant (spiritual/emotional) or irrelevant before generating an answer. |

### 6.3 Answer Content Rules
| ID | Requirement |
| :--- | :--- |
| **F-10** | If a question is unrelated to spiritual/emotional issues, the app responds with a standard apology and does not answer the question content. |
| **F-11** | Every relevant answer has a minimum length of 25 words and a maximum of 250 words. |
| **F-12** | Answers only use the terms "Allah" and "Isa Al-Masih" — the terms "Tuhan" and "Yesus" are not used. |
| **F-13** | If relevant, the answer may include a brief reference from the Quran at the beginning, but the vast majority of quotes come from the Bible. |
| **F-14** | Every answer includes 1–2 links to related articles from the five source websites for further reference. |
| **F-15** | All answer content must only come from/be based on the content of the five approved source websites — no information outside these sources. |
| **F-16** | Within one hour, a single user may only send 30 messages. |

### 6.4 "Like" Interaction
| ID | Requirement |
| :--- | :--- |
| **F-17** | Every answer (not a refusal) displays a "Like" button that the user can press to mark the answer as helpful. |
| **F-18** | The number of "Likes" per answer/topic is saved and can be viewed by the admin. |

### 6.5 Admin Panel
| ID | Requirement |
| :--- | :--- |
| **F-19** | The admin panel can only be accessed through separate authentication from regular user accounts. |
| **F-20** | Admins can view the list of all questions asked by users, including time, topic, and the number of "Likes". |
| **F-21** | Admins can view questions grouped by topic, along with the number of questions per topic. |
| **F-22** | Admins can view the frequency of questions with similar meanings (how many times a similar question is asked). |
| **F-23** | Admins can add or modify answer text for specific topics, with automatic validation that the answer remains within the 25–250 word range. |

### 6.6 Content Sources
All answers must be traceable to one of the following five websites:
* isadanislam.org
* isadanalquran.com
* isadanalfatihah.com
* isaislamdankaumwanita.com
* takutneraka.com

## 7. Non-Functional Requirements

### 7.1 Platform & Distribution
* Responsive web app that can be: (a) embedded as a widget/iframe on WordPress pages, and (b) wrapped as an Android app to be published on the Google Play Store.
* The interface must be optimal on mobile screens (mobile-first), considering the majority of users will likely access it via mobile devices.

### 7.2 Language & Localization
* The entire interface, answers, and system communication use Indonesian.

### 7.3 Performance
* Answers to user questions should ideally be received in under 5 seconds under normal network conditions.

### 7.4 Security & Data Privacy
* Mobile numbers collected via SMS/WhatsApp login are stored securely and only used for authentication and user session recognition.
* Guest users do not generate any personally identifiable data.
* The admin panel must be protected by proper authentication (not static passwords) prior to production launch, enforced at the database level as well (not just on the interface).

### 7.5 Scalability
* The data architecture (questions, answers, users) must support many concurrent users and the growth of question volume over time without requiring major overhauls.

## 8. Architecture & Technology Stack (Summary)
The frontend is built with React so that a single codebase can be served as a WordPress widget or wrapped as an Android app (e.g., via Capacitor). Authentication uses Firebase Authentication for SMS number verification, combined with a separate OTP provider (e.g., Twilio Verify) for the WhatsApp channel, because Firebase natively only supports OTP via SMS. Question, answer, and user interaction data are stored in Firestore. The answer engine uses a Retrieval-Augmented Generation (RAG) approach: user questions are semantically matched against a library of articles from the five source websites, then the most relevant content snippets are sent to a language model (e.g., Claude API) along with system instructions enforcing all rules in Section 6.3.

## 9. Main User Flows

### 9.1 New User Asks a Question
1. User opens the app and sees the welcome screen.
2. User selects one: log in with SMS, log in with WhatsApp, or continue as Guest.
3. If selecting SMS/WhatsApp, the user enters a mobile number, receives a verification code, and enters it to complete login.
4. User arrives at the chat screen and sees a greeting and source note for answers.
5. User types a question and presses send.
6. The system classifies the question; if relevant, the system generates an answer according to content rules and displays it along with article links; if irrelevant, the system displays a refusal message.
7. User can press "Like" on a helpful answer and can ask follow-up questions at any time.

### 9.2 Admin Reviews & Updates Content
1. Admin logs into the admin panel via separate authentication.
2. Admin reviews the list of recent questions, topic groupings, and similar question frequencies.
3. Admin identifies frequently asked topics whose answers need enrichment.
4. Admin updates or adds answers for those topics, ensuring compliance with length and terminology rules.

## 10. Data Model (Summary)

| Entity | Main Attributes |
| :--- | :--- |
| **User** | ID, mobile number (optional), login method (SMS/WhatsApp/Guest), time created |
| **Question** | ID, question text, topic, user ID, answer text, reference articles, number of "Likes", rejected status (yes/no), time created |
| **Answer (per topic)** | Topic, answer text, last updater, time updated |
| **Article** | ID, source site, title, URL, summary/full text, list of related topics |

## 11. Success Metrics (KPIs)

| Metric | Initial Target |
| :--- | :--- |
| Percentage of successfully answered questions (not rejected) | Monitored from start, used as baseline |
| Ratio of "Likes" to total answers provided | Increasing over time |
| Average number of questions per session (engagement indicator) | Between 1-50 questions per session |
| Answer compliance to length rules (25–250 words) | 100% |
| Average time to generate an answer | Under 5 seconds |
| Number of weekly active users | Determined after launch |

## 12. Assumptions & Dependencies
* The five source websites will remain available and accessible for periodic content crawling.
* The team has or will create a Firebase account, WhatsApp OTP provider account (e.g., Twilio), and Google Play Developer account prior to production launch.
* Final answer content will be reviewed by the internal editorial/theological team before broad publication to ensure accuracy and tone appropriateness.
* The chosen language model (LLM) for production supports Indonesian well and can be constrained to only answer from the provided sources.

## 13. Risks & Mitigations

| Risk | Mitigation |
| :--- | :--- |
| System-generated answers are theologically inaccurate or deviate from the source sites' tone | Apply strict system instructions to the LLM, include periodic manual reviews by the editorial team, and provide an admin mechanism to correct answers per topic |
| Ambiguity in classifying questions as relevant/irrelevant | Use LLM-based classification (not just keywords) and collect edge case examples from real question data for continuous refinement |
| Google Play content policies regarding religious/proselytizing content | Carefully review the Google Play Developer Program policies prior to submission, and prepare a clear app description regarding its purpose and audience |
| Abuse of the question field (spam, abusive language) | Add automated moderation/detection layers in the next phase, as well as admin ability to flag/delete problematic entries |
| Dependency on third-party APIs (OTP, LLM) that may cease to function or change pricing | Choose providers with clear SLAs, monitor usage costs regularly, and design an abstraction layer so providers can be swapped without rewriting the application |

## 14. Phased Release Plan
* **Phase 1 — Prototype & Validation (Completed)**
  Functional prototype with a keyword-based answer engine, initial library of 68 articles from the five sites, and complete UI flow (onboarding, chat, admin) for user experience testing.
* **Phase 2 — Production Infrastructure**
  Migrate data storage from local to Firestore, integrate Firebase Authentication (SMS) and WhatsApp OTP provider, and strengthen admin authentication.
* **Phase 3 — Production Answer Engine (RAG)**
  Comprehensive crawling of the five source sites, creation of a vector database, and integration of the production LLM with system instructions enforcing all content rules.
* **Phase 4 — Launch**
  Publish the widget on WordPress, submit the application to the Google Play Store, and monitor post-launch success metrics.

## Appendix A: Supported Topics List
* Love of Allah
* Path of Salvation
* Fear of Hell
* Peace of Mind
* Sin & Forgiveness
* Grief & Loss
* Anxiety & Depression
* Marriage & Family
* Identity of Isa Al-Masih
* Death of Isa Al-Masih
* Authenticity of the Holy Scripture
* Worship & Fasting
* Search for Truth
