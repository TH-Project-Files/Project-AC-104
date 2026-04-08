# AI-AGT-01: Implement Agent tool-call governance through strict allowlists, schema validation, and human-in-the-loop approvals.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Application  
**Implementation Group:** IG 2  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `16.2, 16.4` | NIST CSF: `PR.AC, PR.PT`

---

## Control Details
Detailed Description:
Implement robust governance over autonomous AI agent tool-calling capabilities. This includes enforcing strict allowlists for accessible tools, real-time input/output schema validation, and explicitly defining "Human-in-the-Loop" (HITL) approval gates for high-risk actions.

High-ROI HITL Triggers:
To prevent silent data exfiltration or destructive actions, HITL cryptographic approvals must be triggered for:
- External Transmission: Any agent action that sends content to an external email/domain, external Slack/Teams tenant, webhook, or public URL.
- Export / Bulk Retrieval: Requests exceeding normal limits (e.g., retrieving >100 rows or chunks in a single session).
- Restricted Label Access: Any retrieval/summarization that touches data explicitly labeled as Restricted, Regulated, Legal, HR, Finance, or Security.
- Cross-Boundary Sharing: Attempting to share content across isolated departments (e.g., summarizing HR data and sending it to a non-HR channel).
- Privilege Boundary Crossing: An agent attempting to invoke an admin-only tool, elevated API, or privileged connector (even if read-only).
- Anomalous Tool Sequencing: A tool-call chain that hasn't been approved or seen before (e.g., "RAG -> DB query -> File download -> Email send").

Why AI Compounds Risk:
AI agents can autonomously invoke APIs, query databases, and execute code based on natural language instructions. If an agent is compromised via prompt injection, an attacker can hijack these tool-calling privileges to extract data, pivot internally, or execute unauthorized transactions. Unfettered tool access effectively turns an LLM into an unauthenticated Remote Code Execution (RCE) vector. 

Examples:
1. Restrict an AI agent's accessible tools to a tightly scoped allowlist (e.g., granting read-only DB access) rather than giving it broad, unfettered access to all enterprise APIs.
2. Implement strict, server-side JSON schema validation for all tool inputs to prevent an attacker from passing malicious payloads or SQL injections via a hijacked agent.
3. Require cryptographic "human-in-the-loop" MFA approvals before an agent can execute destructive actions or trigger any of the defined High-ROI events.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
