# AI-GOV-16: Establish AI-specific change management and evaluation gates requiring regression testing, approvals, and rollback plans for updates to models, prompts, agent tools, or RAG datasets.

**Category:** Governance & People (Layer 0: Governance & System Controls)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 2.1, 16.6, 16.7  
**NIST CSF Subcategories:** PR.PS, GV.SC  
**Layered with:** AI-LLM-10 (pre-deployment agent testing these gates automate), AI-GOV-13 and AI-LLM-16 (red-team findings feed new gate test cases), AI-DET-01 (runtime detection of what gates miss — confirmed detections become regression tests), AI-REC-01 (the rollback capability these gates invoke)

---

## Details
Detailed Description:
Establish specialized AI change management workflows and evaluation gates for updates to any component of an AI system. This means that modifications to model versions, prompt templates, agent tools/plugins, or the Retrieval-Augmented Generation (RAG) corpus must go through formal change control, requiring automated regression tests (checking for jailbreaks, data leakage, and tool abuse), explicit approvals, and tested rollback plans before reaching production.

Minimum Evaluation Gate Requirements:
To make the regression-testing mandate auditable, the CI/CD gate must enforce:
- Versioned golden datasets: curated prompt/response test sets stored and versioned alongside the prompts, model configurations, and RAG manifests they validate, and updated whenever red teaming (AI-GOV-13, AI-LLM-16) or runtime detections (AI-DET-01) surface a new attack pattern.
- Adversarial benchmark coverage: every gate run must execute jailbreak, prompt-injection, and restricted-data-leakage suites against the candidate change, not just functional accuracy checks.
- Defined pass/fail thresholds with block-on-fail: e.g., the safety layer must catch a defined percentage of the known-jailbreak corpus and show zero regressions on restricted-data probes; threshold failures block promotion rather than merely warn.
- Behavioral baseline comparison: diff tool-call patterns and output distributions between the current and candidate versions to surface silent drift that individual test cases miss.

Why AI Compounds Risk:
Unlike traditional software where behavior is strictly governed by static code, AI systems are non-deterministic. Their behavior can drastically change simply by altering a system prompt, adding a new document to the RAG knowledge base, or pointing the application to an updated LLM version. Standard CI/CD change management often misses these non-code updates. Without AI-specific evaluation gates, a seemingly harmless prompt tweak or data upload can silently introduce massive vulnerabilities, such as bypassing safety filters or exposing restricted data to autonomous agents.

Examples:
1. Integrate an LLM evaluation framework into the CI/CD pipeline as a blocking gate: every prompt-template or model-version change runs the versioned jailbreak and data-leakage suites, and promotion is denied automatically if detection falls below the defined threshold or any restricted-data probe regresses.
2. Require formal Change Advisory Board (CAB) or security team approval for the introduction of new agentic tools/plugins, treating them with the same rigor as deploying a new firewall rule or external API integration.
3. Establish a version control and rollback strategy for RAG knowledge bases, ensuring that if a newly ingested document causes an AI chatbot to leak sensitive information or hallucinate, the system can instantly revert to the previous verified state.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
