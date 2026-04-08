# AI-END-05: Remove or highly manage local admin and installation rights

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 6: Endpoint Presentation  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `10.1, 10.5` | NIST CSF: `DE.CM, PR.MA`

---

## Control Details
Detailed Description:
Removing local admin rights involves transitioning users from administrative accounts to standard user accounts to enforce the principle of least privilege. This prevents users from performing high-risk actions like installing unauthorized software, disabling security controls, or modifying critical system files, which significantly reduces the organization's attack surface.

Why AI Compounds Risk:
AI exacerbates this risk because automated attack tools and agentic AI can exploit elevated privileges to move laterally through a network, disable AI-driven endpoint protections, and execute malicious code at machine speed. If an AI agent or a compromised account has admin rights, it can weaponize the system against the organization more efficiently than a human attacker.

Examples:
1. Implement Just-In-Time access solutions that provide temporary, time-bound elevated privileges only for specific approved tasks, automatically revoking them once the task is complete.
2. Use Group Policy Objects or Mobile Device Management tools to centrally manage and "flush" local administrator groups, ensuring only authorized domain accounts have elevated access.
3. Deploy Privileged Access Management or Endpoint Privilege Management software to allow "policy-based elevation," which lets standard users run specific, pre-approved applications with administrative rights without giving the user full control over the OS.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
