# AI-LLM-23: Implement structural or cryptographic boundary markers to separate system prompts from untrusted external data within LLM contexts.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 16.1, 16.4  
**NIST CSF Subcategories:** PR.PS, DE.CM  

## Details
Detailed Description:
Applications must utilize robust boundary demarcations (e.g., strict XML tags, distinct message roles, or separate parsing pipelines) whenever an LLM ingests external or untrusted content. This prevents the LLM from confusing developer instructions with user-provided data.

Why AI Compounds Risk:
AI models inherently struggle to distinguish between system instructions and data payloads. Without structural boundaries, a malicious payload hidden in a summarized document or webpage can execute an indirect prompt injection attack, overriding the agent's core constraints and turning the AI into a confused deputy.

Examples:
1. Wrap all external document text within strict `<external_content>` tags before passing it to the LLM.
2. Implement instruction-tuned models that enforce separate API channels for 'System', 'User', and 'Data' roles.
3. Utilize an intermediate parsing LLM to strip actionable instructions from untrusted data before feeding it into the primary agentic workflow.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
