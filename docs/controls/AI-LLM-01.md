# AI-LLM-01: Put strict network filters around your internal AI models so hackers can't steal or copy the AI's core logic.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 1  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Strict network filtering for internal AI models involves creating a secure perimeter around the model's infrastructure to control access and prevent unauthorized extraction of its architecture, parameters, or weights. This includes using firewalls, API gateways, and air-gapped or isolated network segments to ensure that only authenticated and authorized users or systems can interact with the model, thereby protecting intellectual property from competitors or malicious actors.

Why AI Compounds Risk:
AI exacerbates this risk because models are susceptible to query-based extraction attacks where an adversary can systematically probe an API with thousands of prompts to reconstruct the model's internal logic. Furthermore, the high development costs and competitive value of proprietary models make them lucrative targets for model theft, which can be executed remotely through vulnerable network interfaces or APIs.

Examples:
1. Deploy an AI gateway to centralize security, enabling real-time anomaly detection, prompt moderation, and strict rate limiting to prevent high-volume query-based extraction attempts.
2. Utilize robust API access controls, such as OAuth or JWT, combined with IP-based filtering to ensure that only verified corporate applications and users can reach the model endpoints.
3. Segment the network to host internal AI models in isolated environments, using advanced network filters to block all outbound data transfers that do not match pre-defined, authorized patterns.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
