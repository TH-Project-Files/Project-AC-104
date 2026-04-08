# AI-NET-05: Run Continuous Attack Surface Management (ASM) scans

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 3: Network  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `12.1` | NIST CSF: `PR.NW`

---

## Control Details
Detailed Description:
Run Continuous Attack Surface Management (ASM) scans: This recommendation involves the constant, automated discovery and monitoring of an organization’s digital footprint to identify potential entry points for attackers. Unlike periodic assessments, ASM provides real-time visibility into all internal and external assets, including cloud services, shadow IT, and third-party integrations, allowing security teams to analyze, prioritize, and remediate vulnerabilities before they are exploited.

Why AI Compounds Risk:
AI exacerbation of risk: AI expands the attack surface by introducing new components like training data, models, and APIs that can be targeted via techniques such as prompt injection, data poisoning, and model inversion. Furthermore, AI enables "shadow AI," where employees deploy unauthorized AI tools without security oversight, and allows attackers to automate the discovery of vulnerabilities at a much higher scale and speed.

Examples:
1. Automated Discovery of Shadow IT and AI: Implement a solution that continuously scans the corporate network and cloud environments to identify undocumented assets and unauthorized AI applications, bringing them under official security governance.
2. Risk-Based Prioritization: Use ASM tools to assign risk scores to discovered vulnerabilities based on asset criticality and real-world threat intelligence, ensuring IT teams focus on the most severe exposures first.
3. Integration with Security Workflows: Feed ASM data into Security Orchestration, Automation, and Response (SOAR) platforms to automatically trigger remediation actions, such as isolating a misconfigured cloud bucket or generating high-priority tickets for patching.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
