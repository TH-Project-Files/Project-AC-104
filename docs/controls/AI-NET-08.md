# AI-NET-08: Enforce gateway-only egress for AI model providers by blocking direct API access from general subnets at the firewall and SWG.

**Category:** Networking (Layer 3: Network)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 13.1, 13.2  
**NIST CSF Subcategories:** PR.AA, PR.PS  
**Layered with:** AI-APP-10 (the centralized AI Gateway this control makes unbypassable), AI-NET-02 (general default-deny egress filtering), AI-GOV-03 (the approved AI service catalog these routing rules enforce)  

## Details
Detailed Description:
Ensure that all outbound network traffic to external AI model providers (e.g., api.openai.com, anthropic.com) is strictly forced through the centralized AI Gateway. This requires configuring egress firewalls, Secure Web Gateways (SWG), and DNS policies to explicitly deny direct API access from general corporate subnets, developer endpoints, and unapproved servers.

Why AI Compounds Risk:
An AI Gateway (AI-APP-10) is only an effective chokepoint if traffic cannot bypass it. In real-world environments, developers and rogue applications frequently attempt to call external AI APIs directly using keys stored on their local laptops or in CI pipelines. If the network permits these direct outbound connections, it creates "Shadow AI" integrations that completely bypass the organization's prompt redaction, DLP layers, and centralized logging, leading to invisible data exfiltration and compliance violations.

Examples:
1. Configure the egress firewall or SWG to explicitly deny direct access to known AI model provider API domains/IPs from all general subnets, allowing egress only from the dedicated AI Gateway IP addresses.
2. Utilize CASB/SWG category controls to separate browser-based AI tool usage from programmatic API usage, applying strict routing rules to the latter.
3. Combine network restrictions with identity controls by refusing to distribute long-lived provider keys to individuals; instead, require workloads to authenticate via short-lived tokens minted by the gateway or federation.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
