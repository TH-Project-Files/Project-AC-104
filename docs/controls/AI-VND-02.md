# AI-VND-02: Enforce AI vendor minimum security terms, explicitly mandating "no training on customer data," strict tenancy, and guaranteed log access.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: Governance & System Controls  
**Implementation Group:** IG 1  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `15.1, 15.2` | NIST CSF: `GV.SC`

---

## Control Details
Detailed Description:
Enforce standardized, non-negotiable minimum security terms in all contracts with AI vendors and SaaS providers introducing AI features. This must explicitly mandate "zero data retention for model training," strict data tenancy isolation, guaranteed log exports, and data residency compliance.

Why AI Compounds Risk:
Many AI vendors—especially consumer-focused ones pivoting to B2B—default to using customer prompts and data to train their future public models. Without explicit contractual "opt-outs" and tenancy guarantees, sensitive enterprise data entered into an AI tool could be memorized by the provider's model and inadvertently leaked to competitors or the public via future user queries.

Examples:
1. Require vendors to sign a Data Processing Agreement (DPA) explicitly stating that customer data (prompts, RAG context, file uploads, outputs) will absolutely not be used to train, fine-tune, or improve foundational models.
2. Mandate that multi-tenant AI SaaS platforms provide logical separation and encrypted isolation of tenant workspaces, with Bring Your Own Key (BYOK) support where applicable.
3. Ensure the vendor supports automated export of AI interaction logs and audit trails to the enterprise SIEM via API for continuous monitoring.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
