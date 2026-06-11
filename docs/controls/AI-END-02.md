# AI-END-02: Automate Macro Disablement for non-admin users

**Category:** Endpoints (Layer 6: Endpoint Presentation)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 4.1  
**NIST CSF Subcategories:** PR.PS  
**Layered with:** Execution-control chain — AI-END-01 hardens the script engines (owns PowerShell execution policy); this control disables macros and embedded document code; AI-END-09 allowlists applications. Intentional defense-in-depth, not duplication.

---

## Details
Detailed Description:
Automating macro disablement for non-admin users involves using centralized management tools to enforce security policies that prevent unauthorized or malicious embedded code from executing. This recommendation focuses on removing the decision-making process from the end user by programmatically blocking macros and other embedded document code—particularly content originating from the internet. Hardening of the script engines themselves (PowerShell/Python/JS execution policy and signing) is owned by AI-END-01.

Why AI Compounds Risk:
AI exacerbates this risk through automated prompt injection where malicious instructions are hidden within document macros to manipulate AI models. These "Trojan horse" documents can trick AI-powered systems into leaking sensitive data, bypassing security filters, or misclassifying malware as safe. Furthermore, AI can generate highly professional, functional code that contains subtle, hard-to-detect security flaws, leading developers to trust and execute potentially dangerous scripts.

Examples:
1. Use Group Policy Objects (GPO) in Active Directory to enable the "Block macros from running in Office files from the Internet" setting across all non-admin workstations.
2. Configure the productivity suite's security settings via administrative templates to set the default macro behavior to "Disable all macros except digitally signed macros," ensuring only verified code can run.
3. Enable attack surface reduction rules to block Win32 API calls from Office macros and disable legacy Excel 4.0 (XLM) macros, closing the embedded-code delivery channels that AI-generated lures most commonly exploit.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
