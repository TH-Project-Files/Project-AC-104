# AI-USR-11: Develop/deploy an in-house tool to send One-Time Codes (OTCs) to pre-determined personal cellphones or personal emails to out-of-band verify high-risk requests.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: User Facing Controls  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `6.1` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
This recommendation involves creating an internal system to verify high-risk actions—such as large financial transfers or sensitive data access—by sending a unique, short-lived code to a user's pre-registered personal device or email. This creates an out-of-band (OOB) authentication layer, meaning the verification occurs over a completely separate communication channel from the one used to initiate the request, effectively preventing unauthorized access even if primary credentials are stolen.

Why AI Compounds Risk:
AI exacerbates these risks by enabling attackers to conduct sophisticated social engineering and deepfake attacks at scale. Generative AI can mimic a target's voice or writing style to bypass traditional identity checks, making it easier for fraudsters to pose as executives or authorized personnel when submitting high-risk requests.

Examples:
1. High-Value Financial Transfers: Implement a mandatory OTC check for any wire transfer exceeding a specific threshold, where the employee must enter a code sent to their personal mobile device before the transaction is queued for final approval.
2. Privileged Access Management: Require OOB verification for IT administrators attempting to access critical infrastructure or modify global security settings, ensuring that a compromised workstation alone cannot be used to take over the network.
3. Sensitive Data Exports: Integrate the OTC tool with Data Loss Prevention (DLP) systems to trigger a verification code whenever a user attempts to download or email large volumes of proprietary or regulated data to an external destination.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
