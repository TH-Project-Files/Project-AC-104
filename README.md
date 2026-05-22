# Project-AC-104: Defending Against Machine Speed

## Overview
The rules of cybersecurity are changing. Threats are now supercharged with AI, moving faster than human teams can track and compressing attack timelines from days or hours down to just minutes. Adversaries are leveraging hyper-realistic deepfakes, perfectly personalized phishing emails, and agentic polymorphic malware that continuously rewrites its own code to stay invisible. 

This repository houses the **AI Defense-in-Depth Implementation Guide**, a highly actionable maturity model designed specifically to counter these fast-moving threats and defend against machine-speed risks.

---

## The Defense-in-Depth Framework
### Full-Stack Defensive Coverage
The AC-104 framework is built to secure the **entire IT environment**, recognizing that AI risks cannot be mitigated at the application layer alone. The controls provide a holistic defense strategy across the four critical layers of the modern enterprise stack:

- 🌐 **Networking:** Hardening the enterprise perimeter and internal traffic against AI-automated reconnaissance, high-speed lateral movement, and stealthy C2 callbacks to newly generated malicious domains.
- 🆔 **Identity & Access Management (IAM):** Defending both human and non-human identities through phishing-resistant MFA, continuous session monitoring, out-of-band verification for deepfakes, and strict governance over autonomous service accounts.
- 💻 **Endpoints:** Securing corporate devices using advanced behavioral telemetry (EDR/XDR) to block AI-generated polymorphic malware, while restricting unauthorized "Shadow AI" runtimes and untrusted script execution.
- 📱 **Applications & Data:** Protecting enterprise software and messaging pipelines against AI-fuzzing and hyper-personalized phishing, while governing third-party AI integrations via CASBs, API gateways, and strict software supply chain (SLSA) tracking.

### Risk Assessment Method
Rather than relying on vague high-level recommendations, this model is structured to assess risk across four core pillars:

1. **Data Sensitivity:** How sensitive is the data involved?
2. **Network Exposure:** Is the system connected to the internet?
3. **Recovery Time Objective (RTO):** How fast must the system be brought back online?
4. **Audience:** Who uses the system and how widely?

### The "Crawl, Walk, Run" Approach
The framework is broken down into three **Implementation Groups (IGs)** to prevent project fatigue:
* **IG 1 (The Starting Line):** Essential foundational controls for all deployments.
* **IG 2:** Advanced defenses for organizations facing higher risk profiles.
* **IG 3:** Specialized, high-end controls for mission-critical or well-resourced environments.

## Getting Started
To move from chaos to clarity:

1. **Download the Tracker:** Grab the `AC-104-version.csv` from the `/data` folder or clone the raw controls directly from the `/docs` folder.
2. **Filter for Impact:** Start by filtering for **"1-High" aggregate risk** within **Implementation Group 1**. 
3. **Measure Progress:** Use the "Control Implemented" column to track your score (1-10) and report readiness averages to stakeholders.

---

> [!TIP]
> ### Layer 7 Application Example: Agentic Security Auditing
> While the AC-104 guide is designed for the whole IT stack, you can use select controls as a technical specification for AI-assisted AI code reviews. Use the following prompt with your Lead Developer or Security AI (e.g., Claude Sonnet, OpenAI GPT-XX, or Cursor) to audit your agentic project:

> **The AC-104 Master Audit Prompt**
> 
> Read the security controls in `@AC-104-v[Specify version].csv` carefully. 
> 
> You are acting as a **Lead AI Security Auditor and Enterprise GRC Technical Expert**. Your task is to perform a comprehensive code audit of the workspace against the AC-104 Enterprise AI Security Framework and refactor the code to strictly comply with these mandates.
> 
> Please review the code in this active workspace, excluding the environment variable files.
> 
> **Core Auditing Directive:** Do not just read the "Recommendation Description." You MUST parse the "Details" column for every relevant control—specifically analyzing the "Why AI Compounds Risk" and "Examples" sections. Extract the technical nuance from these examples and assess their direct applicability to the current code workspace.
> 
> **Step 1: AC-104 Security Audit**
> Scan the provided code and generate a structured audit report citing specific Recommendation IDs. Focus specifically on these technical implementation areas:
> * **Automated Guardrails & Autonomy (AI-AGT-01, AI-LLM-08):** Do not rely solely on Human-in-the-Loop (HITL) approvals, which fail due to consent fatigue. Look for strict, automated Harness-layer constraints, declarative safety contracts, and real-time schema validation for all tool calls.
> * **Data, Memory & Instruction Boundaries (AI-LLM-23, AI-APP-01, AI-LLM-15):** Ensure strict input sanitization is present and that structural boundary markers (like `<external_content>` tags) are used to separate untrusted external data AND retrieved agent memory (RAG) from system prompts to prevent indirect and persistent memory poisoning.
> * **Agent Communications & Supply Chain (AI-LLM-24, AI-APP-10):** Verify that any agent-to-agent or agent-to-tool communications use cryptographic signatures and freshness nonces (timestamps) to prevent replay attacks. Ensure dynamic third-party plugin/tool loading relies on strict hash verification (e.g., via lockfiles).
> * **Isolation & Sandboxing (AI-LLM-17, AI-LLM-22):** Check if AI code execution is occurring in an isolated microVM/sandbox, and ensure the agent subprocess does not inherit the parent process's global environment variables (e.g., `process.env`).
> * **Execution Safety & Network (AI-LLM-12, AI-LLM-09, AI-DET-01):** Verify parameterized queries (no string interpolation), strict SSRF network allow-lists, and sufficient telemetry logging to detect "Authorized-but-Harmful" operational loops where the agent is acting destructively within its permissions.
> 
> **Step 2: Nuanced Refactor**
> Provide the refactored code that:
> 1. Implements the architectural fixes directly inspired by the "Examples" listed in the AC-104 controls.
> 2. Adds inline comments citing the specific AC-104 control ID (e.g., `// Complies with AI-LLM-12: Parameterized query execution`) explaining *why* the implementation mitigates the risk.
> 3. Notes "Infrastructure Dependencies" for changes outside the scope of application code (e.g., deploying a behavioral WAF).
> 
> **Reply "AC-104 Framework loaded. Which file or module are we auditing first?" to confirm.**

---

## Repository Structure
* `/data`: Contains the primary `AC-104-version.csv` file.
* `/docs`: Detailed documentation and implementation deep-dives.
* `mkdocs.yml`: Configuration for the project's documentation site.

**Remember:** AI is continuously learning how to attack. Your defenses must continuously learn how to adapt. Standing still is no longer an option. Always maintain human in the loop, you the human are ultimately responsible for your environment and actions. AC-104 is provided for educational purposes and is not a substitute for professional guidance and application. 

## License

© 2026 TH-Project-Files. 

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License. 

**What this means:**
* **Anyone can use it:** You are free to copy, redistribute, remix, and build upon this framework.
* **Attribute the author:** You must give appropriate credit, provide a link to the license, and indicate if changes were made.
* **No commercial use:** You may not use this material, or derivatives of it, for commercial purposes or monetization.

The software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

For the full legal terms, please review the [LICENSE.md](LICENSE.md) file included in this repository.
