# AI-LLM-03: Give AI agents only the bare minimum permissions needed to do their jobs.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 1  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `6.1, 6.2` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Detailed Explanation: This recommendation refers to the Principle of Least Privilege (PoLP), a security model where AI agents are granted only the absolute minimum permissions necessary to perform a specific, legitimate task. Instead of providing broad "administrative" or "superuser" access, permissions are restricted by scope, time, and function to ensure that if an agent is compromised or malfunctions, the potential damage to the system is strictly limited.

Why AI Compounds Risk:
Why AI Exacerbates the Risk: AI agents can process data, make decisions, and execute actions across multiple systems at machine speed and scale, far exceeding human capabilities. Unlike traditional software with fixed workflows, AI agents reason and adapt at runtime, meaning a single over-privileged agent with a poorly phrased prompt or a malicious injection can cause systemic, tenant-wide damage or data exfiltration before a human administrator can intervene.

Examples:
1. Corporate Implementation Examples:
2. Granular Role-Based Access: Define specific roles for agents, such as a customer support bot having permissions only to read and comment on tickets (tickets:read, tickets:comment) while being strictly barred from accessing billing or financial databases.
3. Just-in-Time (JIT) Access: Replace permanent, standing permissions with short-lived tokens that are issued only when a task begins and automatically expire after a few minutes or upon task completion.
4. Human-in-the-Loop Overrides: Implement mandatory human approval checkpoints for high-risk or destructive operations, such as transferring funds above a certain threshold, modifying security settings, or deleting production data.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
