# AI-APP-04: Conduct regular OSINT gathering (e.g., Google Dorking) to discover shadow authentication portals or legacy logins for the domain, and secure them behind a VPN or firewall.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: General Usage & AppSec Defense  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `18.1` | NIST CSF: `ID.RA`

---

## Control Details
Detailed Description:
Recommendation Explanation: This strategy involves using Open Source Intelligence (OSINT) and advanced search engine queries, known as advanced search operator queries, to identify publicly indexed but unintended access points. By using specific operators like site:, inurl:, and intitle:, security teams can locate "shadow" authentication portals, forgotten legacy login pages, or misconfigured administrative interfaces that exist outside of official IT oversight. Once discovered, these entry points are secured behind a VPN or firewall to prevent unauthorized access and reduce the organization's external attack surface.

Why AI Compounds Risk:
How AI Exacerbates the Risk: The rapid, unmanaged adoption of generative AI tools (Shadow AI) creates new "shadow" authentication vectors, such as unauthorized API keys, embedded credentials in AI plugins, and personal accounts used for corporate tasks that bypass enterprise logging. AI-powered bots can also automate the discovery of these vulnerabilities at scale, while "agentic" AI workflows may autonomously create persistent, unmanaged non-human identities with access to internal systems, significantly widening the potential for data exfiltration and credential theft.

Examples:
1. Use the query site:\[suspicious link removed\] inurl:login OR inurl:admin to find and catalog all publicly accessible login pages, then verify if they are integrated into the company's Single Sign-On (SSO) or if they should be restricted to internal network access only.
2. Conduct regular searches for exposed configuration or log files using queries like site:\[suspicious link removed\] filetype:env OR filetype:log "password" to identify if developers have inadvertently indexed sensitive credentials or system settings that could lead to portal compromise.
3. Monitor for "Shadow AI" infrastructure by searching for unapproved third-party AI interfaces or "index of" directories containing AI training datasets and model configurations using queries like intitle:"index of" "models" OR "datasets" site:\[suspicious link removed\].

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
