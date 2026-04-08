***

# Project-AC-104: Defending at Machine Speed

## Overview
The rules of cyber security have completely changed. Threats are now supercharged with AI, moving faster than human teams can track and compressing attack timelines from days or hours down to just minutes. Adversaries are leveraging hyper-realistic deepfakes, perfectly personalized phishing emails, and polymorphic malware that continuously rewrites its own code to stay invisible. 

This repository houses an **AI Defense-in-Depth Implementation Guide**, a brand new, highly actionable maturity model designed specifically to counter these fast-moving threats and help you defend at machine speed.

## The Defense-in-Depth Framework
Rather than relying on unfiltered aggregate tasks, or vague high-level recommendations, this model is structured in multiple ways, beginning with assessing risk across four core pillars to help you prioritize what to protect first:
1. **Data Sensitivity:** How sensitive is the data involved?
2. **Network Exposure:** Is the system connected to the internet?
3. **Recovery Time Objective (RTO):** How fast must the system be brought back online if it goes down?
4. **Audience:** Who uses the system and how widely?

### The "Crawl, Walk, Run" Approach
To prevent teams from becoming overwhelmed by attempting to implement 100+ controls simultaneously, the framework is broken down into three manageable **Implementation Groups (IGs)**:
*   **IG 1 (The Starting Line):** Essential foundational controls everyone needs to deploy.
*   **IG 2:** More advanced defenses for organizations facing higher risks.
*   **IG 3:** Specialized, high-end controls for well-resourced organizations.

## Getting Started
To move from chaos to clarity, download the AC-104-V1.csv tracker from /data and begin by filtering to show only the controls with a **"1-High" aggregate risk level** within **Implementation Group 1**. This single step focuses your energy where it will have the largest impact. Proceed from there!

## Repository Structure
This repository contains the following structure to support your implementation:
*   `/data`: Contains the primary `AC-104-V1.csv` file, cataloging all governance, identity, endpoint, application, and network controls.
*   `/docs`: Core documentation files for the framework.
*   `mkdocs.yml`: Configuration file for building and hosting the project's documentation pages.

**Remember:** AI is continuously learning how to attack. Your defenses must continuously learn how to adapt. Standing still is no longer an option.
