# AI-LLM-18: Enforce strict per-user session and context isolation in multi-tenant AI applications.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 16.1  
**NIST CSF Subcategories:** PR.DS

---

## Details
Detailed Description:
This recommendation ensures that every user's interaction with an AI system is isolated within a secure, private session. By treating each conversation as a distinct instance mapped to a specific authenticated identity, organizations prevent cross-contamination where one person's sensitive inputs—such as proprietary code, financial data, or personal information—might be surfaced to another user through shared chat histories, system caches, or the model’s internal memory.

Why AI Compounds Risk:
Session-isolation failures are amplified by three AI-specific mechanisms. Data training loops: models that learn from user inputs can surface one user's sensitive data in another user's answers. Context and memory features: persistent memory and long context windows can mistakenly retrieve private details from a separate user's session. Scope violations: agents that call external tools or databases under poor session management can retrieve and leak internal data to unauthorized employees during a prompt.

Examples:
1. Unique Session Identifiers: Implement backend logic using unique identifiers (such as UUIDs) for every chat session to ensure that data retrieval requests are strictly bound to the authenticated user's ID and cannot be accessed by other sessions.
2. Enterprise Managed Environments: Utilize enterprise-tier AI subscriptions that offer administrative silos, ensuring that organizational data is isolated from the public model and that individual employee histories remain private within the company's tenant.
3. Robust Backend Security Rules: Configure cloud database permissions and security rules to require mandatory authentication for every data request, preventing "authenticated user" vulnerabilities where any logged-in person could potentially view the entire database of stored chats.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
