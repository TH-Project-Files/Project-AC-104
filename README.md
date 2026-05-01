# Project-AC-104: Defending Against Machine Speed

## Overview
The rules of cybersecurity are changing. Threats are now supercharged with AI, moving faster than human teams can track and compressing attack timelines from days or hours down to just minutes. Adversaries are leveraging hyper-realistic deepfakes, perfectly personalized phishing emails, and agentic polymorphic malware that continuously rewrites its own code to stay invisible. 

This repository houses the **AI Defense-in-Depth Implementation Guide**, a highly actionable maturity model designed specifically to counter these fast-moving threats and defend against machine-speed risks.

---

## The Defense-in-Depth Framework
### Full-Stack Defensive Coverage
The AC-104 framework is built to secure the **entire IT environment**, recognizing that AI risks cannot be mitigated at the application layer alone. The controls provide a holistic defense strategy across the four critical layers of the modern enterprise stack:

* **🌐 Networking:** Hardening the perimeter and internal traffic against automated lateral movement and SSRF-driven data exfiltration.
* **🆔 Identity & Access Management (IAM):** Enforcing machine-identity non-repudiation and granular permissions for autonomous agents.
* **💻 Endpoints:** Securing the devices and execution environments where AI models and agentic sub-processes reside.
* **📱 Applications:** Defending the logic, prompt boundaries, and data pipelines that power generative AI systems.

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

1. **Download the Tracker:** Grab the `AC-104-version.csv` from the `/data` folder.
2. **Filter for Impact:** Start by filtering for **"1-High" aggregate risk** within **Implementation Group 1**. 
3. **Execute Audits:** Use the prompt provided in the [Securing Agentic Workflows](#-securing-agentic-workflows) section to evaluate your current code.
4. **Measure Progress:** Use the "Control Implemented" column to track your score (1-10) and report readiness averages to stakeholders.

---

> [!TIP]

### Application Example: Agentic Security Auditing
You can use the AC-104 list as a technical specification for AI-assisted code reviews. Use the following prompt with your Lead Developer or Security AI (e.g., Claude Sonnet, OpenAI GPT-XX, or Cursor) to audit your agentic project:

> **The AC-104 Master Audit Prompt**
> 
> Read the security controls in `@AC-104-v[Specify version].csv` carefully.
> You are acting as a **Lead AI Security Auditor and Enterprise GRC Technical Expert**. Your task is to perform a comprehensive code audit of the workspace against the AC-104 Enterprise AI Security Framework and refactor the code to strictly comply with these mandates.
> 
> **Core Auditing Directive:** Do not just read the "Recommendation Description." You MUST parse the "Details" column for every relevant control—specifically analyzing the "Why AI Compounds Risk" and "Examples" sections. Extract the technical nuance from these examples and assess their direct applicability to the current code workspace.
> 
> **Step 1: AC-104 Security Audit**
> Scan the provided code and generate a structured audit report citing specific Recommendation IDs. Focus specifically on these technical implementation areas:
> * **Agent Autonomy & HITL (AI-AGT-01, AI-LLM-08):** Look for missing Human-in-the-Loop approvals for high-risk actions.
> * **Isolation & Sandboxing (AI-LLM-17, AI-LLM-22):** Check if AI code execution is occurring in the host environment rather than a sandbox; ensure agents do not inherit `process.env`.
> * **Data & Instruction Boundaries (AI-LLM-23, AI-APP-01):** Ensure strict input sanitization and structural boundary markers (e.g., `<external_content>` tags) are present.
> * **Execution Safety (AI-LLM-12):** Verify LLM-generated outputs (SQL, Shell) use parameterized queries, avoiding string interpolation.
> * **Network Boundaries (AI-LLM-09):** Check outbound network requests against strict, hardcoded allow-lists.
> 
> **Step 2: Nuanced Refactor**
> Provide the refactored code that:
> 1. Implements fixes directly inspired by the "Examples" listed in the AC-104 controls.
> 2. Adds inline comments citing the specific AC-104 control ID (e.g., `// Complies with AI-LLM-12`).
> 3. Notes "Infrastructure Dependencies" for changes outside the scope of application code.
> 
> **Reply "AC-104 Framework loaded. Which file or module are we auditing first?" to confirm.**

---

## Repository Structure
* `/data`: Contains the primary `AC-104-version.csv` file.
* `/docs`: Detailed documentation and implementation deep-dives.
* `mkdocs.yml`: Configuration for the project's documentation site.

**Remember:** AI is continuously learning how to attack. Your defenses must continuously learn how to adapt. Standing still is no longer an option. Always maintain human in the loop, you the human are ultimately responsible for your environment and actions. AC-104 is provided for educational purposes and is not a substitute for professional guidance and application. 
