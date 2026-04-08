# AI-USR-10: Replace annual training with Contextual Security Nudges at the point of click

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: User Facing Controls  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `14.1, 14.2` | NIST CSF: `PR.AT`

---

## Control Details
Detailed Description:
Explanation: This recommendation replaces static, once-a-year security presentations with automated, real-time interventions delivered at the exact moment a user performs a risky action. By utilizing nudge theory, these subtle visual cues or prompts interrupt "autopilot" behavior (System 1 thinking) and encourage deliberate, safer decision-making (System 2 thinking) without blocking the user's workflow or requiring them to recall distant training.

Why AI Compounds Risk:
AI Risk Exacerbation: Generative AI increases the frequency and sophistication of cyber threats by automating the creation of highly personalized, convincing phishing messages and deepfakes at scale. Because these AI-driven attacks are harder for humans to detect through traditional means, the real-time, contextual guidance provided by nudges is necessary to intercept social engineering attempts that bypass standard security filters.

Examples:
1. Deploy just-in-time phishing banners that appear within an email client when a user clicks a link from an external sender with a mismatched domain or urgent language.
2. Integrate password-strength meters and visual indicators that provide immediate color-coded feedback as an employee creates or updates credentials for corporate SaaS applications.
3. Use interstitial warning pages or countdown timers that trigger when an employee attempts to navigate to a suspicious URL or download a file containing sensitive personally identifiable information (PII).

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
