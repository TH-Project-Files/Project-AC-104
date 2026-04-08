# AI-END-03: Enforce Automated Patch Management for OS and 3rd-party apps

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 6: Endpoint Presentation  
**Implementation Group:** IG 1  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `7.1` | NIST CSF: `PR.PS`

---

## Control Details
Detailed Description:
Automated patch management is the process of using software to automatically identify, download, test, and deploy updates for operating systems and third-party applications. This lifecycle includes scanning endpoints for missing patches, prioritizing them based on severity, and verifying successful installation to ensure systems remain secure and stable without requiring constant manual intervention from IT teams.

Why AI Compounds Risk:
AI exacerbates cybersecurity risks by enabling attackers to rapidly discover vulnerabilities and automate the creation of sophisticated exploits in as little as an hour after a CVE is released. This drastically shrinks the window of opportunity for defenders, making traditional monthly manual patching cycles insufficient against AI-driven threats that can target multiple systems simultaneously and bypass standard defenses.

Examples:
1. Implement a ring-based deployment strategy where patches are first automatically rolled out to a small pilot group of non-critical systems for 24-48 hours of monitoring before proceeding to the broader production environment.
2. Define granular, policy-driven workflows that automatically approve and schedule critical security updates for high-risk third-party applications like web browsers and document readers during pre-defined maintenance windows.
3. Integrate automated reporting and compliance dashboards that provide real-time visibility into patch status across the entire enterprise, allowing IT teams to quickly identify and remediate any failed installations or unpatched endpoints.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
