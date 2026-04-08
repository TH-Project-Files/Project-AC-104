# AI-LLM-05: Test any fake (synthetic) or anonymized data to make sure hackers can't reverse-engineer it to find real people's identities.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 2  
**Risk Level:** 2-Medium  
**Framework Mappings:** CIS v8: `16.1` | NIST CSF: `PR.DS`

---

## Control Details
Detailed Description:
Explanation: This recommendation emphasizes that synthetic or anonymized data is not inherently anonymous and may still contain patterns that allow for re-identification. Organizations must rigorously validate these datasets using privacy metrics and adversarial testing to ensure that sensitive information from the original records cannot be reconstructed or linked back to real individuals by malicious actors.

Why AI Compounds Risk:
AI Risk: AI models, particularly Large Language Models, can inadvertently memorize specific details from their training data rather than just learning general patterns. If these models are used to generate synthetic data without proper safeguards like differential privacy, they may replicate unique or rare data points that hackers can use to "reverse-engineer" and identify individuals in the source dataset.

Examples:
1. Conduct Membership Inference Attacks (MIAs) and Attribute Inference Attacks (AIAs) to determine if an attacker can identify whether a specific individual was part of the original training set or deduce sensitive hidden attributes.
2. Apply Differential Privacy (DP) techniques during the data generation process, which mathematically guarantees that the inclusion or exclusion of any single data point does not significantly change the output, effectively neutralizing re-identification risks.
3. Use the Distance to Closest Record (DCR) metric to measure the proximity between synthetic records and the original training data; if synthetic records are too close to real ones, they should be filtered out to prevent information leakage.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
