# AI-LLM-24: Enforce cryptographic integrity and freshness checks on all agent-to-agent and agent-to-tool communications.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 16.14, 3.3  
**NIST CSF Subcategories:** PR.DS  

## Details
Detailed Description:
Implement message validation by default across the agentic architecture. Message payloads passed between agents or from an agent to a tool execution engine must include cryptographic signatures (to verify origin and integrity) and timestamps or nonces (to verify freshness).

Why AI Compounds Risk:
As multi-agent systems communicate autonomously at high speeds, the blast radius of a single compromised agent increases. Without payload integrity and freshness checks, a malicious or prompt-injected agent can spoof messages, alter instruction payloads in transit, or replay previously authorized tool commands to laterally infect other agents or bypass access controls.

Examples:
1. Utilize JSON Web Tokens (JWT) or signed HTTP requests for all internal remote procedure calls (RPC) between independent AI agents to ensure cryptographic origin verification.
2. Embed strict timestamps and cryptographic nonces within the message payload schema; the receiving agent must reject any message that falls outside a tight temporal window (e.g., older than 5 seconds) to prevent replay attacks.
3. Enforce mutual TLS (mTLS) combined with payload hashing across the agentic service mesh to protect the confidentiality and integrity of agent communications.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
