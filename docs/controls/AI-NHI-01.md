# AI-NHI-01: Establish Non-Human Identity (NHI) Inventory and Governance (service accounts, API keys, tokens, agent identities)

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: Governance & System Controls  
**Implementation Group:** IG 2  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `5.1, 5.2, 6.8` | NIST CSF: `ID.AM, PR.AA, PR.AC`

---

## Control Details
Detailed Description:
Implement a comprehensive centralized inventory and lifecycle governance program for all non-human identities (NHIs). This includes service accounts, API keys, OAuth tokens, machine identities, and autonomous AI agent identities. The program must track ownership, enforce least privilege (RBAC), and mandate regular rotation and auditing of these credentials.

Why AI Compounds Risk:
AI systems, particularly autonomous agents and large language model (LLM) pipelines, heavily rely on non-human identities to interact with databases, APIs, and cloud services at machine speed. As organizations deploy more AI integrations, the rapid proliferation of unmanaged API keys, hidden service accounts, and overly permissive OAuth tokens creates a massive, invisible attack surface. If an adversary compromises an AI prompt or an agent's workspace, they can immediately harvest these NHIs to pivot laterally, exfiltrate data, or escalate privileges without ever triggering human-centric MFA or behavioral alerts.

Examples:
1. Deploy an NHI management platform or Cloud Infrastructure Entitlement Management (CIEM) tool to continuously auto-discover and map all service accounts, API keys, and OAuth tokens.
2. Enforce strict lifecycle policies for AI-associated identities, prioritizing the use of short-lived/ephemeral tokens and mandatory automated credential rotation rather than static API keys.
3. Implement behavioral monitoring specifically for non-human accounts to detect anomalies, such as an AI agent service account suddenly calling an administrative API or moving large volumes of data outside its baseline.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
