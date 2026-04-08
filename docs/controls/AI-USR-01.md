# AI-USR-01: Enable Automated 'First Contact' Safety Tips to warn users when interacting with new or anomalous external senders often used by AI phishing bots.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: User Facing Controls  
**Implementation Group:** IG 1  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `9.1, 9.2` | NIST CSF: `PR.IR`

---

## Control Details
Detailed Description:
First-contact safety tips are automated visual alerts that appear in an email client when a user receives a message from a sender they do not regularly communicate with or who appears anomalous. These tips serve as a "speed bump," prompting users to verify the identity of the sender and the legitimacy of the content before clicking links or downloading attachments.

Why AI Compounds Risk:
AI exacerbates this risk by enabling attackers to generate highly personalized, grammatically perfect, and contextually relevant phishing emails at scale. These AI-generated messages can mimic a specific professional tone or reference real-world business transactions, making it significantly harder for traditional filters and human observation to detect spoofing or social engineering.

Examples:
1. Enable impersonation protection and mailbox intelligence within the enterprise email security platform to automatically flag external senders with display names similar to internal executives.
2. Configure mail flow rules in the email admin center to prepend a warning banner to any email originating from a domain that has not previously exchanged mail with the organization.
3. Deploy a third-party email security gateway that uses machine learning to analyze communication patterns and inject real-time "untrusted sender" warnings into the body of suspicious external messages.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
