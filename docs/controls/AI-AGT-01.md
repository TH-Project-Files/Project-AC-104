# AI-AGT-01

**Category:** Layer 7: Application  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 16.2, 16.4  
**NIST CSF Subcategories:** PR.AC, PR.PT  

## Recommendation Description
Implement Agent tool-call governance through strict allowlists, schema validation, and human-in-the-loop approvals.

## Details
Detailed Description:
Implement robust governance over autonomous AI agent tool-calling capabilities. This includes enforcing strict allowlists for accessible tools, real-time input/output schema validation, and explicitly defining automated guardrails. Note: Production data shows Human-in-the-Loop (HITL) suffers from "consent fatigue," with users blindly approving up to 93% of prompts. Therefore, rely primarily on Harness-Layer automated constraints and use HITL strictly for high-impact anomalies.

Why AI Compounds Risk:
AI agents can autonomously invoke APIs, query databases, and execute code based on natural language instructions. If an agent is compromised, an attacker can hijack these privileges. Relying solely on per-action human approvals fails at scale, effectively turning an LLM into an unauthenticated Remote Code Execution (RCE) vector because tired users will rubber-stamp the agent's actions.

Examples:
1. Restrict an AI agent's accessible tools to a tightly scoped allowlist (e.g., granting read-only DB access) rather than giving it broad, unfettered access.
2. Enforce declarative safety contracts and automated schema validation at the Harness layer that cannot be overridden by human users suffering from consent fatigue.
3. Shift from per-action human approvals to continuous automated policy enforcement, reserving human alerts only for severe threshold breaches.

## Implementation Status
- **Policy Defined:** 0
- **Control Implemented:** 0
- **Control Automated:** 0
- **Control Reported:** 0

**Assigned To:**   
**Notes/Evidence:**   
