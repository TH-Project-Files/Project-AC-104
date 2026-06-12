# AI-END-11: Govern and restrict Endpoint-Hosted AI Runtimes and Browser AI Extensions (e.g., local LLMs, AI assistant plugins) to prevent local data leakage and unauthorized API binding.

**Category:** Endpoints (Layer 6: Endpoint Presentation)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 1.2, 3.6, 4.5  
**NIST CSF Subcategories:** PR.DS, DE.CM  
**Layered with:** AI-APP-02 (shadow AI discovery on devices and networks), AI-GOV-03 (the approved AI service catalog the allowlists enforce), AI-END-09 (application allowlisting for the runtimes themselves), AI-AGT-01 (governance of browser-driving agents — this control governs the extension/runtime attack surface they execute on)  

## Details
Detailed Description:
Use MDM and EDR to inventory and govern locally installed AI models and frameworks. Enforce local disk encryption for all cached prompts and vector embeddings stored by these tools. Implement host-based firewalls to prevent local AI runners from binding their API services to open network ports, which could expose the local model to other devices on the network.

This governance must extend to browser-based AI extensions: inventory all installed extensions via enterprise browser management, allowlist approved AI extensions and block the rest by default, review the permissions each approved extension requests (clipboard, DOM, cookies, tabs), and apply extension-aware DLP to prevent page content, clipboard data, or session material from being exfiltrated to third-party AI services.

Why AI Compounds Risk:
As "local LLM" frameworks (e.g., Ollama, LM Studio) become more popular, developers are downloading unvetted model weights and running them directly on their endpoints. These local setups bypass corporate AI Gateways and DLP controls. Furthermore, they often cache highly sensitive corporate prompts in plain text on the local disk and occasionally bind insecure API servers to public network interfaces (e.g., 0.0.0.0), exposing the endpoint to exploitation. Browser AI extensions compound the same risk from inside the browser session: a free "AI assistant" extension with broad permissions can silently read every rendered page, harvest clipboard contents and session cookies, and stream them to an unvetted third-party AI service — bypassing the AI Gateway, DLP, and network controls entirely because the exfiltration originates within the user's authenticated browser context.

Examples:
1. Configure host-based firewalls to restrict local AI frameworks from binding services to external network interfaces, restricting them strictly to localhost (127.0.0.1).
2. Enforce endpoint disk encryption (e.g., BitLocker, FileVault) to protect local model artifacts, cached prompt logs, and local vector embeddings from unauthorized physical access.
3. Use application allowlisting to prohibit the execution of unapproved local model runners and track all authorized endpoint-hosted AI deployments in the centralized asset inventory.
4. Use enterprise browser management (e.g., Chrome Browser Cloud Management, Edge administrative policies) to allowlist approved AI extensions, block all others by default, and audit approved extensions' permission grants for clipboard, DOM, cookie, or tab access on a recurring schedule.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
