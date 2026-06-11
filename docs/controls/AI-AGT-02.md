# AI-AGT-02: Enforce Zero-Trust segmentation and strict Role-Based Access Control (RBAC) boundaries for agent-to-agent communications.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 6.8, 12.5, 13.4  
**NIST CSF Subcategories:** PR.AA, PR.IR  

## Details
Detailed Description:
In multi-agent architectures, implement network-layer and application-layer boundaries to prevent low-privilege agents from delegating tasks to, or improperly prompting, high-privilege peers. Agent-to-agent interactions must pass the invoking user's identity and privilege context across the entire agent chain to prevent unauthorized privilege escalation.

Why AI Compounds Risk:
Multi-agent workflows allow specialized AI agents to collaborate autonomously. However, if a public-facing, low-privilege agent (e.g., an external support bot) can freely communicate with an internal, high-privilege agent (e.g., a database administrator bot), an attacker can use indirect prompt injection on the support bot to trick the admin bot into exfiltrating or destroying data—a modern "confused deputy" attack.

Examples:
1. Filter traffic between AI agent network segments to strictly govern task delegation and state sharing.
2. Map specific agent RBAC roles to authorized network boundaries, ensuring peer-to-peer communication requires explicit authorization.
3. Require downstream high-privilege agents to re-validate the original user context (e.g., via delegated OAuth tokens) before executing tasks requested by a peer agent.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
