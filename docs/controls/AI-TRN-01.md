# AI-TRN-01: Enforce Default-Deny Inbound Policies at the transport layer

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 4: Transport  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `12.2, 12.3` | NIST CSF: `PR.NW`

---

## Control Details
Detailed Description:
Default-deny at the transport layer is a security framework where all inbound network traffic is blocked by default unless it matches a specific, predefined rule that explicitly allows it. Operating on a positive security model or whitelist approach, it ensures that only approved ports, protocols, and source IP addresses can interact with the network, thereby minimizing the attack surface and preventing unauthorized access from unknown threats.

Why AI Compounds Risk:
AI exacerbates network risks because AI models and their supporting infrastructure create expansive, non-static attack surfaces that are difficult to baseline with traditional security. Threat actors can use AI to automate the discovery of open ports or misconfigured rules, and the integration of third-party AI APIs often introduces hidden data dependencies and undeclared consumers that can be exploited if inbound traffic is not strictly controlled.

Examples:
1. Configure corporate firewalls and next-generation firewalls (NGFWs) with a final cleanup rule that explicitly denies all traffic not previously matched by a specific business-allowance rule.
2. Implement micro-segmentation within data centers or cloud environments to divide the network into isolated zones, applying default-deny policies to prevent lateral movement between sensitive AI training clusters and general user segments.
3. Deploy container orchestration network policies in containerized environments that use an empty podSelector to deny all ingress traffic to pods by default, requiring developers to explicitly define and document every necessary communication path.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
