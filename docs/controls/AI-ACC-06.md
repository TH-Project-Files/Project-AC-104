# AI-ACC-06: Implement Context-Aware Authentication (e.g. location, device posture, time-of-access)

**Category:** Identity & Access (Layer 5: Access Session)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 6.1, 6.8  
**NIST CSF Subcategories:** PR.AA  
**Layered with:** AI-ACC-05 (event-driven revocation of active sessions — consumes this control's risk signals), AI-ACC-08 (device posture as a contextual input), AI-GOV-15 (UEBA — same behavioral-baselining family applied to user/entity activity)

---

## Details
Detailed Description:
Context-aware authentication is a security method that evaluates real-time situational factors—such as user location, device health, time of access, and network context—to determine the legitimacy of a login attempt. Unlike traditional static credentials, it uses a risk-based engine to dynamically grant seamless access for low-risk behavior or require additional verification (step-up authentication) when anomalies are detected.

Scope note: This control owns risk evaluation at the authentication decision point (allow / step-up / deny before a session is issued). Revocation of already-active sessions on high-risk events is owned by AI-ACC-05.

Why AI Compounds Risk:
AI exacerbates authentication risks by enabling cybercriminals to launch sophisticated, automated attacks at scale, such as using generative AI to create realistic deepfakes for social engineering or utilizing machine learning to bypass traditional bot detection and execute high-speed credential stuffing.

Examples:
1. To implement this in a corporate environment, start by defining granular access policies that require multi-factor authentication (MFA) or block access entirely when employees attempt to reach sensitive financial systems from unrecognized geographic locations or unmanaged personal devices.
2. Integrate a risk-analysis engine that uses machine learning to establish a behavioral baseline for each employee, such as their typical working hours and network types, so the system can automatically flag and challenge "impossible travel" scenarios or logins occurring at highly unusual times.
3. Require step-up authentication with a phishing-resistant factor (e.g., FIDO2) whenever the contextual risk score crosses a defined threshold—for example, a first-time device combined with an off-hours login—before any session is issued. (Continuous monitoring and revocation of the session once issued is handled by AI-ACC-05.)

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
