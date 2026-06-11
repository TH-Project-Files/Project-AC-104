# AI-USR-06: Train staff on Reverse-Turing Tests to detect AI bots in chat/email

**Category:** Governance & People (Layer 0: User Facing Controls)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 14.1, 14.2  
**NIST CSF Subcategories:** PR.AT

---

## Details
Detailed Description:
Training staff on Reverse-Turing Tests involves teaching employees how to intentionally mimic machine-like behavior or use specific interrogation techniques to provoke a non-human response from a chat or email participant. Because modern LLMs handle humor, idiom, and contextual nuance convincingly, the training emphasizes procedural verification—moving the interaction to an authenticated, out-of-band channel (see AI-USR-04)—over conversational 'gotcha' tests, while teaching the behavioral red flags that persist regardless of conversational fluency.

Why AI Compounds Risk:
AI exacerbates this risk by enabling the creation of highly sophisticated, evasive bots that can convincingly mimic human conversation, syntax, and tone at an industrial scale. Generative AI lowers the barrier for attackers to launch personalized phishing or social engineering attacks that are increasingly difficult for traditional security filters or untrained humans to detect.

Examples:
1. Train staff that the reliable test is procedural, not conversational: a legitimate correspondent can always move to an authenticated channel (a known phone number, or a video call with the liveness checks defined in AI-USR-04), while bots and impersonators will resist or deflect out-of-band verification.
2. Educate staff on behavioral red flags that persist even in fluent AI conversation: manufactured urgency, refusal to use established channels, requests that bypass normal process, and inconsistency about shared history or recent in-person interactions.
3. Run periodic simulations where employees interact with current-generation LLM bots to demonstrate that fluency, humor, and cultural context are no longer reliable discriminators—reinforcing that out-of-band verification, not conversational testing, is the dependable control.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
