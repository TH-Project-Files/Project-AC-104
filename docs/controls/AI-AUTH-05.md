# AI-AUTH-05: Monitor external threat intelligence and dark web sources for compromised employee credentials, and enforce automated password resets for exposed accounts.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `5.2, 7.1` | NIST CSF: `ID.RA, DE.CM`

---

## Control Details
Detailed Description:
Implement continuous monitoring of third-party data breaches, dark web marketplaces, and public paste sites for exposed corporate email addresses and passwords. When a compromised credential belonging to an employee is detected, the system should automatically invalidate the current session, force a mandatory password reset, and require re-enrollment or reverification of MFA.

Why AI Compounds Risk:
Adversaries use AI-driven data processing tools to rapidly ingest, normalize, and cross-reference multi-terabyte credential dumps from the dark web. Instead of manually testing passwords, AI allows attackers to instantly correlate leaked personal passwords with corporate email formats and automatically orchestrate credential stuffing attacks at scale across thousands of endpoints. If an organization does not detect and reset a leaked password faster than the AI can test it, an account compromise is almost guaranteed.

Examples:
1. Integrate Identity Protection services (like Microsoft Entra ID Protection or Okta Insights) that automatically cross-reference user passwords against known breached password databases during sign-in.
2. Subscribe to an external Threat Intelligence or Digital Risk Protection (DRP) service (e.g., Recorded Future, HaveIBeenPwned API) to alert the SOC whenever corporate domains appear in fresh credential drops.
3. Configure conditional access policies to automatically flag a user's risk level as "High" upon a credential leak discovery, immediately blocking access until a secure password reset is completed via a verified MFA prompt.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
