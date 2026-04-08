# AI-TRN-02: Apply Intelligent Rate Limiting against high-speed port scans

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 4: Transport  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `12.2, 12.3` | NIST CSF: `PR.NW`

---

## Control Details
Detailed Description:
Intelligent Rate Limiting against high-speed port scans is a dynamic security strategy that goes beyond static blocking by using algorithms to throttle or deny connection attempts that exceed a specific frequency. It monitors inbound traffic for patterns of rapid probing—where an attacker systematically checks multiple ports on one or more systems to identify open services—and automatically restricts the source to prevent resource exhaustion and reconnaissance.

Why AI Compounds Risk:
AI exacerbates this risk by enabling hackers to automate and accelerate the scanning process, reducing the window from vulnerability disclosure to exploitation to less than 48 hours or even minutes. AI-driven tools can also intelligently vary scan frequencies and sequences to mimic legitimate traffic, making traditional, static defense mechanisms less effective at distinguishing between benign network management and a malicious attack.

Examples:
1. Deploy AI-driven Network Detection and Response (NDR) solutions that use machine learning to establish a baseline of normal network behavior and automatically flag or block scanning patterns that deviate from that norm.
2. Configure Next-Generation Firewalls (NGFW) or API Gateways to implement "sliding window" or "token bucket" algorithms that cap the number of connection requests from a single IP address or geographic region within a specific timeframe.
3. Implement automated incident response playbooks that trigger an immediate block on source IPs or service accounts when they exceed high-confidence thresholds for failed connection attempts or sequential port probes.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
