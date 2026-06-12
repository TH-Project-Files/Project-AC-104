# Scoring & Adoption Methodology

This page defines how AC-104 controls are scored, prioritized, and rolled out. It is the authoritative reference for the two fields every control carries — **Implementation Group** and **Aggregate Risk Level** — and for the phased adoption model built on them.

---

## The Two Axes: Priority vs. Risk

AC-104 deliberately separates two questions that frameworks often conflate:

| Axis | Field | Question it answers |
|---|---|---|
| **Priority** | Implementation Group (IG 1/2/3) | *When* should we implement this control? |
| **Risk** | Aggregate Risk Level (1-High / 2-Medium / 3-Low) | *What is at stake* for the system this control protects? |

**Implementation priority is conveyed by the Implementation Group, not the risk score.** The Aggregate Risk Level is a descriptive attribute of the protected asset — never triage your rollout by risk level alone.

---

## The Four Risk Pillars

The Aggregate Risk Level is calculated from four pillars assessed against the system the control protects:

1. **Data Sensitivity** — the classification level of the data the system stores, processes, or can reach. For AI systems, include everything reachable through the model's tools, connectors, and retrieval corpus — not just data the system "owns."
2. **Network Exposure** — the system's attack surface: internet-facing, internal-only, or isolated. This pillar is the likelihood proxy.
3. **Recovery Time Objective (RTO)** — how quickly the system must be restored after impact. For AI-backed systems, set RTO with AI-REC-01's recovery procedures in hand: vector stores and agent memory recover *behavioral fidelity*, not just bytes, and their realistic restoration timelines are not equivalent to a database restore.
4. **Audience Blast Radius** — how many users would be unable to perform **critical business functions** if the system were impacted. This is a business-impact-analysis breadth measure, not a popularity count.

### Reading the Score Honestly

The aggregate is **availability-weighted**. The signature AI failure modes — silent data exfiltration through an agent, cross-tenant session leakage, model theft, quiet RAG-corpus poisoning — typically disrupt nobody's work: blast radius is near zero, there is nothing to "recover," and exposure is often internal. Three of four pillars floor out, and the aggregate can land at **3-Low even when the failure mode is a reportable breach**. That is by design, not a defect:

> **A Low aggregate can coexist with severe confidentiality risk. In those cases, the Implementation Group carries the urgency.**

This is why several confidentiality-critical controls (e.g., session isolation, code-execution sandboxing) carry Low aggregates but IG assignments that demand early adoption from any organization the control applies to.

### Scoring Unit and Re-Scoring Cadence

Score the system the control protects, **at its current stage of adoption**. Blast radius is the most time-sensitive pillar in the framework: an internal copilot that strands nobody today becomes a single point of failure for thousands of users once it is embedded in service-desk, SOC-triage, or customer workflows.

**Re-scoring is mandatory at AI-GOV-16 change gates.** Any change that expands an AI system's user dependency — new integrations, new user populations, workflow embedding — triggers a blast-radius recalculation as part of that control's evaluation gate.

---

## Implementation Groups: Crawl, Walk, Run

Implementation Groups are **cumulative**, exactly as in CIS Controls v8: an IG 2 organization implements all IG 1 *and* IG 2 controls; an IG 3 organization implements everything.

- **IG 1 — The Starting Line.** Essential controls for every organization using AI in any form, including organizations with limited security resources. Dominated by governance, vendor terms, awareness training, and low-cost identity and hygiene wins.
- **IG 2 — Operational AI.** For organizations deploying AI integrations at scale, running agents in production, or carrying regulatory obligations. This is where the bulk of the LLM/agentic technical controls live.
- **IG 3 — Specialized Defense.** High-end controls for mature, well-resourced, or high-risk environments — typically dedicated hardware (inline deep-learning inspection, HSM-backed identities), advanced provenance, and forensic-grade capabilities.

Current distribution across the 118 controls (CIS v8 shown for comparison):

| | IG 1 | IG 2 | IG 3 |
|---|---|---|---|
| **AC-104** (118 controls) | 37 (31%) | 62 (53%) | 19 (16%) |
| **CIS v8** (153 safeguards) | 56 (37%) | 74 (48%) | 23 (15%) |

The IG 2 weight is concentrated in the Applications & Data domain — the LLM/agentic core — because those controls presuppose that the organization is actually deploying AI. Which leads to the most important rule on this page:

### Applicability Triggers (IG Overrides)

CIS IGs assume the safeguard applies to everyone and only resources differ. AC-104 cannot: some controls are irrelevant until you deploy a capability, and **day-one mandatory the moment you do — regardless of your organization's size or IG tier.** The following triggers override the IG label:

