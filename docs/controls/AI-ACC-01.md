# AI-ACC-01: Enforce Aggressive Absolute & Idle Timeouts on sensitive apps

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `6.1, 6.8` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Recommendation Explanation: Enforcing aggressive absolute and idle timeouts involves setting strict time limits on how long a user session can remain active. Idle timeouts terminate a session after a brief period of inactivity to prevent unauthorized access to an unattended device, while absolute timeouts force a re-authentication after a fixed total duration, regardless of activity, to mitigate the risk of long-lived session hijacking.

Why AI Compounds Risk:
AI Risk Exacerbation: The rise of AI increases the risk of "silent" burnout and "brain fry," where employees may leave sensitive sessions open while distracted by complex multitasking or "work snacks" during breaks. Furthermore, automated AI agents and "vibe-coding" can lead to rapid, high-volume data processing that, if left unchecked by session limits, could allow a compromised account to exfiltrate massive amounts of sensitive data before the breach is detected.

Examples:
1. Corporate Implementation Examples:
2. Configure Identity Provider (IdP) policies to trigger a 15-minute idle timeout and an 8-hour absolute timeout for all users accessing internal generative AI platforms or sensitive financial databases.
3. Implement conditional access rules that enforce "aggressive aging" timeouts on Security Gateways, automatically shortening session durations when system memory or connection tables reach a high-risk threshold like 80% capacity.
4. Use mobile device management (MDM) to enforce strict screen-lock timeouts and re-authentication requirements for any corporate application that processes proprietary AI training data or sensitive intellectual property.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
