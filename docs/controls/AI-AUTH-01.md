# AI-AUTH-01: Require possession factor before password factor in sign-on to limit brute force password compromise.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 1  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `6.3, 6.4` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Enabling this feature requires users to verify their identity with a possession factor (e.g., hardware token, authenticator app) before any knowledge factor (i.e., Password, Security Question) during the sign-on process.

Why AI Compounds Risk:
AI accelerates credential stuffing and brute-force attacks by rapidly generating and testing vast volumes of passwords and security question answers. Traditional password-first flows allow these automated AI tools to validate credentials at scale before hitting MFA barriers.

Examples:
1. Configure your Identity Provider (IdP) to prompt for a FIDO2 hardware key or a push notification to a registered device as the initial authentication step.
2. Implement passwordless authentication flows where the possession factor (device + biometric/PIN) entirely replaces the initial password prompt.
3. Establish policies in Conditional Access to block legacy authentication protocols that do not support possession-first workflows.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
