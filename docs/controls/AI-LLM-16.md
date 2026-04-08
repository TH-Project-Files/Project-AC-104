# AI-LLM-16: Regularly test internal AI systems by having security teams pretend to be hackers (Red Teaming) to find weak spots.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 3  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
AI red teaming is a structured, adversarial testing process where security teams simulate real-world attacks to identify vulnerabilities in AI models, data pipelines, and APIs before they can be exploited. This proactive approach goes beyond traditional software testing by focusing on the unique ways AI can misbehave, such as through prompt injection, data poisoning, or model evasion, to ensure the system is resilient and trustworthy.

Why AI Compounds Risk:
AI exacerbates cybersecurity risks because its probabilistic and open-ended nature introduces a larger, more complex attack surface that traditional security tools often miss. Unlike static code, AI systems can be manipulated through natural language (prompt injection), their learning process can be corrupted (data poisoning), and they may inadvertently leak sensitive training data or execute unauthorized actions when integrated with enterprise tools.

Examples:
1. Implement a policy for continuous automated red teaming by using "red team LLMs" to generate thousands of adversarial prompts at scale to test for jailbreaks and content policy violations.
2. Conduct manual red teaming exercises using diverse security experts to simulate sophisticated "role-playing" or "encoding" attacks that attempt to bypass safety guardrails and access restricted internal information.
3. Perform operational risk assessments on agentic AI by testing whether autonomous agents can be tricked into executing unauthorized financial transactions or database queries through conversational manipulation.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
