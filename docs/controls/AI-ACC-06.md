# AI-ACC-06: Implement Context-Aware Authentication (e.g. typing cadence, location)

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `6.1, 6.8` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Context-aware authentication is a security method that evaluates real-time situational factors—such as user location, device health, time of access, and behavioral patterns like typing cadence—to determine the legitimacy of a login attempt. Unlike traditional static credentials, it uses a risk-based engine to dynamically grant seamless access for low-risk behavior or require additional verification (step-up authentication) when anomalies are detected.

Why AI Compounds Risk:
AI exacerbates authentication risks by enabling cybercriminals to launch sophisticated, automated attacks at scale, such as using generative AI to create realistic deepfakes for social engineering or utilizing machine learning to bypass traditional bot detection and execute high-speed credential stuffing.

Examples:
1. To implement this in a corporate environment, start by defining granular access policies that require multi-factor authentication (MFA) or block access entirely when employees attempt to reach sensitive financial systems from unrecognized geographic locations or unmanaged personal devices.
2. Integrate a risk-analysis engine that uses machine learning to establish a behavioral baseline for each employee, such as their typical working hours and network types, so the system can automatically flag and challenge "impossible travel" scenarios or logins occurring at highly unusual times.
3. Deploy continuous access evaluation (CAEP) across the identity stack to monitor active sessions in real-time; if a device's security posture changes—such as an antivirus being disabled or a switch to an unsecured public Wi-Fi—the system can immediately revoke access or trigger a re-authentication prompt.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
