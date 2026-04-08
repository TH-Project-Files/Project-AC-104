# AI-APP-07: Integrate Dynamic Application Security Testing (DAST) into CI/CD

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: General Usage & AppSec Defense  
**Implementation Group:** IG 3  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Integrate Dynamic Application Security Testing (DAST) into CI/CD involves automating black-box security scans that test running applications from the outside-in. Unlike static analysis, DAST simulates real-world attacks (like SQL injection or XSS) on a deployed staging or ephemeral environment to identify runtime vulnerabilities, misconfigurations, and business logic flaws. By embedding these scans directly into the CI/CD pipeline, organizations can catch exploitable issues before code reaches production, creating a continuous security feedback loop.

Why AI Compounds Risk:
AI exacerbates the risk because AI coding assistants generate code at a velocity that traditional manual security reviews cannot sustain, leading to a massive increase in potential vulnerabilities. Furthermore, AI-generated code can introduce systematic risks and "context gaps" such as misunderstood authentication flows or prompt injection vulnerabilities that static tools often miss. Because AI allows for multiple daily deployments, traditional weekly or manual scans leave a significant window of time where unchecked, AI-generated vulnerabilities can be exploited in a live environment.

Examples:
1. Automate DAST scans as a non-blocking stage in an enterprise code repository's CI/CD pipeline that triggers immediately after code is successfully deployed to a dedicated staging environment.
2. Use API-first DAST tools to automatically scan OpenAPI or GraphQL schemas, ensuring that modern API endpoints are covered during every build or merge request.
3. Configure "scan-in-scope" tests for routine pull requests to maintain development speed, while reserving full, deep-dive DAST scans for nightly builds or pre-production deployment schedules.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
