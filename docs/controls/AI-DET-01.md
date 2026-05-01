# AI-DET-01

**Category:** Layer 0: Governance & System Controls (Detection & Response)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 13.1, 13.2  
**NIST CSF Subcategories:** DE.AE, RS.MI  

## Recommendation Description
Implement AI-specific detections and SOAR playbooks (prompt injection, agent/tool abuse, data exfil via AI, connector compromise)

## Details
Detailed Description:
Develop and deploy specialized detection rules within your SIEM/XDR and automated playbooks within your SOAR platform. Detections must not solely look for malicious attackers; they must also alert on authorized agents behaving destructively due to inadequate system prompts or logic failures ("Authorized-but-Harmful" behavior).

Why AI Compounds Risk:
Traditional detection rules are designed for standard malware or lateral movement. They fail to recognize when an autonomous agent chains together authorized API calls in an unauthorized or logically flawed manner. Without AI-specific behavioral detections, an authorized agent can cause massive system degradation (e.g., looping queries, deleting authorized files) while remaining completely invisible to threat-based SIEM alerts.

Examples:
1. Create SIEM rules that trigger when an authorized agent engages in a destructive loop (e.g., mass file deletion) within its permitted scope, catching non-malicious but harmful operational failures.
2. Create a SOAR playbook that automatically isolates an AI agent or revokes its API keys if it begins exhibiting "tool-use drift" (e.g., calling a database query tool it rarely uses).
3. Monitor network egress for sudden spikes in data transfer to known public AI endpoints and trigger an automated SOAR response.

## Implementation Status
- **Policy Defined:** 0
- **Control Implemented:** 0
- **Control Automated:** 0
- **Control Reported:** 0

**Assigned To:**   
**Notes/Evidence:**   
