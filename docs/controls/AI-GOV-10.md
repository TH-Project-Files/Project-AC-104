# AI-GOV-10: Require AI Vendor Risk Assessments for all new software purchases

**Category:** Governance & People (Layer 0: Governance & System Controls)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 15.1, 17.1  
**NIST CSF Subcategories:** GV.PO, GV.OV

---

## Details
Detailed Description:
This recommendation mandates that any new software procurement must undergo a specialized risk assessment to evaluate the artificial intelligence components, focusing on model-specific risks like training data provenance, algorithmic bias, and output reliability that standard security reviews might overlook.

Why AI Compounds Risk:
AI exacerbates risk because systems are dynamic and can experience model drift or change behavior over time, process massive amounts of sensitive data that may be repurposed for training, and often lack transparency in how they reach specific decisions or handle data isolation.

Examples:
1. Tier vendors based on AI criticality so that high-risk tools, such as those handling customer PII, receive deeper technical scrutiny than low-risk internal summarization tools.
2. Require vendors to provide model cards or system cards that document the model's capabilities, limitations, and intended use cases to ensure alignment with corporate ethical and security standards.
3. Update the Third-Party Risk Management (TPRM) program to include specific questionnaire items regarding whether company data will be used to train the vendor's global models and if there are options for users to opt out of AI features.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
