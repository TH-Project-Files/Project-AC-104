# AI-DET-01: Implement AI-specific detections and SOAR playbooks (prompt injection, agent/tool abuse, data exfil via AI, connector compromise)

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 0: Governance & System Controls (Detection & Response)  
**Implementation Group:** IG 2  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `13.1, 13.2` | NIST CSF: `DE.AE, RS.MI`

---

## Control Details
Detailed Description:
Develop and deploy specialized detection rules within your SIEM/XDR and automated playbooks within your SOAR platform that are specifically tuned for AI-related threat vectors. This includes continuous monitoring and automated response mechanisms for LLM prompt injections, autonomous agent/tool abuse, data exfiltration through AI APIs, and the compromise of third-party AI connectors.

Minimum Telemetry Sources for AI Detections:
- LLM application gateway logs (or CASB/Proxy logs for external SaaS models)
- OAuth app governance and consent logs
- Identity Provider (IdP) risk and anomaly events
- EDR and DLP telemetry
- DNS and Secure Web Gateway (SWG) logs

Containment Primitives (SOAR Playbook Actions):
To operationalize the response, playbooks should be built around reusable containment primitives:
- Revoke compromised tokens
- Disable rogue or vulnerable OAuth applications
- Block destination categories or malicious domains
- Quarantine phishing or malicious mailbox messages
- Disable specific non-human/agent identities
- Rotate exposed secrets
- Isolate affected endpoints

Why AI Compounds Risk:
Traditional detection rules are designed for standard malware, lateral movement, or SQL injections; they fail to recognize the unique signatures of AI-centric attacks, such as semantic manipulation (prompt injection) or an autonomous agent chaining together authorized API calls in an unauthorized manner. Without AI-specific detections and machine-speed SOAR playbooks, an attacker can hijack an LLM or AI agent to extract sensitive data or pivot into internal networks long before a human analyst identifies the anomalous pattern.

Examples:
1. Ingest AI application gateway logs into the SIEM and write correlation rules to detect high-volume, repetitive, or anomalous prompt structures indicative of a prompt injection or jailbreak attempt.
2. Create a SOAR playbook that automatically isolates an AI agent or revokes its API keys if it begins exhibiting "tool-use drift" (e.g., calling a database query tool it rarely uses or attempting an excessive number of unapproved external web connections).
3. Monitor network egress for sudden spikes in data transfer to known public AI endpoints (e.g., OpenAI, Anthropic APIs) and trigger an automated SOAR response to block the connection and alert the security team of potential AI-driven data exfiltration.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
