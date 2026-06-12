# AI-LOG-01: Establish policies and controls for AI prompt/chat retention, privacy masking, legal hold, and strict access management for observability logs.

**Category:** Governance & People (Layer 4: Data)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 3.2, 8.12  
**NIST CSF Subcategories:** PR.DS, DE.CM  
**Layered with:** AI-LLM-04 (the agent audit logs this policy governs), AI-GOV-11 (the AI incident response playbook whose investigations trigger holds), AI-GOV-02 (data classification driving what gets masked)

---

## Details
Detailed Description:
Establish formal policies and technical controls for the retention, privacy masking, and access management of AI prompt logs, chat histories, and LLM tracing data.

Retention must be reconciled with legal and records-management obligations, not just minimized: define legal-hold triggers (reasonably anticipated litigation, regulatory investigation, internal misconduct inquiries, or public-records requests) that suspend automated purging for the affected custodians, agents, and systems, and document how AI log retention schedules align with the records laws applicable to the organization (e.g., FERPA and state public-records rules in education; HIPAA, SEC, or sector rules elsewhere). Aggressive purging without a hold mechanism converts a privacy control into a spoliation risk.

Why AI Compounds Risk:
Users frequently overshare highly sensitive data—such as PII, PHI, proprietary source code, and corporate strategy—with AI chatbots and development tools. If prompts and chat histories are logged in plain text without strict retention limits or Role-Based Access Control (RBAC), the logging infrastructure (e.g., observability platforms, SIEMs) inadvertently becomes a massive, highly concentrated repository of the organization's most sensitive data, creating a prime target for exfiltration.

Examples:
1. Deploy data loss prevention (DLP) or masking tools to dynamically redact PII, credentials, and sensitive terms from prompts before they are written to observability logs or telemetry platforms.
2. Enforce aggressive data retention limits (e.g., 30 days maximum) on AI chat histories and prompt logs unless the records are subject to an active legal hold or explicitly required for a specific compliance investigation.
3. Restrict access to raw LLM traces and prompt logs strictly to authorized security and debugging personnel, requiring Just-In-Time (JIT) access for any investigations.
4. Implement a documented legal-hold workflow with legal counsel and records management: when a hold is declared, automated purging is suspended for the identified users, agents, and systems, and the held logs are preserved in an access-controlled archive until counsel releases the hold.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
