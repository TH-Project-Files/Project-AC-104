# AI-USR-02: Enforce Targeted Impersonation Protection for High-Value Targets (VIPs) to detect subtle visual or character-based spoofing of key personnel names.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: User Facing Controls  
**Implementation Group:** IG 1  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `9.1, 9.2` | NIST CSF: `PR.IR`

---

## Control Details
Detailed Description:
Targeted Impersonation Protection for High-Value Targets (VIPs) is a specialized security layer designed to protect executives and key personnel from sophisticated phishing attacks. It uses advanced detection algorithms to identify subtle visual or character-based spoofing, such as "lookalike" domains or "homoglyphs" where characters from different alphabets are used to mimic legitimate names and email addresses.

Why AI Compounds Risk:
AI exacerbates this risk by enabling attackers to automate the creation of highly convincing, personalized, and error-free impersonation attempts at scale. Generative AI can mimic the specific writing style, tone, and professional vocabulary of a VIP, making it nearly impossible for traditional filters or human observation to detect the fraud based on language alone.

Examples:
1. Configure "Executive Protection" policies in email security gateways (like a secure email gateway or an enterprise endpoint protection platform) by inputting the specific display names of VIPs and setting the system to flag any external emails that use those names or slight variations of them.
2. Implement advanced domain monitoring services that use behavioral AI to scan for the registration of lookalike domains (e.g., using a "0" instead of an "o") and automatically block or quarantine communications from these unauthorized sources.
3. Deploy mailbox intelligence and anti-phishing safety tips that provide real-time visual warnings to employees when an email address includes unexpected characters or appears similar to a known internal contact but originates from an external sender.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
