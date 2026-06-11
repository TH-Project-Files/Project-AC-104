# AI-APP-12: Govern, sanitize, and monitor AI-specific indexing files (e.g., llms.txt and llms-full.txt) to prevent sensitive data exposure and indirect prompt injection.

**Category:** Applications & Data (Layer 7: Application)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 3.1, 13.2, 16.1  
**NIST CSF Subcategories:** PR.DS, PR.PS  

## Details
Detailed Description:
Establish strict governance over the creation and modification of machine-readable AI indexing files like llms.txt. Ensure these files undergo automated sensitive data scanning (DLP) before publication and utilize File Integrity Monitoring (FIM) to detect unauthorized tampering.

Why AI Compounds Risk:
The llms.txt standard allows organizations to compile their site's data into a single, AI-optimized Markdown file. If ungoverned, developers might inadvertently expose restricted data. Furthermore, because AI agents automatically parse and trust this file for context, a compromised llms.txt file is an ideal delivery mechanism for indirect prompt injection attacks targeting downstream AI workflows.

Examples:
1. Require all llms.txt and llms-full.txt files to pass through a CI/CD pipeline equipped with secret scanning and DLP before being deployed to the public-facing web root.
2. Implement File Integrity Monitoring (FIM) on the web server to alert security teams immediately if the llms.txt file is modified outside of approved deployment windows.
3. Establish a formal policy dictating what content categories (e.g., public tutorials, API schemas) are permitted in AI index files, explicitly forbidding the inclusion of internal architecture or beta endpoints.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
