# AI-LLM-02: Put speed limits on AI agents so they don't get stuck in endless loops or crash internal systems.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 1  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Putting speed limits on AI agents involves implementing rate limiting and behavioral throttling to constrain the frequency and volume of requests an agent can make within a specific timeframe. This prevents agents from entering recursive loops, where they repeatedly execute the same faulty logic, or overwhelming infrastructure with high-velocity requests that can lead to system crashes or resource exhaustion.

Why AI Compounds Risk:
AI exacerbates this risk because agents operate at machine speed, capable of executing thousands of requests per second, which far exceeds human operational rhythms and traditional security monitoring capabilities. Furthermore, sophisticated AI can exhibit behavioral drift or execute coordinated, distributed activities that stay within standard fixed limits while still achieving a malicious or catastrophic aggregate impact.

Examples:
1. Implement sliding window rate limiting to continuously track requests over rolling time periods, preventing agents from exploiting fixed window boundaries to double their throughput.
2. Deploy behavioral throttling that applies graduated constraints (such as 25% to 75% rate reductions) based on the severity of detected anomalies, such as CPU consumption patterns inconsistent with the agent's declared function.
3. Utilize tools like distributed in-memory data stores and event streaming platforms for real-time behavioral scoring and sub-millisecond lookups to ensure consistent enforcement across multiple entry points in a corporate network.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
