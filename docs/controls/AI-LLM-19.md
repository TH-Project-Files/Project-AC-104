# AI-LLM-19: Keep a 'nutrition label' (Bill of Materials) for your AI models and verify that no one has tampered with their code or plugins.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 3  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `15.1` | NIST CSF: `GV.SC`

---

## Control Details
Detailed Description:
This recommendation advises organizations to maintain an AI Bill of Materials (AIBOM), which is a machine-readable inventory of every dataset, model, and software component used in an AI system. It serves as a "nutrition label" to provide transparency into the system's "ingredients," such as data provenance, model lineage, and third-party dependencies. This process ensures that the AI's code and plugins remain secure and uncorrupted by verifying their integrity throughout the development and deployment lifecycle.

Why AI Compounds Risk:
AI exacerbates security risks because it is not static software; it is a "living" system that evolves through retraining and depends on complex, often external, data pipelines. This complexity creates a larger attack surface where malicious actors can inject corrupted data (data poisoning) or manipulate model behavior through untrusted plugins and hidden dependencies, which traditional security tools may fail to detect.

Examples:
1. Use automated tools to generate and update AIBOMs within CI/CD pipelines to ensure the inventory reflects real-time changes in models and datasets.
2. Implement standardized profiles, such as SPDX 3.0, to document model architecture, licensing, and training data sources in a consistent, interoperable format.
3. Establish a formal governance framework that assigns clear ownership to MLOps and data science teams for monitoring "trust ingredients," such as data deletion policies and human-in-the-loop oversight.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
