# AI-END-08: Deploy Data Loss Prevention (DLP) to monitor formatted file exfiltration

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 6: Endpoint Presentation  
**Implementation Group:** IG 3  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `4.1` | NIST CSF: `PR.PS`

---

## Control Details
Detailed Description:
Deploying Data Loss Prevention (DLP) to monitor formatted file exfiltration involves using security tools to identify, track, and block the unauthorized transfer of structured and unstructured files (such as PDF, DOCX, or XLSX) across endpoints, networks, and cloud environments.

Why AI Compounds Risk:
Traditional DLP uses content awareness (scanning for patterns like Social Security numbers) and context analysis (inspecting file metadata like size and format) to enforce security policies and prevent sensitive data from leaving the corporate perimeter via email, USB, or web uploads.

Examples:
1. AI exacerbates this risk because generative AI tools can easily ingest, summarize, or paraphrase sensitive formatted documents, allowing users to inadvertently or maliciously exfiltrate proprietary information through natural language prompts that bypass simple keyword-based filters.
2. Use Endpoint DLP agents on corporate laptops to monitor and block users from copying sensitive formatted files to unauthorized USB drives or uploading them to personal cloud storage accounts.
3. Implement Network DLP to inspect outbound email attachments and web traffic in real time, automatically encrypting or blocking files that contain regulated data like PII or intellectual property.
4. Integrate Cloud-native DLP with SaaS platforms like enterprise productivity suites to audit file sharing permissions and prevent sensitive documents from being shared with external, unauthorized email addresses.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
