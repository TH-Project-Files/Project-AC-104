# AI-USR-12: Mandate "Secure AI Prompting and Vibe Coding" training for all citizen developers and staff utilizing AI-assisted coding tools.

**Category:** Governance & People (Layer 0: User Facing Controls)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 14.1, 14.9  
**NIST CSF Subcategories:** PR.AT  
**Layered with:** AI-GOV-01 (the AI use policy governing vibe coding that this training operationalizes), AI-APP-11 (secrets management baseline — this training teaches the habit that control enforces), AI-APP-09 (scanning repositories for AI-generated code), AI-END-05 (removal of local admin rights limiting the blast radius of an unsafe AI-generated script)  

## Details
Detailed Description:
Develop a specialized, lightweight training module specifically for non-engineering staff ("vibe coders") who use AI to generate scripts, automations, or web apps. The training must bypass traditional SSDLC concepts and focus directly on the three core AI-coding risks: 1) Supply Chain Poisoning (manually verifying AI-suggested packages before installation), 2) Secret Management (prompting the AI to never hardcode API keys), and 3) Execution Isolation (never running AI-generated scripts with local Admin privileges).

Why AI Compounds Risk:
AI models hallucinate non-existent code libraries (which attackers register to drop malware), prioritize functional code over secure code (leaving secrets in plaintext), and fail to understand the user's local execution privileges. Vibe coders lack the traditional engineering background to spot these flaws, leading to rapid, systemic vulnerabilities if they implicitly trust the AI's output.

Examples:
1. Require any employee requesting a Copilot or Cursor license to pass a 15-minute module on "AI Hallucinations in Code."
2. Run simulation drills where vibe coders are presented with an AI script containing a hardcoded token and must successfully prompt the AI to refactor it into an environment variable.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
