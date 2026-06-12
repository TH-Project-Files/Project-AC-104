# AI-AGT-01: Implement Agent tool-call governance through strict allowlists, schema validation, and human-in-the-loop approvals.

**Category:** Applications & Data (Layer 7: Application)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 16.2, 16.4  
**NIST CSF Subcategories:** PR.AA, PR.PS  
**Layered with:** AI-LLM-09 (IG 1 starter allowlisting that this control extends), AI-LLM-08 (the human-in-the-loop mandate this control operationalizes for agent tool-calls), AI-LLM-03 (least privilege), AI-LLM-23 (untrusted-content boundaries for page-embedded injection), AI-END-11 (governance of the browser extension/runtime surface these agents execute on)  

## Details
Detailed Description:
Implement robust governance over autonomous AI agent tool-calling capabilities. This includes enforcing strict allowlists for accessible tools, real-time input/output schema validation, and explicitly defining "Human-in-the-Loop" (HITL) approval gates for high-risk actions. This governance applies equally to computer-use and browser-driving agents, where the "tool" is a live browser or desktop session: such agents must run in isolated browser profiles with no ambient credentials, saved sessions, or autofill data, navigate only within a domain allowlist, and treat all rendered page content as untrusted input subject to the boundary controls in AI-LLM-23.

High-ROI HITL Triggers:
To prevent silent data exfiltration or destructive actions, HITL cryptographic approvals must be triggered for:
- External Transmission: Any agent action that sends content to an external email/domain, external Slack/Teams tenant, webhook, or public URL.
- Export / Bulk Retrieval: Requests exceeding normal limits (e.g., retrieving >100 rows or chunks in a single session).
- Restricted Label Access: Any retrieval/summarization that touches data explicitly labeled as Restricted, Regulated, Legal, HR, Finance, or Security.
- Cross-Boundary Sharing: Attempting to share content across isolated departments (e.g., summarizing HR data and sending it to a non-HR channel).
- Privilege Boundary Crossing: An agent attempting to invoke an admin-only tool, elevated API, or privileged connector (even if read-only).
- Anomalous Tool Sequencing: A tool-call chain that hasn't been approved or seen before (e.g., "RAG -> DB query -> File download -> Email send").
- Credentialed Web Actions: A computer-use or browser-driving agent attempting to enter credentials, submit forms on authenticated sites, or complete payment, approval, or state-changing flows on behalf of a user.

Why AI Compounds Risk:
AI agents can autonomously invoke APIs, query databases, and execute code based on natural language instructions. If an agent is compromised via prompt injection, an attacker can hijack these tool-calling privileges to extract data, pivot internally, or execute unauthorized transactions. Unfettered tool access effectively turns an LLM into an unauthenticated Remote Code Execution (RCE) vector. 

Examples:
1. Restrict an AI agent's accessible tools to a tightly scoped allowlist (e.g., granting read-only DB access) rather than giving it broad, unfettered access to all enterprise APIs.
2. Implement strict, server-side JSON schema validation for all tool inputs to prevent an attacker from passing malicious payloads or SQL injections via a hijacked agent.
3. Require cryptographic "human-in-the-loop" MFA approvals before an agent can execute destructive actions or trigger any of the defined High-ROI events.
4. Run browser/computer-use agents in dedicated, ephemeral browser profiles containing no saved passwords, cookies, or sessions; scope navigation to an explicit domain allowlist; and require HITL approval before the agent enters credentials or submits any state-changing form, preventing page-embedded prompt injection from escalating into agent-executed account takeover or CSRF.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
