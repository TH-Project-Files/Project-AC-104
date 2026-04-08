# AI-DLK-03: Implement Zero-Trust segmentation to prevent lateral movement

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 2: Data Link  
**Implementation Group:** IG 3  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `12.1, 13.4` | NIST CSF: `PR.NW, DE.CM`

---

## Control Details
Detailed Description:
Zero-Trust segmentation, or microsegmentation, divides a network into small, isolated zones to stop threats from spreading laterally by requiring strict identity verification and authorization for every access request, regardless of whether the user is inside or outside the network perimeter.

Why AI Compounds Risk:
AI exacerbates lateral movement risk by enabling attackers to automate discovery, operate in parallel, and compress attack timelines from months to minutes, allowing them to exploit vulnerabilities and move through a network faster than traditional security teams can react.

Examples:
1. Use software-defined networking (SDN) or next-generation firewalls (NGFW) to create granular micro-perimeters around specific application workloads, ensuring that a breach in one zone does not grant access to others.
2. Implement identity-based access control and multi-factor authentication (MFA) to verify the authenticity of every digital interaction based on user identity and device posture rather than static network location.
3. Deploy AI-powered segmentation platforms to automatically discover application behaviors and generate precise, real-time security policies that adapt as cloud and hybrid environments grow.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
