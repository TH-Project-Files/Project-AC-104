# AI-LLM-17: Force AI tools that write or run code to do so in a secure, isolated bubble (sandbox) so they can't break anything on the network.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 3  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Detailed Explanation: Sandboxing creates a secure, isolated runtime environment where AI-generated code can execute without direct access to the host operating system, production databases, or internal networks. This isolation ensures that even if the AI generates malicious or buggy code, the impact is contained within a temporary "bubble," preventing system-wide crashes, data exfiltration, or unauthorized lateral movement across the corporate infrastructure.

Why AI Compounds Risk:
Why AI Exacerbates Risk: Unlike human-written code that goes through peer review, AI models can generate billions of lines of code instantly that may contain hallucinations, unintentional vulnerabilities, or "jailbroken" malicious logic. Since AI agents often require autonomy to perform tasks, allowing them to execute code directly on application servers or local machines without isolation creates a high-speed vector for spreading malware, leaking secrets, or corrupting critical data at scale.

Examples:
1. Deploy ephemeral, container-based sandboxes using tools like container orchestration platforms with sandboxed runtimes to provide microVM isolation for every AI-generated task.
2. Integrate specialized AI execution APIs to run untrusted code in short-lived environments that automatically terminate after a task is completed.
3. Use WebAssembly (WASM) runtimes to execute AI-generated Python or JavaScript in a lightweight, browser-based or server-side sandbox that strictly limits filesystem and network access.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
