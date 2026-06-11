# AI-LLM-10: Mandate pre-deployment testing and review of AI agent code and instructions.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 16.1, 16.2  
**NIST CSF Subcategories:** PR.DS, GV.SC

---

## Details
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
