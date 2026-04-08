# AI-NET-03: Configure firewall and DNS filtering blocklists to automatically drop traffic to Newly Registered and Parked Domains

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 3: Network  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `4.4, 12.3` | NIST CSF: `PR.NW`

---

## Control Details
Detailed Description:
Recommendation Explanation: This security measure involves configuring network defenses to automatically block connections to domains that have been recently registered (typically within the last 30 days) or are currently "parked" (registered but not yet hosting an active website). These domains are high-risk because they lack a historical reputation and are frequently used by threat actors to launch short-lived phishing campaigns, host malware, or act as command-and-control servers before they can be identified and blacklisted by traditional security feeds.

Why AI Compounds Risk:
AI Risk Exacerbation: Generative AI allows attackers to programmatically register and set up thousands of brand-adjacent domains at a scale and speed that overwhelms manual monitoring. AI can also instantly generate realistic, localized website content and phishing lures for these new domains, making them appear legitimate to users and traditional detectors while maintaining a clean reputation long enough to execute a breach.

Examples:
1. Point corporate DNS settings to a cloud-based DNS filtering provider that utilizes AI-driven threat intelligence to categorize and block the Newly Registered Domains (NRD) category by default.
2. Integrate a real-time NRD database feed into the corporate firewall's security services to automatically update blocklists and drop all outbound traffic directed to domains registered within a specific timeframe, such as the last 30 days.
3. Deploy endpoint security agents on remote devices that enforce DNS filtering policies, ensuring that traffic to parked or brand-new domains is blocked even when employees are working off-site and not protected by the office perimeter firewall.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
