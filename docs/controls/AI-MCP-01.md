# AI-MCP-01

**Category:** Layer 7: Application  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 1.1, 2.1, 4.1  
**NIST CSF Subcategories:** GV.SC, PR.DS  

## Recommendation Description
Implement an Enterprise Model Context Protocol (MCP) Registry to govern capability exposure, track server provenance, and detect capability drift.

## Details
Detailed Description:
Mandate that all MCP integrations—whether local stdio subprocesses or remote Streamable HTTP servers—are verified against an approved Enterprise MCP Registry. Deny-by-default any dynamic updates to an MCP server’s declared tools, resources, or prompts (listChanged notifications) until the new capabilities undergo a formal security review, preventing "rug pull" supply chain attacks.

Why AI Compounds Risk:
The Model Context Protocol (MCP) standardizes tool access, accelerating how rapidly AI agents can connect to disparate databases, APIs, and local files. Without a centralized registry to baseline capabilities, a benign third-party MCP server can silently update to include new, high-risk tools or request broader resource access without administrative oversight.

Examples:
1. Maintain an authoritative enterprise inventory of all MCP components, tracking their deployment type, declared capabilities, and approval status.
2. Configure the AI Gateway to intercept listChanged notifications, halting access to any newly declared MCP tools until they are reviewed and approved.
3. Disallow direct internet-based installations of third-party MCP servers, requiring all artifacts to be mirrored, hashed, and served from a vetted internal registry.

## Implementation Status
- **Policy Defined:** 0
- **Control Implemented:** 0
- **Control Automated:** 0
- **Control Reported:** 0

**Assigned To:**   
**Notes/Evidence:**   
