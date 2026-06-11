# AI-APP-14: Implement Supply-chain Levels for Software Artifacts (SLSA) or equivalent frameworks for all agent dependencies and dynamically loaded tools.

**Category:** Applications & Data (Layer 7: Application)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 16.2, 2.1  
**NIST CSF Subcategories:** GV.SC, PR.DS  
**Layered with:** AI-APP-13 (dependency health evaluation — verify provenance with this control, then evaluate maintenance health), AI-LLM-19 (AIBOM documentation of model and plugin lineage), AI-MCP-01 (MCP server provenance and capability-drift detection)  

*Note: Re-homed from AI-APP-10 in v1.2.0 to resolve an ID collision with the AI Gateway control.*

## Details
Detailed Description:
Establish and enforce a Secure Software Development Framework (SSDF) that explicitly manages third-party agentic dependencies. Organizations must verify the digital signatures, cryptographic hashes, and provenance of agent packages, tool plugins, and runtime libraries before allowing them into the production execution environment.

Why AI Compounds Risk:
AI agents rely heavily on dynamic, open-source tool libraries (e.g., Python packages or npm modules) to interact with external services. If an attacker successfully compromises a package in the supply chain, the agent will inadvertently download and execute the backdoor. Because agents have autonomous execution capabilities, a poisoned dependency essentially hands the attacker direct, machine-speed access to the agent's environment and authorized tools.

Examples:
1. Adopt the SLSA framework to ensure artifact integrity from source code to deployment, preventing the injection of unauthorized code into the agent's toolsets.
2. Enforce strict hash-checking in package managers (e.g., package-lock.json or poetry.lock) to verify the SHA-256 signatures of all third-party AI plugins before loading them into the runtime.
3. Maintain an internally vetted, private artifact registry (e.g., Artifactory) for agent dependencies, explicitly blocking the agent platform from dynamically fetching unverified code directly from public repositories.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
