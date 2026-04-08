# AI-END-02: Automate Macro and Script Disablement for non-admin users

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 6: Endpoint Presentation  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `4.1` | NIST CSF: `PR.PS`

---

## Control Details
Detailed Description:
Automating macro and script disablement for non-admin users involves using centralized management tools to enforce security policies that prevent unauthorized or malicious code from executing. This recommendation focuses on removing the decision-making process from the end user by programmatically blocking macros—particularly those from the internet—and restricting script execution to only those that are digitally signed or located in verified trusted folders.

Why AI Compounds Risk:
AI exacerbates this risk through automated prompt injection where malicious instructions are hidden within document macros to manipulate AI models. These "Trojan horse" documents can trick AI-powered systems into leaking sensitive data, bypassing security filters, or misclassifying malware as safe. Furthermore, AI can generate highly professional, functional code that contains subtle, hard-to-detect security flaws, leading developers to trust and execute potentially dangerous scripts.

Examples:
1. Use Group Policy Objects (GPO) in Active Directory to enable the "Block macros from running in Office files from the Internet" setting across all non-admin workstations.
2. Configure the productivity suite's security settings via administrative templates to set the default macro behavior to "Disable all macros except digitally signed macros," ensuring only verified code can run.
3. Implement PowerShell Execution Policies through centralized management to restrict script execution to "AllSigned," which requires all scripts to be signed by a trusted publisher before they can be executed by a user.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
