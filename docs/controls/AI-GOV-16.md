# AI-GOV-16: Establish AI-specific change management and evaluation gates requiring regression testing, approvals, and rollback plans for updates to models, prompts, agent tools, or RAG datasets.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: Governance & System Controls  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `2.1, 16.6, 16.7` | NIST CSF: `PR.IP, GV.SC`

---

## Control Details
Detailed Description:
Establish specialized AI change management workflows and evaluation gates for updates to any component of an AI system. This means that modifications to model versions, prompt templates, agent tools/plugins, or the Retrieval-Augmented Generation (RAG) corpus must go through formal change control, requiring automated regression tests (checking for jailbreaks, data leakage, and tool abuse), explicit approvals, and tested rollback plans before reaching production.

Why AI Compounds Risk:
Unlike traditional software where behavior is strictly governed by static code, AI systems are non-deterministic. Their behavior can drastically change simply by altering a system prompt, adding a new document to the RAG knowledge base, or pointing the application to an updated LLM version. Standard CI/CD change management often misses these non-code updates. Without AI-specific evaluation gates, a seemingly harmless prompt tweak or data upload can silently introduce massive vulnerabilities, such as bypassing safety filters or exposing restricted data to autonomous agents.

Examples:
1. Integrate AI-specific regression testing tools (e.g., prompt vulnerability scanners, LLM evaluation frameworks) into the CI/CD pipeline to automatically test for jailbreak regressions and prompt injection susceptibility before any prompt template change is deployed.
2. Require formal Change Advisory Board (CAB) or security team approval for the introduction of new agentic tools/plugins, treating them with the same rigor as deploying a new firewall rule or external API integration.
3. Establish a version control and rollback strategy for RAG knowledge bases, ensuring that if a newly ingested document causes an AI chatbot to leak sensitive information or hallucinate, the system can instantly revert to the previous verified state.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
