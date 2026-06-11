# AI-LLM-22: Enforce strict environment variable and secret scoping for AI agent runtimes to prevent unconditional inheritance of the parent process environment.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 16.1, 16.4  
**NIST CSF Subcategories:** PR.PS  

## Details
Detailed Description:
Restrict AI agent subprocesses from inheriting the full parent environment (e.g., Node.js `process.env`). Secrets, API keys, and connection strings must be securely scoped, injected, or retrieved via token exchange only when explicitly required by authorized tools.

Why AI Compounds Risk:
LLMs cannot be trusted with raw memory or environment access. An attacker using prompt injection can command the AI to enumerate and exfiltrate all system environment variables, instantly stealing cloud, database, and encryption keys that happen to be loaded into the host process.

Examples:
1. Refactor agent loaders to pass a localized, minimal environment object instead of the global process environment.
2. Utilize a dedicated Secrets Manager API within specific tool logic rather than injecting secrets as static environment variables.
3. Enforce containerized or sandboxed runtimes for the agent processes where the host environment is inherently masked.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
