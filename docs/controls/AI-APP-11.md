# AI-APP-11: Establish a secrets management baseline for AI stacks, mandating centralized secrets managers and prohibiting hardcoded API keys in repos, notebooks, and prompt templates.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Application  
**Implementation Group:** IG 1  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `16.2, 16.3` | NIST CSF: `PR.DS, DE.CM`

---

## Control Details
Detailed Description:
Establish a strict secrets management baseline across all AI development stacks and agent toolchains. This requires prohibiting the hardcoding of API keys, tokens, or credentials within source code repositories, Jupyter notebooks, prompt templates, or CI/CD logs. All sensitive credentials must be dynamically retrieved from a centralized enterprise secrets manager, and automated scanning must be implemented to detect and block leaked keys.

Why AI Compounds Risk:
AI development workflows are highly experimental and fast-paced. Data scientists and engineers frequently rely on Jupyter notebooks, prompt debugging tools, and local tracing environments to rapidly test external LLM APIs or agent integrations. These environments are notorious for inadvertently leaking long-lived API keys. If an adversary or automated bot scrapes a leaked LLM API key or an agent's backend token, they can instantly incur massive cloud compute costs (Denial of Wallet) or pivot directly into backend databases, entirely bypassing the organization's front-end AI security gateways and access controls.

Examples:
1. Integrate automated secret scanning tools (e.g., git-leaks, GitHub Advanced Security) into the CI/CD pipeline to detect and block commits containing hardcoded LLM API keys or autonomous agent tokens.
2. Mandate that all AI development environments and agent frameworks retrieve credentials dynamically at runtime via a centralized enterprise Secrets Manager, explicitly forbidding hardcoded credentials in Jupyter notebooks or prompt templates.
3. Configure automated redaction of sensitive credentials, API keys, and authorization headers within LLM observability platforms, tracing tools (like LangSmith/Phoenix), and prompt debugging logs.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
