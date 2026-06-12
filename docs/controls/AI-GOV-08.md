# AI-GOV-08: Establish OAuth Application and Consent-Grant Governance to restrict third-party 'AI Productivity' apps and defend against consent phishing and rogue app registrations.

**Category:** Governance & People (Layer 0: Governance & System Controls)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 9.1, 9.2  
**NIST CSF Subcategories:** PR.IR  
**Layered with:** AI-NHI-01 (OAuth tokens and app identities belong in the non-human identity inventory), AI-DET-01 (consent logs are a required telemetry source, and "disable rogue OAuth applications" is one of its containment primitives), AI-GOV-03 (the approved AI service catalog consent policies enforce)

---

## Details
Detailed Description:
Implement a centralized management framework to monitor and control third-party applications that use OAuth tokens to access corporate data environments like enterprise productivity suites. This governance must cover the full consent-grant attack lifecycle, not just app inventory: consent phishing (tricking a user into authorizing a malicious app, giving the attacker durable token access without ever touching a password), rogue application registrations used for post-breach persistence, and stale or over-scoped grants that outlive their original purpose.

Why AI Compounds Risk:
AI productivity tools operate autonomously, consuming, summarizing, and moving vast amounts of data across integrated SaaS platforms without constant human oversight — a persistent AI integration with overprivileged permissions can quietly exfiltrate thousands of records daily through legitimate but unmonitored API connections. The consent-grant path compounds this: attackers now use AI to mass-produce convincing fake "AI assistant" apps and consent-phishing lures, and a single granted token bypasses MFA, password resets, and most account-takeover defenses because the access is technically authorized.

Examples:
1. Enable the App Governance feature within the enterprise endpoint protection platform for Cloud Apps to gain deep visibility into OAuth-enabled app behaviors and automated response capabilities
2. Establish custom governance policies that automatically revoke access for stale applications or those showing anomalous data transfer patterns and unauthorized permission changes
3. Restrict self-service user consent to ensure only qualified administrators can authorize new AI integrations after a thorough security review of the requested scopes and publisher reputation
4. Alert on and auto-quarantine new app registrations and consent grants matching high-risk patterns — unverified publishers, lookalike "AI assistant" names, or broad scopes such as full mailbox read, files read/write, and offline access — and feed these events into the AI-DET-01 detection pipeline
5. Run a recurring (e.g., quarterly) recertification of all active OAuth grants, requiring business owners to re-justify each AI integration's scopes and automatically revoking grants that go unattested

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
