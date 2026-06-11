# AI-AGT-03: Implement Distributed Tracing (e.g., OpenTelemetry) across multi-agent workflows for end-to-end explainability.

**Category:** Applications & Data (Layer 7: Internal LLMs & Agentics)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 8.1, 8.5, 16.1  
**NIST CSF Subcategories:** DE.CM, AU.AU  

## Details
Detailed Description:
Instrument all agentic applications with distributed tracing standards. Generate unique request identifiers for every user prompt and propagate these IDs through all resulting sub-agent spawns, tool invocations, and memory retrievals.

Why AI Compounds Risk:
When agents delegate tasks to other agents (multi-agent coordination), standard application logging loses the thread of execution. Without distributed tracing, it is impossible to reconstruct the provenance chain from a final action back to the original user input, making root cause analysis and regulatory explainability impossible during an incident.

Examples:
1. Implement OpenTelemetry to capture timing and dependency information across agent boundaries.
2. Record complete decision histories, including the specific chunks of retrieved RAG context and the intermediate reasoning steps the agent used to select a specific tool.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
