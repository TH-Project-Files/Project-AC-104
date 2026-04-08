# AI-LLM-07: Automatically scan and clean up the text users send to AI to stop them from sharing too much sensitive information.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
This recommendation involves implementing automated tools to scan user prompts in real-time for sensitive data such as PII, financial details, or intellectual property, and then sanitizing that text through redaction, anonymization, or blocking before it reaches the AI model.

Why AI Compounds Risk:
AI exacerbates data exposure risks because models often ingest and store user inputs for future training, making sensitive information retrievable by others, and employees frequently use AI to process large volumes of data for efficiency without realizing the security trade-offs.

Examples:
1. Deploy an AI-driven Data Loss Prevention (DLP) gateway that sits between users and LLMs to automatically identify and redact sensitive patterns like Social Security numbers or API keys in flight.
2. Use semantic prompt detection tools to recognize the context of a query and block or flag interactions that attempt to share proprietary business logic or unreleased internal documents.
3. Implement enterprise-sanctioned AI platforms that integrate with existing cloud security tools to provide full audit logging and real-time user guidance when a policy violation is attempted.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
