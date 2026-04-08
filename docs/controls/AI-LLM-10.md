# AI-LLM-10: Thoroughly test and review the code and instructions for AI agents before letting them run in the real world.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `16.1, 16.2` | NIST CSF: `PR.DS, GV.SC`

---

## Control Details
Detailed Description:
This recommendation emphasizes the necessity of a rigorous evaluation pipeline for AI agents, involving tracking components, applying specific metrics (like hit rate and task completion), and logging execution flows via LLM tracing to ensure agents behave consistently and fail gracefully before deployment.

Why AI Compounds Risk:
AI exacerbates risk because agents often operate with "superuse" privileges and autonomy, meaning a single flaw or compromised skill can lead to machine-speed data exfiltration, unauthorized system access, or chained vulnerabilities across an entire agent network without human oversight.

Examples:
1. Establish LLM tracing and observability using tools to monitor end-to-end execution traces and individual component spans during runtime.
2. Create a "golden dataset" of 20-50 diverse test cases, including edge cases and adversarial inputs, to benchmark agent performance and ensure consistency across model updates.
3. Implement a mix of 3-5 metrics, such as tool hit rates and success rates, supplemented by LLM-based evaluators to provide qualitative judgment on response helpfulness and coherence.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
