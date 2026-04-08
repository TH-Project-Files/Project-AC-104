# AI-NET-02: Implement Strict Egress Filtering to stop C2 callbacks

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 3: Network  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `4.4, 12.3` | NIST CSF: `PR.NW`

---

## Control Details
Detailed Description:
Egress filtering is a security practice that monitors and controls outbound network traffic by examining data packets at network boundaries like firewalls or routers. Implementing strict filtering involves a default-deny stance where all outbound traffic is blocked unless it matches specific, authorized business rules, such as allowing only necessary ports like 80 (HTTP), 443 (HTTPS), or 53 (DNS) to known destinations. This stops command-and-control (C2) callbacks by preventing compromised internal systems from establishing communication channels with an attacker's external infrastructure, effectively neutralizing the attacker's ability to issue commands or exfiltrate data.

Why AI Compounds Risk:
AI exacerbates this risk by acting as a stealthy intermediary for C2 communications, a technique known as AI as a C2 Proxy. Attackers can prompt legitimate, trusted AI platforms to retrieve content from malicious URLs and return instructions within the AI's response, making malicious traffic blend in with normal HTTPS interactions with trusted services. This creates background noise that traditional network defenses often fail to detect, as the malware never contacts the attacker's infrastructure directly.

Examples:
1. Implement Application Layer Filtering using Deep Packet Inspection (DPI) to analyze the content of outbound packets, ensuring they conform to allowed protocols and detecting protocol tunneling.
2. Configure a Default-Deny policy on all network gateways and firewall appliances, explicitly permitting only essential services and ports required for business operations.
3. Route outbound web traffic through a Network Firewall or proxy server configured with strict domain allow lists and TLS interception to inspect encrypted traffic for suspicious data flows.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
