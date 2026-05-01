# AI-LLM-08

**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 16.1  
**NIST CSF Subcategories:** PR.DS  

## Recommendation Description
Require a human to review and approve any important or risky actions taken by AI.

## Details
Detailed Description:
Establish an oversight framework where automated systems cannot execute high-stakes decisions independently. Because human-in-the-loop oversight often degrades into "human-on-the-side" at production scale, manual review must be reserved for the absolute highest-stakes actions, while automated guardrails handle the bulk of policy enforcement.

Why AI Compounds Risk:
AI can process data and execute actions at a scale and speed that outpaces manual oversight. However, forcing humans to review every action leads to 93% blind approval rates. If the organization relies on fatigued humans to catch subtle algorithmic errors or prompt injections, the security model will fail.

Examples:
1. Require a senior manager to electronically sign off only on anomalous AI-generated financial transactions exceeding a specific monetary threshold, rather than reviewing every transaction.
2. Replace repetitive per-action approvals with continuous automated policy enforcement at the Harness and Environment layers.
3. Treat human review as an exception-handling or incident response mechanism rather than a primary preventative control.

## Implementation Status
- **Policy Defined:** 0
- **Control Implemented:** 0
- **Control Automated:** 0
- **Control Reported:** 0

**Assigned To:**   
**Notes/Evidence:**   
