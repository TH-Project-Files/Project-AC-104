# AI-LLM-20: Track exactly where your AI training data comes from to ensure hackers haven't poisoned it with malicious information.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 7: Internal LLMs & Agentics  
**Implementation Group:** IG 3  
**Risk Level:** 3-Low  
**Framework Mappings:** CIS v8: `15.1` | NIST CSF: `GV.SC`

---

## Control Details
Detailed Description:
Explanation: This recommendation refers to establishing data provenance, which is the ability to trace the origin, ownership, transformations, and generation of datasets used to train or fine-tune AI models. By documenting the historical record of data—including who created it, when it was created, and what changes were made—organizations can verify the authenticity and integrity of their information. This process allows developers to identify and filter out poisoned data, which is malicious or biased information intentionally injected by hackers to skew model outputs, create hidden backdoors, or degrade system performance.

Why AI Compounds Risk:
Why AI Exacerbates the Risk: AI models learn patterns and make decisions based entirely on the quality of their training data, meaning any foundational compromise is inherited and perpetuated throughout the model's operational lifetime. The complexity of AI often creates black boxes where it is difficult to see how data transformations lead to specific results, making subtle "stealth attacks" hard to detect through standard validation. Furthermore, the massive scale and speed of data ingestion in modern generative AI, which often involves scraping vast amounts of unverified web content, provide numerous entry points for attackers to silently plant malicious samples.

Examples:
1. Use automated tools to generate data provenance cards that summarize a dataset's creators, original sources, and license conditions to ensure all training material is reputable and legally compliant.
2. Adopt cryptographic authentication standards, such as digital signatures, to create tamper-proof records of the history of digital content, allowing the system to verify that the data has not been altered by an unauthorized party.
3. Establish a formal metadata management system that records column-level lineage, tracking every touchpoint and transformation a data asset undergoes from its original collection to its final use in the AI pipeline.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
