# AI-LLM-04: Keep detailed records of everything AI agents do, including the prompts they receive and actions they take.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 1  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `8.1` | NIST CSF: `DE.CM`

---

## Control Details
Detailed Description:
Detailed Explanation: This recommendation involves maintaining comprehensive audit trails of all AI agent activities, including the specific prompts received, the internal reasoning or decision-making steps taken, the tools invoked, and the final outputs or actions executed. These logs serve as a critical observability mechanism for monitoring performance, ensuring regulatory compliance, and facilitating rapid debugging when autonomous systems behave unexpectedly.

Why AI Compounds Risk:
Why AI Exacerbates Risk: Unlike traditional software that follows static, predictable code, AI agents are non-deterministic and can make autonomous, on-the-fly decisions in dynamic environments. This complexity creates "invisible blind spots" where a single user request can trigger dozens of interconnected tool calls and LLM prompts, making it nearly impossible to diagnose failures, detect bias, or identify security breaches without structured, granular records.

Examples:
1. Deploy a centralized log management platform that uses machine-readable formats (like JSON) to capture timestamps, user context, intent classification, and the full sequence of actions for every agent transaction.
2. Establish graduated logging levels—such as Basic, Detailed, and Audit—to balance operational needs with storage costs, ensuring that high-risk activities are documented with full decision trees and reasoning pathways.
3. Integrate real-time monitoring and alerting systems that scan agent logs for anomalies, such as attempts to access sensitive PII or unauthorized external data sharing, to trigger immediate remediation workflows.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
