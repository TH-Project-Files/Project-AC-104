# AI-LLM-11: Continuously scan and classify sensitive company data so you know exactly what information AI tools might access.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `3.1, 3.12` | NIST CSF: `ID.AM, PR.DS`

---

## Control Details
Detailed Description:
Explanation: This recommendation involves using automated tools to proactively identify, inventory, and label sensitive information—such as PII, financial records, and intellectual property—across all corporate storage environments. By maintaining a continuous scanning pipeline, organizations can ensure that data is categorized by sensitivity levels (e.g., Public, Internal, Confidential, Restricted) in real-time, allowing for the application of appropriate security controls and access boundaries before data is ingested or processed by AI systems.

Why AI Compounds Risk:
Why AI Exacerbates Risk: AI models, particularly Large Language Models, can inadvertently memorize and leak sensitive training data through their outputs, a phenomenon known as privacy leakage. Furthermore, AI systems often require vast amounts of data to function, which increases the likelihood of "shadow data" or "dark data" being ingested without proper oversight, potentially exposing trade secrets or regulated information to unauthorized users via simple natural language queries.

Examples:
1. Deploy automated data classification pipelines, such as a cloud provider DLP or a native data compliance solution, to scan cloud storage buckets and SharePoint sites on a recurring schedule to tag files containing sensitive information types like Social Security numbers or credit card data.
2. Integrate sensitive data monitoring solutions that use machine learning to identify unstructured data patterns (e.g., source code or legal agreements) and automatically apply digital tags or metadata that trigger Data Loss Prevention (DLP) actions, such as blocking the data from being uploaded to external Generative AI tools.
3. Establish a risk-based data governance framework that requires all new data assets to be classified at the point of creation, combined with periodic "on-demand" scans of legacy data repositories to identify and quarantine sensitive items that do not meet the security requirements for AI processing.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
