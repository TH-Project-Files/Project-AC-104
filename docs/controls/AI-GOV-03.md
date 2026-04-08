# AI-GOV-03: Establish an Approved AI Service Catalog and enforce it via web proxies/CASB, explicitly limiting employee access to only vetted and sanctioned AI tools.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: Governance & System Controls  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `15.1, 17.1` | NIST CSF: `GV.PO, GV.OV`

---

## Control Details
Detailed Description:
This recommendation involves creating a centralized, vetted list of approved AI services and using technical controls like Cloud Access Security Brokers (CASB) or web proxies to block access to unmanaged "Shadow AI" while allowing only sanctioned tools.

Why AI Compounds Risk:
AI exacerbates risk because the rapid proliferation of easy-to-use GenAI tools leads to widespread "Shadow AI" usage, where employees may inadvertently upload sensitive proprietary data or personally identifiable information into public models that use the data for training.

Examples:
1. Configure a CASB to automatically discover all AI applications in use, assign risk scores to them, and enforce real-time block policies on high-risk or unsanctioned AI websites.
2. Implement a service catalog within an ITSM platform where employees can view and request access to pre-vetted AI tools that meet company security and compliance standards.
3. Use a Secure Web Gateway to apply granular controls, such as allowing "view only" access to certain AI sites while blocking the ability to "upload" or "post" content to prevent data exfiltration.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
