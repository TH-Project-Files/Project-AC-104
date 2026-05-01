# AI-LLM-15

**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 16.1  
**NIST CSF Subcategories:** PR.DS  

## Recommendation Description
Protect the specialized databases that feed knowledge to your AI (Vector Stores) with encryption and strict access rules.

## Details
Detailed Description:
Protect vector databases, which store the mathematical representations of sensitive corporate data, using encryption at rest and strict access rules (RBAC). Furthermore, address "persistent memory poisoning" by ensuring that data retrieved from an agent's memory is always treated as untrusted upon ingestion, regardless of the database's encryption status.

Why AI Compounds Risk:
While encryption protects against external theft, it does not prevent "persistent memory poisoning," where an agent writes corrupted data to its own memory and blindly trusts it upon retrieval days later. Because the poisoned data comes from the agent's own records (inside the trust boundary), the agent acts on it without hesitation.

Examples:
1. Treat all data retrieved from an agent's own vector store or scratchpad as untrusted user input, enforcing strict boundary markers during prompt assembly to prevent persistent memory poisoning from executing inside the trust boundary.
2. Deploy vector databases within a Private Virtual Cloud (VPC) and use fine-grained RBAC to restrict access so that only the specific AI application's service account can execute queries.
3. Enable comprehensive audit logging to track every similarity search query, setting alerts for anomalous patterns that might indicate a systematic attempt to exfiltrate or poison the database content.

## Implementation Status
- **Policy Defined:** 0
- **Control Implemented:** 0
- **Control Automated:** 0
- **Control Reported:** 0

**Assigned To:**   
**Notes/Evidence:**   
