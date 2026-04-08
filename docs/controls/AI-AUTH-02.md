# AI-AUTH-02: Require advanced CAPTCHA on password reset requests to prevent automated abuse.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `6.5` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Implementing an advanced CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) on password reset and account recovery forms prevents malicious actors from using automated scripts to trigger mass password reset emails, brute-force reset tokens, or perform account enumeration.

Why AI Compounds Risk:
AI and machine learning models are now highly capable of solving legacy text and image-based CAPTCHAs at scale. Furthermore, AI-driven automation frameworks can be deployed to overwhelm authentication endpoints with millions of reset requests, leading to SMS/email toll fraud, denial of service (MFA fatigue), or the interception of recovery codes. Organizations must deploy AI-resistant, behavioral-based CAPTCHAs to counter these intelligent bots.

Examples:
1. Integrate enterprise-grade, behavioral CAPTCHAs (like reCAPTCHA v3 or Cloudflare Turnstile) on all password reset and account recovery portals.
2. Combine CAPTCHA enforcement with strict rate limiting (e.g., maximum 3 reset requests per IP/account per hour).
3. Implement Web Application Firewall (WAF) bot-management rules to detect and block headless browsers attempting to interact with the recovery endpoints.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
