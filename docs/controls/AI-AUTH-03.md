# AI-AUTH-03: Enable immediate, un-mutable out-of-band notifications for all critical account changes (e.g., password reset, MFA device addition).

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `5.3` | NIST CSF: `PR.AA, DE.CM`

---

## Control Details
Detailed Description:
Ensure that any sensitive changes to an account's security posture (such as adding a new MFA device, changing a password, or altering recovery methods) trigger an immediate, read-only alert sent to a secure, out-of-band channel (e.g., a push notification to an existing registered device or an email to a separate, confirmed address). These notifications must be un-mutable, meaning an attacker cannot suppress or turn them off even if they gain access to the account settings.

Why AI Compounds Risk:
AI-driven bots and automated scripts can execute account takeover (ATO) sequences—such as adding a rogue MFA device or swapping out recovery emails—within milliseconds of gaining initial access. Because these attacks occur at machine speed, immediate out-of-band notifications serve as a crucial human-in-the-loop tripwire, allowing the legitimate user or security team to detect and freeze the compromised account before the attacker establishes persistence.

Examples:
1. Configure your Identity Provider (IdP) to send mandatory, un-suppressible push alerts to a user's previously enrolled authenticator app whenever a new authentication method is added.
2. Implement automated "one-click" account-locking workflows within the notification (e.g., a "This wasn't me, lock my account" button) so users can instantly halt the attack.
3. Remove the ability for end-users to disable security alerts for their accounts within self-service portals.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
