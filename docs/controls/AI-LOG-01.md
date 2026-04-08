# AI-LOG-01: Establish policies and controls for AI prompt/chat retention, privacy masking, and strict access management for observability logs.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 4: Data  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `3.2, 8.12` | NIST CSF: `PR.DS, DE.CM`

---

## Control Details
Detailed Description:
Establish formal policies and technical controls for the retention, privacy masking, and access management of AI prompt logs, chat histories, and LLM tracing data.

Why AI Compounds Risk:
Users frequently overshare highly sensitive data—such as PII, PHI, proprietary source code, and corporate strategy—with AI chatbots and development tools. If prompts and chat histories are logged in plain text without strict retention limits or Role-Based Access Control (RBAC), the logging infrastructure (e.g., observability platforms, SIEMs) inadvertently becomes a massive, highly concentrated repository of the organization's most sensitive data, creating a prime target for exfiltration.

Examples:
1. Deploy data loss prevention (DLP) or masking tools to dynamically redact PII, credentials, and sensitive terms from prompts before they are written to observability logs or telemetry platforms.
2. Enforce aggressive data retention limits (e.g., 30 days maximum) on AI chat histories and prompt logs unless explicitly required for a specific compliance investigation.
3. Restrict access to raw LLM traces and prompt logs strictly to authorized security and debugging personnel, requiring Just-In-Time (JIT) access for any investigations.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
