# AI-LLM-14: Set up alerts to notify security teams if an AI agent starts behaving unexpectedly or out-of-bounds.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
This recommendation involves implementing real-time monitoring and automated notification systems that trigger when an AI agent's actions deviate from established baselines or predefined safety boundaries. It focuses on detecting anomalies in tool usage, data access patterns, and reasoning steps to identify potential compromises, such as prompt injection or autonomous drift, before they result in significant data exfiltration or system damage.

Why AI Compounds Risk:
AI exacerbates this risk because agents possess a degree of non-deterministic autonomy and often hold high-level privileges to interact with internal APIs and sensitive databases. Unlike traditional software with coded paths, an agent's behavior changes based on runtime prompts, making malicious actions indistinguishable from normal operations to standard security tools that lack AI-aware behavioral analysis.

Examples:
1. Implement behavioral analytics to establish a baseline for normal tool invocation sequences and trigger an alert if an agent suddenly accesses a sensitive database or external API it rarely uses.
2. Set up threshold-based alerts for technical metrics such as a sudden spike in token consumption, high frequency of agent restarts, or a "max iterations" breach where an agent is stuck in a logic loop.
3. Integrate AI-aware runtime detection that reconstructs the causal chain of events, alerting security teams when a sequence of individually benign actions—like a RAG query followed by a tool call—indicates a developing "escape chain" attack.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
