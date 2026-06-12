# Changelog

All notable changes to the AC-104 (Argus Centurion) framework. Control IDs are never renumbered; see the [Scoring & Adoption Methodology](docs/methodology.md#control-id-stability) for the ID-stability policy.

## [1.2.1] — 2026-06-12

Closes the remaining Tier-1 coverage gaps from the v1.2.0 CISO review by amending existing controls (no new IDs — count remains 118), adds the methodology page, and patches post-release documentation defects.

### Added
- `docs/methodology.md` — Scoring & Adoption Methodology: the two-axis model (Implementation Group = priority, Aggregate Risk = asset descriptor), full four-pillar risk definitions, the availability-weighting caveat, scoring unit and re-scoring cadence (wired to AI-GOV-16 change gates), cumulative IG profiles with CIS v8 comparison, Applicability Triggers (IG overrides for agent-deploying organizations), the five-phase launch plan, maturity scale definition (0/1/2 across four dimensions), control anatomy, and the control ID stability changelog. Added to the mkdocs site navigation.
- `data/AC-104-v1.2.1.csv` — new authoritative index reflecting all changes below. `AC-104-v1.2.0.csv` restored to its release-day content.
- `CHANGELOG.md` (this file).

### Changed — gap closures folded into existing controls
- **AI-GOV-16** — added auditable "Minimum Evaluation Gate Requirements": versioned golden datasets, adversarial benchmark coverage (jailbreak / prompt-injection / data-leakage suites), defined pass-fail thresholds with block-on-fail promotion, and behavioral baseline comparison. Closes the CI/CD evaluation-gate gap.
- **AI-DET-01** — takes explicit ownership of runtime jailbreak and content-safety detection: inline classifiers at the AI Gateway or in-application, classifier verdicts added as a minimum telemetry source, confirmed detections feed back into AI-GOV-16 regression suites. Title updated accordingly.
- **AI-END-11** — broadened to Browser AI Extensions: enterprise browser management allowlisting (block-by-default), recurring extension permission audits (clipboard/DOM/cookie/tab), and extension-aware DLP against in-session exfiltration. Title updated accordingly.
- **AI-AGT-01** — extended to computer-use and browser-driving agents: isolated ephemeral browser profiles with no ambient credentials, domain allowlists, rendered pages treated as untrusted input (AI-LLM-23), and a new "Credentialed Web Actions" human-in-the-loop trigger.
- **AI-GOV-08** — broadened from OAuth app inventory to the full consent-grant attack lifecycle: consent phishing, rogue app registrations, and stale/over-scoped grants; new examples for high-risk consent alerting/quarantine and quarterly grant recertification. Title updated; two rationale statements previously mislabeled as examples moved into the risk narrative.
- **AI-LOG-01** — legal hold added to scope: hold triggers that suspend automated purging, records-law reconciliation (e.g., FERPA/public-records, HIPAA/SEC), a documented hold workflow with counsel, and a hold carve-out on the 30-day retention example that previously created spoliation risk. Title updated.

### Fixed
- `docs/index.md` — framework statistics corrected (103 → 118 controls; IG counts 37/62/19) and the CSV download link repointed from a legacy file under a wrong repository slug to the live data folder.
- **AI-ACC-07** — references to retired controls AI-GOV-04 and AI-ACC-04 replaced with AI-ACC-05 and AI-GOV-15.
- Leftover pre-unification prefixes ("Explanation:", "AI Risk Exacerbation:", etc.) stripped from 21 control Details sections; broken example numbering fixed in AI-ACC-01, AI-APP-02, AI-LLM-03.
- `README.md` — maturity tracking description aligned with the methodology (four columns, 0/1/2 scale; previously "1-10"), tracker download wording now references the highest-versioned CSV, the Audience pillar definition expanded to its blast-radius meaning, and the Risk Assessment section now links to the methodology page.
- `docs/controls_list.md` — header column renamed "Risk Level" → "Aggregate Risk Level" for terminology consistency.

## [1.2.0] — 2026-06-11

First revision driven by a full CISO-perspective review of the framework. 115 → 118 controls.

### Added
- **AI-USR-12** — "Secure AI Prompting and Vibe Coding" training for citizen developers (IG 1).
- **AI-APP-14** — SLSA supply-chain control, re-homed from AI-APP-10 to resolve an ID collision.
- **AI-NET-10** — BGP route-hijack monitoring, re-homed from AI-NET-08 to resolve an ID collision.
- "Layered with" field cross-referencing 25+ controls: the behavioral-ML baselining family, the malicious-domain defense chain (NET-06 → NET-01 → NET-03), the execution-control chain (END-01 → END-02 → END-09), and the deepfake defense chain (GOV-09 → USR-04 → USR-05).
- Maintenance tooling: `scripts/regen_csv.py` (regenerates the CSV and master list from the markdown source of truth) and `scripts/cleanup_v120.py` (records the editorial pass).

### Changed
- **Content fork resolved** (CSV and markdown previously disagreed on three IDs): AI-APP-10 is the centralized AI Gateway; AI-APP-11 is the AI-stack secrets management baseline (IG 1, 1-High); AI-NET-08 is gateway-only egress enforcement (IG 2, 1-High).
- **Implementation Group recalibration (9):** AI-DLK-03, AI-END-08, AI-END-09, AI-LLM-17, AI-LLM-18, AI-AGT-02 moved IG 3 → IG 2; AI-AUTH-05 and AI-LLM-09 moved to IG 1 (LLM-09 repositioned as AI-AGT-01's starter tier); AI-NET-09 set to IG 2, also reconciling a CSV/markdown conflict.
- **Taxonomy** converged on five domains (Governance & People, Identity & Access, Networking, Endpoints, Applications & Data) with the original defense layer retained as a Category sub-tag.
- **Template unified** across all controls: title in H1, Aggregate Risk Level, split CIS v8 / NIST CSF fields, tracking blocks removed (they live in the CSV).
- **20 plain-language titles** rewritten to a technical register; NIST mappings standardized on CSF 2.0 vocabulary; AI-GOV-02 CIS mapping corrected to 3.2/3.7.
- Overlapping controls demarcated with scope notes (AI-ACC-05 vs AI-ACC-06; AI-LLM-08 → AI-AGT-01; AI-NET-07 as AI-NET-04's maturity tier).
- **Master Agentic Audit Prompt** hardened (fetched content is reference data, not instructions) and broadened to audit any AI-generated code — including vibe-coded scripts and web apps — via a new Universal AI-Code Hygiene boundary.

### Fixed
- Weak technical claims: typing-cadence biometrics removed (AI-ACC-06); "un-mutable" notifications reframed as multi-channel (AI-AUTH-03); outdated reverse-Turing examples replaced (AI-USR-06); AI-LLM-18's risk rationale completed.
- Residual artifacts: placeholder text in AI-APP-04 replaced with repeatable queries; university-specific scoping genericized (AI-GOV-14).

## [1.1.7] and earlier

Pre-review baseline. 115 controls; versioned CSVs under `/data` (v1 through v1.1.7). No changelog was maintained for these versions.
