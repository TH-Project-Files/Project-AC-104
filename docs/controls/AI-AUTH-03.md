# AI-AUTH-03: Enable immediate multi-channel out-of-band notifications for all critical account changes (e.g., password reset, MFA device addition).

**Category:** Identity & Access (Layer 5: Access Session)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 5.3  
**NIST CSF Subcategories:** PR.AA, DE.CM

---

## Details
Detailed Description:
Ensure that any sensitive changes to an account's security posture (such as adding a new MFA device, changing a password, or altering recovery methods) trigger an immediate, read-only alert sent to a secure, out-of-band channel (e.g., a push notification to an existing registered device or an email to a separate, confirmed address). Deliver these alerts to multiple, pre-registered out-of-band channels (e.g., push plus a secondary email or SMS) so that an attacker who controls one channel cannot suppress them all, and remove the ability for end-users to disable security alerts through self-service settings.

Why AI Compounds Risk:
AI-driven bots and automated scripts can execute account takeover (ATO) sequences—such as adding a rogue MFA device or swapping out recovery emails—within milliseconds of gaining initial access. Because these attacks occur at machine speed, immediate out-of-band notifications serve as a crucial human-in-the-loop tripwire, allowing the legitimate user or security team to detect and freeze the compromised account before the attacker establishes persistence.

Examples:
1. Configure your Identity Provider (IdP) to send mandatory push alerts (not suppressible through self-service settings) to a user's previously enrolled authenticator app whenever a new authentication method is added.
2. Implement automated "one-click" account-locking workflows within the notification (e.g., a "This wasn't me, lock my account" button) so users can instantly halt the attack.
3. Remove the ability for end-users to disable security alerts for their accounts within self-service portals.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
