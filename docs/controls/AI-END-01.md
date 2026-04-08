# AI-END-01: Harden Script Execution: Restrict script execution (PowerShell/Python/JS) to only digitally signed scripts and enforce allowlists for trusted script paths to block AI-generated droppers.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 6: Endpoint Presentation  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `7.1` | NIST CSF: `PR.PS`

---

## Control Details
Detailed Description:
Hardening script execution involves configuring the operating system to only run scripts that have been digitally signed by a trusted authority and limiting execution to specific, pre-approved file paths. This prevents unauthorized or malicious code from running even if it is successfully delivered to an endpoint.

Why AI Compounds Risk:
AI exacerbates this risk by enabling attackers to rapidly generate unique, sophisticated malware droppers and obfuscated scripts that can bypass traditional signature-based antivirus or heuristic detections. Because AI can create endless variations of scripts, relying on reactive detection is insufficient; proactive execution control is required to block these untrusted, AI-generated payloads.

Examples:
1. Configure PowerShell execution policies to AllSigned via Group Policy Objects (GPO) to ensure only scripts signed by the corporate Certificate Authority or trusted vendors can run.
2. Implement application control solutions to enforce an allowlist that restricts script execution to specific, read-only directories like C:\\Program Files\\ where users cannot save AI-generated files.
3. Utilize an endpoint management tool to deploy and manage code-signing certificates to all internal developers, ensuring that custom administrative or automation scripts are signed before deployment to production environments.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
