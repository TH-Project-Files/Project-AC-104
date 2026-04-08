# AI-USR-09: Implement Out-of-Band/Verbal Verification for high-risk financial/data actions

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: User Facing Controls  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `6.3, 6.4, 6.5` | NIST CSF: `PR.AA, PR.IR`

---

## Control Details
Detailed Description:
Out-of-band verification is a security process that requires two separate and independent communication channels to validate a user's identity or a specific high-risk request. By moving the verification away from the primary channel (like an email or web portal) to a secondary one (like a known phone number or a dedicated app), organizations ensure that an attacker must compromise two unconnected systems simultaneously to succeed.

Why AI Compounds Risk:
AI exacerbates this risk by enabling sophisticated social engineering through high-quality deepfake audio and video that can impersonate executives or colleagues with near-perfect accuracy. Generative AI also allows attackers to create hyper-personalized, convincing phishing emails at scale, increasing the likelihood that employees will trust fraudulent instructions if they rely on a single communication channel.

Examples:
1. Require a secondary verbal confirmation via a known, pre-verified phone number for any wire transfer or change to vendor payment details initiated via email.
2. Implement automated push notifications through a secure mobile authentication app that requires biometric approval (like facial or fingerprint recognition) for any high-risk data access or administrative account changes.
3. Establish a dual-approval mandate where one employee initiates a sensitive financial action in the primary system and a second authorized employee must verify and approve it through a separate, out-of-band communication method.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
