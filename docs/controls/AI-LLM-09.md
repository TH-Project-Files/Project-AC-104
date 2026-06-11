# AI-LLM-09: Enforce deny-by-default allowlists restricting AI agent egress to approved endpoints and systems.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 16.1  
**NIST CSF Subcategories:** PR.DS  
**Layered with:** AI-AGT-01 (the IG 2 operationalization — extends this control's allowlisting with schema validation and human-in-the-loop approval gates), AI-LLM-03 (least-privilege foundation), AI-LLM-01 (network filters around model infrastructure)

---

## Details
Detailed Description:
Explanation: This recommendation involves implementing a deny-by-default security posture where AI agents are restricted to interacting only with a pre-approved list of URLs, APIs, or internal databases. By defining these strict boundaries at the configuration or network level, organizations prevent agents from reaching unverified external sites or sensitive internal systems that are not required for their specific tasks. This ensures that even if an agent is compromised or receives a malicious command, its ability to exfiltrate data or access unauthorized resources is physically limited by the underlying infrastructure.

Positioning: This is the IG 1 starting point for restricting agent reach. Organizations operating at IG 2, or deploying agents with tool-calling capabilities, should implement the full tool-call governance regime in AI-AGT-01, which extends this allowlisting with server-side schema validation and human-in-the-loop approval triggers.

Why AI Compounds Risk:
Why AI Exacerbates Risk: Traditional automation follows predictable, hard-coded logic, whereas AI agents use natural language reasoning to autonomously decide which tools to use and which sites to visit. This autonomy makes them susceptible to indirect prompt injection, where an agent might read a malicious website or document containing hidden instructions that trick it into sending sensitive data to an attacker-controlled URL. Furthermore, because agents can process and move data at scale much faster than a human, an unrestricted agent could quietly leak massive amounts of proprietary information through forced URL loads or unauthorized API calls before the activity is detected.

Examples:
1. Tool-Level Scoping: Configure the agent framework to use scoped tool definitions where each tool (e.g., a web search tool or a database connector) has a hard-coded allow-list of permitted domains or tables, denying any request that falls outside those specific parameters.
2. Network Isolation and Sandboxing: Run AI agents within isolated containers or sandboxes that have egress filtering enabled at the network level, ensuring the agent can only establish connections to known corporate endpoints or verified third-party service providers.
3. Identity and Access Management (IAM): Register AI agents as distinct identities within the corporate IAM system, assigning them the minimum necessary permissions to access specific internal applications or websites only during required business hours or for specific approved use cases.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
