# AI-RAG-01: Implement RAG authorization enforcement and security trimming to ensure AI only synthesizes data the user is permitted to see.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 4: Data  
**Implementation Group:** IG 2  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `3.3, 5.1` | NIST CSF: `PR.AC, PR.DS`

---

## Control Details
Detailed Description:
Implement strict access control mapping and "security trimming" within Retrieval-Augmented Generation (RAG) pipelines so the AI can only retrieve and synthesize information that the querying user is explicitly authorized to access. 

Why AI Compounds Risk:
Generative AI acts as a powerful aggregator. If an AI application has global read access to the backend document repository (e.g., SharePoint, Google Drive, Confluence, S3) and does not trim retrieval results based on the querying user's permissions, any employee could ask the chatbot for "next quarter's layoff list," "executive salary bands," or "M&A strategy"—and the RAG pipeline would dutifully fetch and summarize it.

Examples:
1. Enforce pass-through authentication (e.g., OAuth delegation) so the RAG indexing and querying mechanisms assume the identity and exact file-level permissions of the end-user.
2. Implement access control lists (ACLs) directly within the vector database to cryptographically filter document chunks before prompt assembly.
3. Periodically audit RAG system service accounts to ensure they do not default to excessive, tenant-wide global read permissions across the enterprise.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
