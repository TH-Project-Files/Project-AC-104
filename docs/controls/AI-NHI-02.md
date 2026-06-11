# AI-NHI-02: Enforce Cryptographic and Hardware-Backed Identities (e.g., TPMs, HSMs) for production AI agents.

**Category:** Identity & Access (Layer 0: Governance & System Controls)  
**Implementation Group:** IG 3  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 5.1, 5.2, 16.1  
**NIST CSF Subcategories:** PR.AA  

## Details
Detailed Description:
Assign persistent, cryptographically rooted identifiers to all agent workloads. For production and high-risk agents, bind authentication material to hardware security modules (HSMs), trusted platform modules (TPMs), or confidential computing enclaves.

Why AI Compounds Risk:
Mitigations based on friction (e.g., complex passwords, IP restrictions) degrade significantly against an adversary that can grind through tedious steps at scale using AI. If an agent's host is compromised, hardware-bound credentials ensure the attacker cannot simply exfiltrate a static token from a configuration file to impersonate the agent elsewhere.

Examples:
1. Issue X.509 certificates to each agent and require mutual TLS (mTLS) with certificate pinning for all service connections.
2. Implement remote attestation to verify an agent's execution environment integrity before granting it access to backend databases.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
