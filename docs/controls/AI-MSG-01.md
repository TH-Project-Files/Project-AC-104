# AI-MSG-01: Deploy Anomalous Attachment & Rare File Type Filtering to block unusual containers (e.g., ISO, IMG) used by AI-automated malware delivery.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 6: Messaging/Web  
**Implementation Group:** IG 2  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `9.1, 9.2` | NIST CSF: `PR.IR`

---

## Control Details
Detailed Description:
Deploying anomalous attachment and rare file type filtering involves configuring email gateways and security agents to identify and block file extensions that are not typical for daily business operations, such as ISO, IMG, or VHD, which are frequently used to wrap and deliver malicious payloads while evading standard scanners.

Why AI Compounds Risk:
AI exacerbates this risk by enabling threat actors to automate the creation of polymorphic malware that changes its code structure every few seconds, allowing it to bypass signature-based detection and use these rare container files to hide its intent until execution.

Examples:
1. Use enterprise cloud email providers or similar mail flow rules to create a block-list for specific extensions like .iso, .img, .vhd, and .cab to prevent them from reaching user inboxes.
2. Configure advanced email security solutions that use machine learning to establish a baseline of normal sender behavior and flag any attachments that deviate from the established organizational norm.
3. Deploy endpoint protection platforms that utilize behavioral monitoring to detect and block the mounting or execution of unusual file types in real-time, regardless of whether the file hash is known to be malicious.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
