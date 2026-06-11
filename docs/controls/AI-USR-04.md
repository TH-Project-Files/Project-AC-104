# AI-USR-04: Implement Executive Challenge-Response Protocols (e.g., pre-established safe words) for urgent voice/video requests.

**Category:** Governance & People (Layer 0: User Facing Controls)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 14.1, 17.1  
**NIST CSF Subcategories:** PR.AT, RS.MA  
**Layered with:** Deepfake defense chain — AI-GOV-09 owns the governing protocol; this control owns the challenge-response, safe-word, and liveness mechanics referenced by the chain; AI-USR-05 trains staff to apply them.

---

## Details
Detailed Description:
Executive challenge-response protocols are manual authentication methods where an individual verifies the identity of a caller or video participant by issuing a specific challenge that requires a pre-agreed, secret response, such as a safe word or a unique piece of personal information known only to the involved parties.

Why AI Compounds Risk:
AI significantly exacerbates impersonation risks through deepfake technology, which allows attackers to convincingly clone an executive's voice or likeness in real-time, making traditional visual and auditory cues unreliable for verifying identity during urgent or sensitive requests.

Examples:
1. Establish a rotating system of weekly or daily "code phrases" shared through secure, out-of-band channels that executives must use to authorize high-value financial transactions or sensitive data transfers.
2. Implement "liveness challenges" during video calls where employees ask the executive to perform unpredictable physical actions, such as turning their head fully to the side or waving a hand in front of their face, to disrupt AI-generated overlays.
3. Create a formal "Human Firewall" policy that mandates an out-of-band callback to a pre-validated secondary phone number whenever an executive makes an unusual or high-pressure request via voice or video.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
