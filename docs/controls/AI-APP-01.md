# AI-APP-01: Enforce Strict Input Sanitization frameworks against AI fuzzing

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: General Usage & AppSec Defense  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Enforce Strict Input Sanitization: This recommendation involves implementing robust frameworks to clean, filter, and validate all data entering an AI system to ensure it is free of malicious code, unexpected characters, or hidden instructions. It acts as a primary defense by neutralizing threats like prompt injection, SQL injection, and cross-site scripting (XSS) before they reach the model or underlying infrastructure.

Why AI Compounds Risk:
AI Risk Exacerbation: Generative AI increases the complexity of input threats because attackers can use AI-powered fuzzing to automatically generate thousands of "innocent-looking" but structurally plausible inputs that exploit a model's probabilistic logic. These automated attacks can identify subtle triggers—such as specific formatting symbols or context-shifting phrases—at a scale and speed that manual security testing cannot match, making traditional static defenses insufficient.

Examples:
1. Implement Action-Selector Patterns: Force AI agents to output strictly typed JSON schemas with predefined action IDs rather than open-ended natural language. This treats the model's output as data rather than executable instructions, effectively freezing control flow and preventing semantic manipulation of downstream functions.
2. Deploy AI-SPM and WAF Tools: Utilize AI-Security Posture Management (AI-SPM) tools to gain visibility into the AI supply chain and identify risks in third-party frameworks. Combine this with Web Application Firewalls (WAF) configured to detect anomalous input patterns and block known adversarial sequences before they are processed.
3. Use Structural Spotlighting: Implement "spotlighting" techniques to mathematically or structurally delimit untrusted user data from privileged system instructions. If the system detects an input attempting to "break out" of its assigned zone to influence the operational plan, the workflow is automatically halted to prevent unauthorized actions.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
