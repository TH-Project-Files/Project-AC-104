# AI-APP-08: Monitor 3rd-party connections via Cloud Application Security Broker (CASB)

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: General Usage & AppSec Defense  
**Implementation Group:** IG 3  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Detailed Explanation: This recommendation involves using a Cloud Application Security Broker (CASB) as an intermediary security enforcement point between an organization's users and cloud service providers. It works by discovering all third-party cloud applications in use (including shadow IT), classifying them based on risk and data sensitivity, and enforcing security policies like data loss prevention (DLP), encryption, and access control in real-time to protect corporate data and monitor user behavior.

Why AI Compounds Risk:
Why AI Exacerbates the Risk: AI increases risk because many third-party applications now embed "shadow AI" features without explicit disclosure, potentially leading to unauthorized data training on sensitive corporate information. Furthermore, the rapid evolution and automated decision-making of AI tools can create new vulnerabilities, such as model drift or data exfiltration, which traditional manual vendor assessments are too slow to detect or quantify.

Examples:
1. Use a CASB's auto-discovery and API-based scanning features to identify all unsanctioned AI-enabled third-party tools being used by employees and block those that do not meet the organization's risk profile.
2. Configure granular DLP policies within the CASB to prevent users from uploading files containing sensitive personal information or intellectual property to authorized third-party SaaS platforms.
3. Deploy an inline CASB proxy to monitor real-time traffic for anomalous behavior, such as a sudden surge in data downloads by an employee, and automatically trigger access restrictions to mitigate potential insider threats or compromised accounts.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
