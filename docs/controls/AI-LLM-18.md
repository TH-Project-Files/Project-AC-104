# AI-LLM-18: Keep different users' AI chats strictly separated so one person's data doesn't accidentally leak into another person's chat.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 3  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Explanation: This recommendation ensures that every user's interaction with an AI system is isolated within a secure, private session. By treating each conversation as a distinct instance mapped to a specific authenticated identity, organizations prevent cross-contamination where one person's sensitive inputs—such as proprietary code, financial data, or personal information—might be surfaced to another user through shared chat histories, system caches, or the model’s internal memory.

Why AI Compounds Risk:
Why AI Exacerbates the Risk:

Examples:
1. Data Training Loops: Many AI models use human inputs to improve and retrain themselves, meaning sensitive data shared by one user could potentially be generated as an answer for a different user in the future.
2. Context and Memory Features: Modern AI assistants often use persistent memory or long context windows to recall past interactions; without strict separation, these features can mistakenly retrieve and display private details from a separate user's session.
3. LLM Scope Violations: AI agents often have the ability to call external tools or databases; poor session management can lead to the AI unintentionally retrieving and leaking internal organizational data to unauthorized employees during a prompt.
4. Corporate Implementation Examples:
5. Unique Session Identifiers: Implement backend logic using unique identifiers (such as UUIDs) for every chat session to ensure that data retrieval requests are strictly bound to the authenticated user's ID and cannot be accessed by other sessions.
6. Enterprise Managed Environments: Utilize enterprise-tier AI subscriptions that offer administrative silos, ensuring that organizational data is isolated from the public model and that individual employee histories remain private within the company's tenant.
7. Robust Backend Security Rules: Configure cloud database permissions and security rules to require mandatory authentication for every data request, preventing "authenticated user" vulnerabilities where any logged-in person could potentially view the entire database of stored chats.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
