# AI-ACC-08: Enforce managed-device and continuous device posture checks as a prerequisite for accessing sensitive applications and enterprise AI tools.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 2  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `1.2, 11.4` | NIST CSF: `PR.AC, DE.CM`

---

## Control Details
Detailed Description:
Mandate that access to sensitive enterprise applications, AI Gateways, and corporate AI instances (e.g., enterprise LLM workspaces) is restricted exclusively to managed devices that pass continuous health and posture checks.

Why AI Compounds Risk:
AI vastly accelerates the scale and sophistication of Adversary-in-the-Middle (AiTM) phishing attacks, which are designed to steal live session tokens immediately after a user passes MFA. Often, attackers will replay these stolen session cookies from an IP address in the exact same region as the victim to evade traditional geographic conditional access rules. However, they almost always replay the token from an unmanaged, unrecognized machine (e.g., a rogue server or personal laptop). Enforcing strict device posture ensures that even if a valid session token is stolen, it is fundamentally useless outside of the organization's tightly controlled, attested hardware fleet, effectively closing the token replay and unmanaged browser gaps.

Examples:
1. Integrate Identity Provider (IdP) Conditional Access policies with Mobile Device Management (MDM) telemetry to automatically block application access from unmanaged or BYOD devices.
2. Require a healthy EDR signal (e.g., no active malware detected, firewall enabled, OS fully patched) as a continuous prerequisite for accessing internal AI agent workspaces and high-value data repositories.
3. Utilize enterprise browsers or Secure Web Gateways (SWG) to enforce device attestation certificates before allowing data uploads or deep interactions with sanctioned external AI models.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
