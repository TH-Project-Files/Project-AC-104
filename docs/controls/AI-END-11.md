# AI-END-11

**Category:** Layer 6: Endpoint Presentation  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 1.2, 3.6, 4.5  
**NIST CSF Subcategories:** PR.DS, DE.CM  

## Recommendation Description
Govern and restrict Endpoint-Hosted AI Runtimes (e.g., local LLMs) to prevent local data leakage and unauthorized API binding.

## Details
Detailed Description:
Use MDM and EDR to inventory and govern locally installed AI models and frameworks. Enforce local disk encryption for all cached prompts and vector embeddings stored by these tools. Implement host-based firewalls to prevent local AI runners from binding their API services to open network ports, which could expose the local model to other devices on the network.

Why AI Compounds Risk:
As "local LLM" frameworks (e.g., Ollama, LM Studio) become more popular, developers are downloading unvetted model weights and running them directly on their endpoints. These local setups bypass corporate AI Gateways and DLP controls. Furthermore, they often cache highly sensitive corporate prompts in plain text on the local disk and occasionally bind insecure API servers to public network interfaces (e.g., 0.0.0.0), exposing the endpoint to exploitation.

Examples:
1. Configure host-based firewalls to restrict local AI frameworks from binding services to external network interfaces, restricting them strictly to localhost (127.0.0.1).
2. Enforce endpoint disk encryption (e.g., BitLocker, FileVault) to protect local model artifacts, cached prompt logs, and local vector embeddings from unauthorized physical access.
3. Use application allowlisting to prohibit the execution of unapproved local model runners and track all authorized endpoint-hosted AI deployments in the centralized asset inventory.

## Implementation Status
- **Policy Defined:** 0
- **Control Implemented:** 0
- **Control Automated:** 0
- **Control Reported:** 0

**Assigned To:**   
**Notes/Evidence:**   