| If your organization... | These controls become baseline immediately |
|---|---|
| Deploys autonomous agents (any scale, any vendor) | AI-AGT-01, AI-PAM-01, AI-LLM-22, AI-LLM-23, AI-LLM-24 |
| Runs agents that write or execute code | AI-LLM-17 |
| Uses MCP servers or dynamically loaded agent tools | AI-MCP-01, AI-APP-14 |
| Operates a multi-tenant AI application (multiple users, one system) | AI-LLM-18 |
| Allows browser-driving / computer-use agents | AI-AGT-01 (Credentialed Web Actions trigger), AI-END-11 |

A small organization at IG 1 resources that stands up its first production agent implements the first row *that week* — "IG 2" on those controls describes the general population's timeline, not yours.

---

## Phased Launch

The recommended rollout, in the spirit of CIS v8's IG-based phasing. Begin every phase by applying any Applicability Triggers that match your environment.

| Phase | Scope | Count | Intent |
|---|---|---|---|
| **1 — First 30 days** | IG 1 controls with 1-High aggregate risk | 7 | AI-VND-02, AI-GOV-17, AI-APP-11, AI-AUTH-01, AI-END-10, AI-USR-01, AI-USR-02 — contract terms, threat modeling, secrets hygiene, possession-first auth, continuous scanning, and two awareness toggles |
| **2 — First quarter** | Remaining IG 1 | 30 | Complete the essential baseline: policy, catalog, training program, identity fundamentals |
| **3 — Walk, priority slice** | IG 2 controls with 1-High aggregate risk | 21 | The highest-stakes operational controls: agent governance, gateway + egress enforcement, NHI inventory, behavioral mailbox intelligence |
| **4 — Walk, complete** | Remaining IG 2 | 41 | Full operational coverage |
| **5 — Run** | IG 3 | 19 | Adopt as risk profile and resources justify |

Track progress with the maturity columns in the versioned CSV (below) and report phase-completion percentages to stakeholders.

---

## Maturity Tracking

The versioned CSV (`/data/AC-104-vX.Y.Z.csv`, highest semantic version is authoritative) carries four maturity dimensions per control, each scored on a three-point ordinal scale — **0 = not started, 1 = partial, 2 = full**:

| Column | Question |
|---|---|
| Policy Defined | Is there a written, approved policy mandating this control? |
| Control Implemented | Is the control technically in place? |
| Control Automated | Does it operate without manual intervention? |
| Control Reported | Is its status visible in recurring reporting? |

The four dimensions are intentionally sequential — policy before implementation, implementation before automation — so an honest profile typically reads as a descending staircase. Report readiness as per-domain or per-IG averages.

---

## Control Anatomy

Every control file follows one template:

- **Title (H1)** — `AI-XXX-NN: imperative description`
- **Category** — one of five domains (Governance & People, Identity & Access, Networking, Endpoints, Applications & Data), with the original defense layer retained as a sub-tag for continuity
- **Implementation Group / Aggregate Risk Level** — the two axes defined above
- **CIS v8 Safeguards / NIST CSF Subcategories** — mappings (NIST references use CSF 2.0 vocabulary)
- **Layered with** *(where present)* — names the controls this one intentionally overlaps with and each one's distinct job. Apparent redundancy across these sets is **defense-in-depth, not duplication** — and frequently one platform capability, not several products. Evaluate shared tooling before procuring per-control point solutions.
- **Details** — Detailed Description, Why AI Compounds Risk, and Examples

---

## Control ID Stability

Control IDs are **never renumbered**. Gaps in the sequence are retired controls, preserved so that historical assessments remain comparable:

- **Retired (pre-v1.2.0):** AI-ACC-04, AI-GOV-04 through AI-GOV-07, AI-LLM-06, AI-DLK-01, AI-DLK-02, AI-VND-01
- **Redefined in v1.2.0** (resolving a content fork between the CSV and documentation): AI-APP-10 (now the centralized AI Gateway), AI-APP-11 (now the AI-stack secrets management baseline), AI-NET-08 (now gateway-only egress enforcement)
- **Re-homed in v1.2.0:** the prior AI-APP-10 (SLSA supply chain) → **AI-APP-14**; the prior AI-NET-08 (BGP route-hijack monitoring) → **AI-NET-10**
- **Added in v1.2.0:** AI-USR-12 (secure AI prompting and vibe-coding training)

If you tracked an assessment against v1.1.x, re-map those three redefined IDs before comparing scores across versions.

---
*Part of the Argus Centurion (AC-104) Open Source AI Readiness Security Framework.*
