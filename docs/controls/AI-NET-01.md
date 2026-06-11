# AI-NET-01: Mandate enterprise Secure Recursive DNS with encrypted lookups (DoH/DoT) backed by real-time “big data” threat intelligence to block malicious domains and resist DNS spoofing/hijacking

**Category:** Networking (Layer 3: Network)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 9.2  
**NIST CSF Subcategories:** PR.IR  
**Layered with:** Malicious-domain defense chain — AI-NET-06 supplies the threat-intelligence feeds; this control is the DNS-resolution enforcement layer; AI-NET-03 applies domain-age policy (NRD/parked) at the firewall and DNS filter. One outcome, three enforcement points: implement as a single pipeline, not three separate products.

---

## Details
Detailed Description:
Implement enterprise-grade Secure Recursive DNS services that support encrypted lookups via DNS over HTTPS (DoH) or DNS over TLS (DoT). These services must be backed by real-time, large-scale ("big data") threat intelligence to automatically block connections to newly registered malicious domains, botnet command-and-control servers, and phishing sites, while also protecting the integrity and privacy of DNS queries.

Why AI Compounds Risk:
AI dramatically accelerates the creation of malicious infrastructure. Adversaries use AI to automatically generate thousands of highly convincing typosquatted domains and dynamically alter domain generation algorithms (DGAs) in real-time to evade traditional blocklists. By the time static, legacy threat lists update, the AI-driven attack has already shifted to new domains. Real-time, big-data backed secure DNS is essential to detect and block these ephemeral, machine-speed domain variations before users can connect.

Examples:
1. Deploy an enterprise DNS security solution that supports real-time global threat intelligence, category controls, Newly Registered Domain (NRD) / Domain Generation Algorithm (DGA) protection, and API export to the SIEM.
2. Enforce encrypted DNS (DoH/DoT) configurations via Mobile Device Management (MDM) or Group Policy (GPO) to prevent local network hijacking and eavesdropping on DNS queries.
3. Block outbound port 53 and unapproved DoH/DoT IP addresses at the firewall to ensure all endpoints, including unmanaged IoT devices, are forced to use the organization's secure recursive DNS infrastructure.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
