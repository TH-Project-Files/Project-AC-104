# AI-AUTH-04: Enable user enumeration prevention for authentication and account recovery workflows to obscure account existence.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `6.2, 16.1` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Enabling user enumeration prevention ensures that authentication and recovery endpoints return generic, indistinguishable error messages regardless of whether an account actually exists. If a user doesn't exist or cannot sign in, the system provides a standard authenticator verification error rather than confirming the account's status.

Why AI Compounds Risk:
AI and automated botnets dramatically increase the speed and scale of reconnaissance. Attackers can feed massive datasets of scraped emails and credentials into AI tools to systematically probe IDP endpoints. By identifying which accounts are valid (enumeration), AI can immediately pivot to launching highly targeted, personalized spear-phishing campaigns or focused credential stuffing attacks specifically against those verified users.

Examples:
1. Configure the Identity Provider (IdP) to return a generic "Authentication failed" message for both bad usernames and bad passwords.
2. Standardize password reset messages (e.g., "If that account exists, a recovery email has been sent") rather than confirming "User not found."
3. Implement response-time normalization on authentication endpoints to prevent AI bots from using timing analysis to deduce whether an account exists based on server processing time.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
