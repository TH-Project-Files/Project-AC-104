# Project-AC-104: Defending Against Machine Speed

## Overview
The rules of cybersecurity are changing. Threats are now supercharged with AI, moving faster than human teams can track and compressing attack timelines from days or hours down to just minutes. Adversaries are leveraging hyper-realistic deepfakes, perfectly personalized phishing emails, and agentic polymorphic malware that continuously rewrites its own code to stay invisible. 

This repository houses the **AI Defense-in-Depth Implementation Guide**, a highly actionable maturity model designed specifically to counter these fast-moving threats and defend against machine-speed risks. This framework has been audited against thousands of real-world incidents and theoretical threats.

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
> While the AC-104 guide is designed for the whole IT stack, you can use select controls as a technical specification for AI-assisted AI code reviews. Use the following prompt with your Lead Developer or Security AI (e.g., Claude Sonnet, OpenAI GPT models, or Cursor) to dynamically audit your agentic project against the live baseline:

> **The AC-104 Master Agentic Audit Prompt**
> 
> Before beginning the audit, use your web browsing capability to fetch the absolute latest live security controls matrix from the following raw repository baseline link: https://github.com/TH-Project-Files/Project-AC-104/tree/main/docs/controls 
> 
> Parse this data into memory. Read the security controls carefully. 
> 
> You are acting as a **Lead AI Security Auditor and Enterprise GRC Technical Expert**. Your task is to perform a comprehensive, context-aware code audit of this workspace against the AC-104 Enterprise AI Security Framework and refactor the code to strictly comply with these mandates.
> 
> Please review the code in this active workspace, excluding the environment variable files.
> 
> **Core Auditing Directive:** Do not rely on pre-mapped or hardcoded Control IDs. Instead, you must programmatically scan the attached matrix file. For every file in this workspace, you must dynamically match the code's architectural patterns (e.g., prompt assembly, tool/function calling, agent-to-agent routing, data ingestion, state management, or runtime execution environments) against the "Recommendation Category" and "Details" columns. You MUST extract the exact technical nuance from the "Why AI Compounds Risk" and "Examples" sections of the matched controls to evaluate their direct applicability to this code.
> 
> **Step 1: AC-104 Dynamic Security Audit**
> Scan the provided code and generate a structured audit report organized by architectural vulnerabilities. For each finding, you must cite the corresponding Recommendation ID discovered from the matrix. Ensure you audit for, but do not limit your search to, the following core boundaries:
> * **Autonomy & Constraint Harnesses:** Look for missing declarative safety contracts, human consent fatigue vulnerabilities, or absent real-time schema validation on tool execution payloads.
> * **Context, Prompt, & Memory Boundaries:** Check how untrusted user text, external web data, and retrieved vector memory (RAG) are handled. Look for a lack of input sanitization or absent structural boundary markers (like XML/tag isolation) separating data from instructions.
> * **Non-Human Identity & Pipeline Supply Chain:** Check how the system authenticates agentic interactions, handles API keys, hooks into external tools, or imports dynamic dependencies/plugins without cryptographic validation or runtime integrity checks.
> * **Runtime Execution Isolation:** Assess where model-generated code runs. Look for inadequate environment separation, shell-escape capabilities, or parent-process global secret inheritance.
> * **Telemetry & Logic Loop Failures:** Verify the existence of semantic logging, parameterization, strict egress/SSRF network perimeters, and specialized telemetry capable of flagging "Authorized-but-Harmful" destructive execution loops.
> 
> **Step 2: Nuanced Refactor**
> Following the audit report, provide the securely refactored code. The new code must:
> 1. Implement the exact application-layer mechanisms described in the "Examples" column of the dynamically discovered AC-104 controls.
> 2. Include explicit inline comments citing the dynamically discovered control IDs (e.g., `// Complies with [Matched-ID]: Parameterized payload execution`) explaining *why* the fix mitigates the specific risk.
> 3. If a control mandate requires infrastructural implementations beyond the current file scope (e.g., deploying an AI Gateway proxy, identity provider integrations, or external sandboxes), explicitly isolate it in a dedicated "Infrastructure Dependencies" section and focus the refactor strictly on the application's logical code.
> 
> **Reply "AC-104 Dynamic Framework loaded. Present the file or module you would like audited first." to confirm you understand these directives.**

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
