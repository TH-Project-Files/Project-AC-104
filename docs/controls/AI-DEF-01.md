# AI-DEF-01: Deploy a dedicated AI Triage Agent to perform automated first-pass investigations on security alerts.

**Category:** Governance & People (Layer 0: Governance & System Controls)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 13.1, 13.2, 17.4  
**NIST CSF Subcategories:** DE.AE, RS.AN  

## Details
Detailed Description:
Integrate a securely hosted, read-only AI model at the front of your SIEM alert queue. This "triage agent" must automatically collect evidence, enrich data, and produce a structured disposition (query, think, report) for every alert before human review.

Why AI Compounds Risk:
Frontier AI models are compressing the timeline between vulnerability and exploit from months to hours. Traditional security operations, where humans manually analyze every alert, cannot keep pace with attackers who use AI to probe defenses and exfiltrate data at machine speed.

Examples:
1. Connect an AI model with read-only access to your SIEM to automatically draft triage context for high-volume, noisy alert rules.
2. Automate the bookkeeping and evidence collection around incidents, reserving human analysts purely for making containment and disclosure decisions.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
