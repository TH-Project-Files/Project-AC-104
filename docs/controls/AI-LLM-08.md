# AI-LLM-08: Require a human to review and approve any important or risky actions taken by AI.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Explanation: This recommendation establishes a "human-in-the-loop" framework where automated systems cannot execute high-stakes decisions independently, ensuring accountability, ethical alignment, and error correction.

Why AI Compounds Risk:
Risk Exacerbation: AI can process data and execute actions at a scale and speed that outpaces manual oversight, meaning a single algorithmic error or biased model can cause widespread financial or reputational damage before detection.

Examples:
1. Require a senior manager to electronically sign off on AI-generated financial transactions or wire transfers exceeding a specific monetary threshold.
2. Mandate that HR professionals review and validate AI-shortlisted job candidates to ensure the selection process adheres to diversity and inclusion standards.
3. Implement a manual review step for AI-generated cybersecurity firewall rules before they are deployed to production environments to prevent accidental service outages.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
