# AI-APP-02: Monitor employee devices and networks to block the use of unsanctioned or hidden 'Shadow AI' apps.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: General Usage & AppSec Defense  
**Implementation Group:** IG 1  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Detailed Explanation: This recommendation focuses on gaining visibility and control over the unauthorized use of artificial intelligence tools, often called Shadow AI, by monitoring corporate endpoints and network traffic. It involves identifying unapproved standalone applications, browser extensions, and hidden AI features within sanctioned software that employees use without IT oversight. By monitoring these access points, organizations can enforce security policies, prevent the input of sensitive data into external models, and mitigate risks related to data residency and compliance.

Why AI Compounds Risk:
Why AI Exacerbates Risk: Unlike traditional software, AI models are designed to ingest and process data to generate outputs, and many consumer-grade tools use these inputs for further training, potentially leading to the permanent exposure of proprietary information. The ease of access via browsers and the rapid, often silent, integration of AI features into existing SaaS platforms make it difficult for traditional IT asset management to keep pace. Furthermore, the unpredictable nature of AI outputs and the lack of audit trails for these interactions create significant blind spots for security and compliance teams.

Examples:
1. Corporate Implementation Examples:
2. Deploy Cloud Access Security Brokers (CASB) or intercepting proxies to analyze network traffic and DNS queries for signatures of known AI platforms and APIs.
3. Utilize Endpoint Detection and Response (EDR) or browser monitoring tools to identify locally installed AI agents and browser extensions used for unauthorized tasks like code debugging or document summarization.
4. Implement Data Loss Prevention (DLP) rules that use regex or sensitive data identifiers to block the pasting of confidential information, such as source code or PII, into web-based AI chat interfaces.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
