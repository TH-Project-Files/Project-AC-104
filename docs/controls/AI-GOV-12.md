# AI-GOV-12: Deploy targeted deepfake and synthetic media detection tooling for high-risk workflows (rather than an org-wide mandate)

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: Governance & System Controls  
**Implementation Group:** IG 3  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `14.1, 17.1` | NIST CSF: `PR.AT, RS.MA`

---

## Control Details
Detailed Description:
Implement deepfake and synthetic media detection tooling for targeted, high-risk workflows (e.g., executive communications, high-value financial transfers, and high-privilege helpdesk requests). *Maturity Note:* This is designed as a targeted, localized control rather than an organization-wide mandate; a mature organization focuses this tooling specifically where synthetic media poses the highest fraud or reputational risk.

Why AI Compounds Risk:
Generative AI allows threat actors to clone voices (audio deepfakes) with just a few seconds of sample audio, and generate highly convincing synthetic video of key personnel. This technology is actively used to bypass helpdesk voice verification, authorize fraudulent wire transfers (Business Email Compromise via voice/video), and fabricate executive statements for extortion or market manipulation. Because humans can no longer reliably distinguish high-quality deepfakes from reality, specialized technical detection is required for critical validation checkpoints.

Examples:
1. Deploy specialized deepfake and liveness detection software for the IT helpdesk to use when verifying identity for high-privilege account resets or MFA bypass requests.
2. Integrate third-party deepfake analysis APIs into the financial approval workflow to automatically scan voicemail, recorded requests, or teleconferencing streams for synthetic artifacts before processing high-value wire transfers.
3. Establish an incident response playbook that includes access to a specialized digital forensics service or a commercial deepfake-detection platform, enabling PR and Legal teams to rapidly verify the authenticity of suspicious media during a brand crisis.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
