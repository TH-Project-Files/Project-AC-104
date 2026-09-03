# AI-APP-15: Continuously scan public internet sources for exposed organizational secrets, AI API keys, and non-human identity credentials, and automatically revoke on discovery.

**Category:** Applications & Data (Layer 7: Application)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 7.1, 16.2  
**NIST CSF Subcategories:** ID.RA, DE.CM, RS.MI  
**Layered with:** AI-APP-11 (the inward-facing secrets baseline and CI/CD scanning this control extends beyond the perimeter), AI-AUTH-05 (external monitoring for human credentials — this control covers non-human identity secrets), AI-NHI-01 (the NHI inventory that makes a discovered key attributable to an owner), AI-ACC-03 (aggressive token rotation, which bounds the exposure window this control detects), AI-NET-05 (attack surface management for exposed assets rather than exposed secrets)  

## Details
Detailed Description:
Establish continuous, automated discovery of the organization's own secrets on public internet surfaces outside its control boundary. In-pipeline secret scanning (AI-APP-11) only inspects repositories and build systems the organization owns; it never sees a key pushed to a developer's personal GitHub account, a contractor's repository, a public gist or paste site, a published npm or PyPI package, a public container image layer, an exposed object-storage bucket, a mobile application bundle, a shared Colab notebook, or a Hugging Face repository or Space. Scanning must cover those external surfaces, attribute each finding to an owning system or non-human identity, and trigger automated revocation and rotation rather than a ticket. Because deletion does not equal remediation — a secret committed to a public repository persists in forks, clones, public event archives, and third-party mirrors after the commit is removed — the response workflow must treat every externally discovered credential as permanently compromised and rotate it, not merely delete the exposure.

Why AI Compounds Risk:
Adversaries have automated the entire find-validate-abuse loop. Agentic tooling continuously monitors public code-hosting event streams, tests discovered keys against provider APIs within minutes of a push, and pivots automatically on any that authenticate — collapsing the defender's remediation window from days to a single-digit number of minutes. AI development workflows widen the exposure surface at the same time: experimental notebooks, prompt-sharing sites, agent framework configurations, model-hosting repositories, and observability traces are all published casually and all routinely carry long-lived provider keys. The consequences are also AI-specific. A leaked model-provider key funds resale markets for stolen inference capacity and drives uncapped compute spend (Denial of Wallet), and a leaked cloud or agent-runtime credential grants an autonomous attacker a fully legitimate identity that bypasses the AI gateway, egress controls, and perimeter defenses entirely. Multiple AI-accelerated intrusions have started not with an exploit but with a credential the organization had already published and never knew it had lost.

Examples:
1. Subscribe to a Digital Risk Protection or external secret-scanning service (e.g., GitHub secret scanning with provider validity checks, GitGuardian, Truffle Security, or an equivalent) covering public code hosts, gists, paste sites, package registries, container registries, and public object storage for the organization's key formats, internal hostnames, and cloud account identifiers.
2. Wire every confirmed external finding into an automated revocation pipeline that invalidates the credential at the issuing provider, rotates it through the enterprise secrets manager, and opens an incident — targeting a mean time to revoke measured in minutes, since a validated key is typically abused faster than a human triage queue can reach it.
3. Extend coverage to identities the organization does not own: contractor and vendor repositories under contractual scanning obligations, developer personal accounts covered by acceptable-use policy, and published artifacts (mobile bundles, container images, model repositories, and Spaces) scanned at release time as a promotion gate.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
