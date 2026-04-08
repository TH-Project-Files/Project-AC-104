# AI-ACC-07: Enable device-bound/session-bound token protections (where supported) to reduce replay of stolen session tokens

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 3  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `6.1, 6.8` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Implement modern device-bound or session-bound token protections, where access tokens or session cookies are tightly bound to the specific trusted hardware device or endpoint that performed the initial authentication. This ensures that even if a session cookie is stolen, it cannot be easily replayed or used from a different, untrusted machine. 

*Defense-in-Depth Context:* While other controls in this framework (such as AI-GOV-04, AI-ACC-04, and AI-ACC-05) focus on detect-and-respond capabilities—monitoring for session risk and actively revoking access upon anomaly detection—this control acts as a strict preventative measure. It validates the cryptographic or hardware binding before a compromised token can ever be successfully replayed.

Why AI Compounds Risk:
AI accelerates the deployment and scale of Adversary-in-the-Middle (AiTM) phishing campaigns. These automated toolkits intercept and steal session tokens immediately after a user successfully completes an MFA prompt. Once the session cookie is stolen, automated AI bots can rapidly replay it from their own infrastructure to completely bypass MFA. Device-bound tokens neutralize this threat by ensuring the stolen token is rejected outside the victim's validated physical device.

Examples:
1. Enable identity provider (IdP) features that bind session tokens to a registered endpoint's trusted hardware module or perform continuous device health attestation.
2. Implement advanced passwordless or hardware-bound authentication flows (like FIDO2/WebAuthn) that inherently tie session continuity to the original authorized endpoint.
3. Enforce continuous access evaluation policies that instantly revoke sessions if IP address, location, or device fingerprint anomalies are detected, acting as a compensating control when strict hardware binding is not fully supported.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
