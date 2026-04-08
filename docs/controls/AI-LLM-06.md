# AI-LLM-06: Ensure AI agents operate using the requesting user's own identity and access permissions (e.g., via OAuth/OIDC tokens) rather than relying on highly privileged, hard-coded service accounts or static API keys.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `6.2, 6.8` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
This recommendation advocates for authenticated delegation, where AI agents use short-lived, scoped tokens (like OAuth 2.1 with PKCE) linked to the specific human user's identity to ensure they only access data and systems the user is personally authorized to use. Moving away from static API keys or highly privileged service accounts prevents "privilege escalation" and ensures that every autonomous action is traceable to a specific human principal through a clear delegation chain.

Why AI Compounds Risk:
AI exacerbates security risks because agents operate at machine speed and can be non-deterministic, potentially taking unpredictable actions or triggering "unbounded automation loops" that a static service account wouldn't catch. Without user-bound identities, an agent's activity is indistinguishable from system-level actions, creating massive accountability gaps and a larger "blast radius" if an agent is manipulated via prompt injection to access sensitive data beyond its intended task.

Examples:
1. Implement an OAuth 2.0 On-Behalf-Of (OBO) flow for internal tools, where a customer support an AI assistant receives a delegated token to access a CRM only with the specific permissions of the logged-in representative.
2. Integrate the Model Context Protocol (MCP) with an OIDC-compliant authorization server to allow AI agents to dynamically discover tools and receive purpose-bound, short-lived credentials for specific administrative tasks.
3. Require "out-of-band" human authentication, such as a push notification or biometrics, before an AI agent can use a delegated token to execute high-risk financial transactions or infrastructure changes.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
