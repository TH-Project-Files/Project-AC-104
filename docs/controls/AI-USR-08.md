# AI-USR-08: Mandate Phishing-Resistant MFA (FIDO2/WebAuthn) to neutralize credential harvesting

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: User Facing Controls  
**Implementation Group:** IG 1  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `6.3, 6.4, 6.5` | NIST CSF: `PR.AA, PR.IR`

---

## Control Details
Detailed Description:
Phishing-resistant MFA (FIDO2/WebAuthn) uses public-key cryptography to ensure that authentication is tied to a specific, legitimate domain, making it immune to credential harvesting and man-in-the-middle attacks. Unlike traditional MFA that relies on shared secrets like OTPs or push notifications, the private key never leaves the user's device, and the protocol verifies the origin of the login request to prevent interception.

Why AI Compounds Risk:
AI exacerbates these risks by allowing attackers to create highly convincing, personalized phishing content and fake login pages at scale, which can easily trick users into providing traditional MFA codes or approving malicious push requests.

Examples:
1. Deploy hardware security keys to employees to provide the highest level of assurance through physical, device-bound authentication.
2. Enable platform-based biometrics, such as OS-native facial or fingerprint recognition, to allow users to authenticate securely using their device's built-in hardware.
3. Implement Conditional Access policies in identity providers like an enterprise identity provider to strictly require phishing-resistant authentication strengths for accessing sensitive corporate resources and administrative roles.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
