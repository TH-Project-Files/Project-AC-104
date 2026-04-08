# AI-LLM-13: Ensure that when AI tools talk to each other or use plugins, they prove who they are and only share the minimum necessary data.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Detailed Explanation: This recommendation emphasizes two pillars of secure interoperability for AI agents and plugins: identity verification and data minimization. First, every AI component must have a verifiable identity (authentication) to ensure that only authorized agents can initiate actions or access services. Second, once authenticated, these tools must adhere to the principle of least privilege, sharing only the specific data points required to complete a task (authorization), rather than providing broad access to underlying databases or user contexts.

Why AI Compounds Risk:
Why AI Exacerbates Risk: AI agents often operate autonomously and at high velocity, performing thousands of operations per minute which makes manual human oversight impossible. Unlike traditional software, AI is probabilistic and can be manipulated via prompt injection to perform "excessive agency," where it might overshare sensitive data or call unauthorized APIs if strict, deterministic security boundaries and identity-linked scopes are not enforced.

Examples:
1. Deploy an OAuth 2.0 or 2.1 framework where every AI agent is registered as a unique non-human entity with short-lived, scoped access tokens. This ensures that if an agent needs to "write to a calendar," its token is restricted to that specific action and cannot be used to "delete files" or "read emails."
2. Use an AI Gateway to centralize authentication and enforce strict schema validation. The gateway can intercept outgoing requests from an AI tool to a plugin, stripping out any PII (Personally Identifiable Information) or unnecessary metadata before the data reaches the external service.
3. Implement Fine-Grained Authorization (FGA) within RAG (Retrieval-Augmented Generation) pipelines. When a coordinator agent asks a retrieval plugin for information, the system should check the original user's identity claims against document metadata to ensure the agent only "sees" and "shares" the specific text chunks the user is legally permitted to access.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
