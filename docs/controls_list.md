# Argus Centurion Master Control List

This table provides a high-level overview of the 103 controls within the AC-104 baseline. 

| ID | Group | Description | Category |
|---|---|---|---|
| [AI-VND-02](controls/AI-VND-02.md) | **IG 1** | Enforce AI vendor minimum security terms, explicitly mandating "no training on customer data," strict tenancy, and guaranteed log access. | Layer 0: Governance & System Controls |
| [AI-GOV-01](controls/AI-GOV-01.md) | **IG 1** | Establish and enforce a Generative AI Acceptable Use Policy | Layer 0: Governance & System Controls |
| [AI-GOV-02](controls/AI-GOV-02.md) | **IG 1** | Implement rigorous Data Classification Mapping and System Agnostic Coverage Policies | Layer 0: Governance & System Controls |
| [AI-GOV-03](controls/AI-GOV-03.md) | **IG 1** | Establish an Approved AI Service Catalog and enforce it via web proxies/CASB, explicitly limiting employee access to only vetted and sanctioned AI tools. | Layer 0: Governance & System Controls |
| [AI-GOV-04](controls/AI-GOV-04.md) | **IG 2** | Implement Continuous Session Risk Monitoring (e.g., 'impossible travel') to detect and automatically revoke session tokens hijacked by AI-automated scripts. | Layer 0: Governance & System Controls |
| [AI-GOV-08](controls/AI-GOV-08.md) | **IG 2** | Establish OAuth Application Governance to restrict third-party 'AI Productivity' apps from accessing sensitive mailbox or cloud storage data. | Layer 0: Governance & System Controls |
| [AI-NHI-01](controls/AI-NHI-01.md) | **IG 2** | Establish Non-Human Identity (NHI) Inventory and Governance (service accounts, API keys, tokens, agent identities) | Layer 0: Governance & System Controls |
| [AI-GOV-09](controls/AI-GOV-09.md) | **IG 2** | Establish a Deepfake/Voice Clone Executive Protection Protocol | Layer 0: Governance & System Controls |
| [AI-GOV-10](controls/AI-GOV-10.md) | **IG 2** | Require AI Vendor Risk Assessments for all new software purchases | Layer 0: Governance & System Controls |
| [AI-GOV-11](controls/AI-GOV-11.md) | **IG 2** | Develop an AI-specific Incident Response Playbook | Layer 0: Governance & System Controls |
| [AI-GOV-16](controls/AI-GOV-16.md) | **IG 2** | Establish AI-specific change management and evaluation gates requiring regression testing, approvals, and rollback plans for updates to models, prompts, agent tools, or RAG datasets. | Layer 0: Governance & System Controls |
| [AI-GOV-12](controls/AI-GOV-12.md) | **IG 3** | Deploy targeted deepfake and synthetic media detection tooling for high-risk workflows (rather than an org-wide mandate) | Layer 0: Governance & System Controls |
| [AI-GOV-13](controls/AI-GOV-13.md) | **IG 3** | Conduct Continuous Red Teaming against AI defenses | Layer 0: Governance & System Controls |
| [AI-GOV-14](controls/AI-GOV-14.md) | **IG 3** | Implement Cryptographic Provenance (e.g., C2PA standards) for all official university executive media to establish verifiable digital trust. | Layer 0: Governance & System Controls |
| [AI-GOV-15](controls/AI-GOV-15.md) | **IG 3** | Deploy AI-Driven Behavioral Analytics (UEBA) for baseline anomaly detection | Layer 0: Governance & System Controls |
| [AI-DET-01](controls/AI-DET-01.md) | **IG 2** | Implement AI-specific detections and SOAR playbooks (prompt injection, agent/tool abuse, data exfil via AI, connector compromise) | Layer 0: Governance & System Controls (Detection & Response) |
| [AI-USR-01](controls/AI-USR-01.md) | **IG 1** | Enable Automated 'First Contact' Safety Tips to warn users when interacting with new or anomalous external senders often used by AI phishing bots. | Layer 0: User Facing Controls |
| [AI-USR-02](controls/AI-USR-02.md) | **IG 1** | Enforce Targeted Impersonation Protection for High-Value Targets (VIPs) to detect subtle visual or character-based spoofing of key personnel names. | Layer 0: User Facing Controls |
| [AI-USR-03](controls/AI-USR-03.md) | **IG 1** | Advanced AI Phishing Simulations: Update Security Awareness Training to include simulations specifically mimicking high-quality, multilingual LLM-generated phishing models. | Layer 0: User Facing Controls |
| [AI-USR-04](controls/AI-USR-04.md) | **IG 1** | Implement Executive Challenge-Response Protocols (e.g., pre-established safe words) for urgent voice/video requests. | Layer 0: User Facing Controls |
| [AI-USR-05](controls/AI-USR-05.md) | **IG 1** | Conduct Deepfake-Specific Awareness Training focusing on 'liveness' checks (e.g., asking callers to turn their head) and audio/visual artifact detection. | Layer 0: User Facing Controls |
| [AI-USR-06](controls/AI-USR-06.md) | **IG 1** | Train staff on Reverse-Turing Tests to detect AI bots in chat/email | Layer 0: User Facing Controls |
| [AI-USR-07](controls/AI-USR-07.md) | **IG 1** | Deploy an Automated Incident Reporting Button to instantly quarantine suspected AI phishing | Layer 0: User Facing Controls |
| [AI-USR-08](controls/AI-USR-08.md) | **IG 1** | Mandate Phishing-Resistant MFA (FIDO2/WebAuthn) to neutralize credential harvesting | Layer 0: User Facing Controls |
| [AI-USR-09](controls/AI-USR-09.md) | **IG 2** | Implement Out-of-Band/Verbal Verification for high-risk financial/data actions | Layer 0: User Facing Controls |
| [AI-USR-10](controls/AI-USR-10.md) | **IG 2** | Replace annual training with Contextual Security Nudges at the point of click | Layer 0: User Facing Controls |
| [AI-USR-11](controls/AI-USR-11.md) | **IG 2** | Develop/deploy an in-house tool to send One-Time Codes (OTCs) to pre-determined personal cellphones or personal emails to out-of-band verify high-risk requests. | Layer 0: User Facing Controls |
| [AI-DLK-03](controls/AI-DLK-03.md) | **IG 3** | Implement Zero-Trust segmentation to prevent lateral movement | Layer 2: Data Link |
| [AI-DLK-04](controls/AI-DLK-04.md) | **IG 3** | Utilize AI Network Baseline Monitoring to detect anomalous network traffic patterns and alert on them | Layer 2: Data Link |
| [AI-NET-01](controls/AI-NET-01.md) | **IG 1** | Mandate enterprise Secure Recursive DNS with encrypted lookups (DoH/DoT) backed by real-time “big data” threat intelligence to block malicious domains and resist DNS spoofing/hijacking | Layer 3: Network |
| [AI-NET-02](controls/AI-NET-02.md) | **IG 1** | Implement Strict Egress Filtering to stop C2 callbacks | Layer 3: Network |
| [AI-NET-03](controls/AI-NET-03.md) | **IG 1** | Configure firewall and DNS filtering blocklists to automatically drop traffic to Newly Registered and Parked Domains | Layer 3: Network |
| [AI-NET-08](controls/AI-NET-08.md) | **IG 2** | Enforce gateway-only egress for AI model providers by blocking direct API access from general subnets at the firewall and SWG. | Layer 3: Network |
| [AI-NET-04](controls/AI-NET-04.md) | **IG 2** | Upgrade to AI-Enhanced Next-Gen Firewalls (NGFW) for behavioral and realtime threat blocking | Layer 3: Network |
| [AI-NET-05](controls/AI-NET-05.md) | **IG 2** | Run Continuous Attack Surface Management (ASM) scans | Layer 3: Network |
| [AI-NET-06](controls/AI-NET-06.md) | **IG 2** | Implement automated threat intelligence feeds from big data sources (e.g., large-scale MDR providers or crowd-sourced intelligence) to proactively block emerging AI-driven attacker infrastructure. | Layer 3: Network |
| [AI-NET-07](controls/AI-NET-07.md) | **IG 3** | Enable hardware-accelerated Deep Learning (DL) on Next-Generation Firewalls (NGFW) for inline threat detection | Layer 3: Network |
| [AI-NET-08](controls/AI-NET-08.md) | **IG 3** | Monitor BGP with Automated Route Hijacking Detection | Layer 3: Network |
| [AI-LOG-01](controls/AI-LOG-01.md) | **IG 1** | Establish policies and controls for AI prompt/chat retention, privacy masking, and strict access management for observability logs. | Layer 4: Data |
| [AI-RAG-01](controls/AI-RAG-01.md) | **IG 2** | Implement RAG authorization enforcement and security trimming to ensure AI only synthesizes data the user is permitted to see. | Layer 4: Data |
| [AI-TRN-01](controls/AI-TRN-01.md) | **IG 1** | Enforce Default-Deny Inbound Policies at the transport layer | Layer 4: Transport |
| [AI-TRN-02](controls/AI-TRN-02.md) | **IG 2** | Apply Intelligent Rate Limiting against high-speed port scans | Layer 4: Transport |
| [AI-TRN-03](controls/AI-TRN-03.md) | **IG 3** | Use Deep Packet Inspection (DPI) to identify mis-ported traffic | Layer 4: Transport |
| [AI-TRN-04](controls/AI-TRN-04.md) | **IG 3** | Deploy Stateful Protocol Anomaly Detection (IPS) | Layer 4: Transport |
| [AI-AUTH-01](controls/AI-AUTH-01.md) | **IG 1** | Require possession factor before password factor in sign-on to limit brute force password compromise. | Layer 5: Access Session |
| [AI-ACC-01](controls/AI-ACC-01.md) | **IG 1** | Enforce Aggressive Absolute & Idle Timeouts on sensitive apps | Layer 5: Access Session |
| [AI-ACC-02](controls/AI-ACC-02.md) | **IG 1** | Implement Concurrent Login Restrictions | Layer 5: Access Session |
| [AI-AUTH-02](controls/AI-AUTH-02.md) | **IG 1** | Require advanced CAPTCHA on password reset requests to prevent automated abuse. | Layer 5: Access Session |
| [AI-AUTH-03](controls/AI-AUTH-03.md) | **IG 1** | Enable immediate, un-mutable out-of-band notifications for all critical account changes (e.g., password reset, MFA device addition). | Layer 5: Access Session |
| [AI-AUTH-04](controls/AI-AUTH-04.md) | **IG 1** | Enable user enumeration prevention for authentication and account recovery workflows to obscure account existence. | Layer 5: Access Session |
| [AI-ACC-03](controls/AI-ACC-03.md) | **IG 2** | Enforce Aggressive Token Rotation: Implement automated rotation for all privileged credentials and shorten session token lifetimes to neutralize the persistence of AI-generated infostealers. | Layer 5: Access Session |
| [AI-PAM-01](controls/AI-PAM-01.md) | **IG 2** | Implement Privileged Access Management (PAM) with Just-In-Time (JIT) elevation for privileged actions by humans and AI agents | Layer 5: Access Session |
| [AI-ACC-08](controls/AI-ACC-08.md) | **IG 2** | Enforce managed-device and continuous device posture checks as a prerequisite for accessing sensitive applications and enterprise AI tools. | Layer 5: Access Session |
| [AI-ACC-04](controls/AI-ACC-04.md) | **IG 2** | Automate Impossible Travel Detection and block concurrent logins from separate regions | Layer 5: Access Session |
| [AI-ACC-05](controls/AI-ACC-05.md) | **IG 2** | Configure Automated Session Invalidation upon risk detection | Layer 5: Access Session |
| [AI-ACC-06](controls/AI-ACC-06.md) | **IG 2** | Implement Context-Aware Authentication (e.g. typing cadence, location) | Layer 5: Access Session |
| [AI-AUTH-05](controls/AI-AUTH-05.md) | **IG 2** | Monitor external threat intelligence and dark web sources for compromised employee credentials, and enforce automated password resets for exposed accounts. | Layer 5: Access Session |
| [AI-ACC-07](controls/AI-ACC-07.md) | **IG 3** | Enable device-bound/session-bound token protections (where supported) to reduce replay of stolen session tokens | Layer 5: Access Session |
| [AI-END-01](controls/AI-END-01.md) | **IG 1** | Harden Script Execution: Restrict script execution (PowerShell/Python/JS) to only digitally signed scripts and enforce allowlists for trusted script paths to block AI-generated droppers. | Layer 6: Endpoint Presentation |
| [AI-END-02](controls/AI-END-02.md) | **IG 1** | Automate Macro and Script Disablement for non-admin users | Layer 6: Endpoint Presentation |
| [AI-END-03](controls/AI-END-03.md) | **IG 1** | Enforce Automated Patch Management for OS and 3rd-party apps | Layer 6: Endpoint Presentation |
| [AI-END-04](controls/AI-END-04.md) | **IG 2** | Deploy Advanced Behavioral Telemetry: Implement high-fidelity logging (e.g. Sysmon-style) to capture process creation and network connections used by AI-assisted malware that evades signature-based AV. | Layer 6: Endpoint Presentation |
| [AI-END-05](controls/AI-END-05.md) | **IG 2** | Remove or highly manage local admin and installation rights | Layer 6: Endpoint Presentation |
| [AI-END-06](controls/AI-END-06.md) | **IG 2** | Deploy AI-Driven EDR/XDR for behavioral process termination | Layer 6: Endpoint Presentation |
| [AI-END-07](controls/AI-END-07.md) | **IG 2** | Utilize File Integrity Monitoring (FIM) for critical OS files | Layer 6: Endpoint Presentation |
| [AI-END-08](controls/AI-END-08.md) | **IG 3** | Deploy Data Loss Prevention (DLP) to monitor formatted file exfiltration | Layer 6: Endpoint Presentation |
| [AI-END-09](controls/AI-END-09.md) | **IG 3** | Configure Application Allow-listing to block untrusted executables | Layer 6: Endpoint Presentation |
| [AI-MSG-01](controls/AI-MSG-01.md) | **IG 2** | Deploy Anomalous Attachment & Rare File Type Filtering to block unusual containers (e.g., ISO, IMG) used by AI-automated malware delivery. | Layer 6: Messaging/Web |
| [AI-MSG-02](controls/AI-MSG-02.md) | **IG 2** | Implement Behavioral Mailbox Intelligence to baseline user communication patterns (tone, frequency, habits) and flag AI-generated anomalies. | Layer 6: Messaging/Web |
| [AI-MSG-03](controls/AI-MSG-03.md) | **IG 2** | Enforce Universal URL Unwrapping and deep link analysis for shortened or redirected URLs to reveal hidden AI-generated malicious destinations. | Layer 6: Messaging/Web |
| [AI-APP-11](controls/AI-APP-11.md) | **IG 1** | Establish a secrets management baseline for AI stacks, mandating centralized secrets managers and prohibiting hardcoded API keys in repos, notebooks, and prompt templates. | Layer 7: Application |
| [AI-AGT-01](controls/AI-AGT-01.md) | **IG 2** | Implement Agent tool-call governance through strict allowlists, schema validation, and human-in-the-loop approvals. | Layer 7: Application |
| [AI-APP-10](controls/AI-APP-10.md) | **IG 2** | Implement a centralized AI Gateway or Control Plane to broker, govern, and monitor all enterprise interactions with external LLMs and AI services. | Layer 7: Application |
| [AI-APP-01](controls/AI-APP-01.md) | **IG 1** | Enforce Strict Input Sanitization frameworks against AI fuzzing | Layer 7: General Usage & AppSec Defense |
| [AI-APP-02](controls/AI-APP-02.md) | **IG 1** | Monitor employee devices and networks to block the use of unsanctioned or hidden 'Shadow AI' apps. | Layer 7: General Usage & AppSec Defense |
| [AI-APP-03](controls/AI-APP-03.md) | **IG 2** | Deploy Advanced Bot Management (invisible or behavioral CAPTCHAs) | Layer 7: General Usage & AppSec Defense |
| [AI-APP-04](controls/AI-APP-04.md) | **IG 2** | Conduct regular OSINT gathering (e.g., Google Dorking) to discover shadow authentication portals or legacy logins for the domain, and secure them behind a VPN or firewall. | Layer 7: General Usage & AppSec Defense |
| [AI-APP-05](controls/AI-APP-05.md) | **IG 2** | Utilize a Behavioral Web Application Firewall (WAF) | Layer 7: General Usage & AppSec Defense |
| [AI-APP-06](controls/AI-APP-06.md) | **IG 3** | Implement API Security Gateways with strict rate limiting | Layer 7: General Usage & AppSec Defense |
| [AI-APP-07](controls/AI-APP-07.md) | **IG 3** | Integrate Dynamic Application Security Testing (DAST) into CI/CD | Layer 7: General Usage & AppSec Defense |
| [AI-APP-08](controls/AI-APP-08.md) | **IG 3** | Monitor 3rd-party connections via Cloud Application Security Broker (CASB) | Layer 7: General Usage & AppSec Defense |
| [AI-APP-09](controls/AI-APP-09.md) | **IG 3** | Scan your company's code repositories to automatically find and review code that was generated by AI. | Layer 7: General Usage & AppSec Defense |
| [AI-LLM-01](controls/AI-LLM-01.md) | **IG 1** | Put strict network filters around your internal AI models so hackers can't steal or copy the AI's core logic. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-02](controls/AI-LLM-02.md) | **IG 1** | Put speed limits on AI agents so they don't get stuck in endless loops or crash internal systems. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-03](controls/AI-LLM-03.md) | **IG 1** | Give AI agents only the bare minimum permissions needed to do their jobs. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-04](controls/AI-LLM-04.md) | **IG 1** | Keep detailed records of everything AI agents do, including the prompts they receive and actions they take. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-05](controls/AI-LLM-05.md) | **IG 2** | Test any fake (synthetic) or anonymized data to make sure hackers can't reverse-engineer it to find real people's identities. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-06](controls/AI-LLM-06.md) | **IG 2** | Ensure AI agents operate using the requesting user's own identity and access permissions (e.g., via OAuth/OIDC tokens) rather than relying on highly privileged, hard-coded service accounts or static API keys. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-07](controls/AI-LLM-07.md) | **IG 2** | Automatically scan and clean up the text users send to AI to stop them from sharing too much sensitive information. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-08](controls/AI-LLM-08.md) | **IG 2** | Require a human to review and approve any important or risky actions taken by AI. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-09](controls/AI-LLM-09.md) | **IG 2** | Create strict 'allow-lists' so AI agents can only talk to approved websites or internal systems. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-10](controls/AI-LLM-10.md) | **IG 2** | Thoroughly test and review the code and instructions for AI agents before letting them run in the real world. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-11](controls/AI-LLM-11.md) | **IG 2** | Continuously scan and classify sensitive company data so you know exactly what information AI tools might access. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-12](controls/AI-LLM-12.md) | **IG 2** | Put strict safety checks in place when letting AI talk directly to your company databases (like translating plain text into SQL queries). | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-13](controls/AI-LLM-13.md) | **IG 2** | Ensure that when AI tools talk to each other or use plugins, they prove who they are and only share the minimum necessary data. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-14](controls/AI-LLM-14.md) | **IG 2** | Set up alerts to notify security teams if an AI agent starts behaving unexpectedly or out-of-bounds. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-15](controls/AI-LLM-15.md) | **IG 2** | Protect the specialized databases that feed knowledge to your AI (Vector Stores) with encryption and strict access rules. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-16](controls/AI-LLM-16.md) | **IG 3** | Regularly test internal AI systems by having security teams pretend to be hackers (Red Teaming) to find weak spots. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-17](controls/AI-LLM-17.md) | **IG 3** | Force AI tools that write or run code to do so in a secure, isolated bubble (sandbox) so they can't break anything on the network. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-18](controls/AI-LLM-18.md) | **IG 3** | Keep different users' AI chats strictly separated so one person's data doesn't accidentally leak into another person's chat. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-19](controls/AI-LLM-19.md) | **IG 3** | Keep a 'nutrition label' (Bill of Materials) for your AI models and verify that no one has tampered with their code or plugins. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-20](controls/AI-LLM-20.md) | **IG 3** | Track exactly where your AI training data comes from to ensure hackers haven't poisoned it with malicious information. | Layer 7: Internal LLMs & Agentics |
| [AI-LLM-21](controls/AI-LLM-21.md) | **IG 3** | Install data loss prevention (DLP) tools to stop AI agents from accidentally or maliciously leaking sensitive company data. | Layer 7: Internal LLMs & Agentics |
