# AI-NET-11: Enforce front-door-only ingress: publish internet-facing services solely through consolidated, hardened front doors, require pre-authentication for every non-public application, and lock origins against direct access.

**Category:** Networking (Layer 3: Network)  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 1-High  
**CIS v8 Safeguards:** 4.4, 4.8, 6.3, 12.2  
**NIST CSF Subcategories:** PR.IR, PR.AA, ID.AM  
**Layered with:** AI-NET-08 (the outbound mirror of this control — gateway-only egress makes the AI Gateway unbypassable for outbound traffic; front-door-only ingress does the same for inbound traffic), AI-TRN-01 (transport-layer default-deny inbound, the port-level baseline this control extends to published services), AI-APP-05 and AI-APP-03 (the WAF and bot management that run on the front doors and are only effective when origins cannot be reached around them), AI-NET-05 and AI-APP-04 (attack surface scanning and OSINT portal discovery — the detective controls that measure this control's failures), AI-USR-08 (the phishing-resistant MFA the pre-authentication layer enforces), AI-MCP-01 (the registry of MCP servers, none of which should be anonymously reachable)  

## Details
Detailed Description:
Treat internet reachability as a privilege granted per service, not a default of the network. Every service reachable from the internet must satisfy four conditions: it is recorded in an exposure register with a named owner and a business justification; it is published through one of a small number of approved front doors (a reverse proxy, CDN, or load-balancer tier that terminates TLS and carries the WAF, bot management, rate limiting, and logging); its origin accepts traffic only from that front door; and, unless its content is deliberately public, the request is authenticated at the front door before any application code sees it. Anything reachable that fails one of these conditions is an incident, not a backlog item.

Pre-authentication is the default for everything not meant for the anonymous public: staff and internal web applications, administrative consoles, development and staging environments, dashboards, agent user interfaces, and model or agent APIs. An identity-aware proxy or zero-trust access layer integrated with the enterprise identity provider challenges the user first, so an application's own login page — and whatever vulnerabilities sit behind it — is never the first thing an unauthenticated internet client can reach. Endpoints that cannot perform an interactive sign-in (inbound webhooks, partner APIs, MCP servers) are still published on the same front doors and authenticated there by machine means: request signatures, mutual TLS, or OAuth client credentials.

Origin lockdown is what makes the front door a control rather than a suggestion. A WAF, an authentication rule, or a rate limit protects nothing if the origin answers requests that arrive around it. Origins must have no direct internet path: no public addresses where private connectivity is available, ingress restricted to the front door, and — because the address ranges of shared CDNs and cloud load balancers are shared with other tenants — a second check such as mutual TLS or a secret header that only the front door can supply.

Minimum Requirements for Any Internet-Reachable Service:
- An entry in the exposure register: hostname, owner, justification, front door, and authentication mode (public by design, pre-authenticated, or machine-authenticated)
- Publication only through an approved front door carrying TLS, WAF, rate limiting, and centralized logging
- An origin that is unreachable from the internet except through that front door, verified by test rather than by configuration review
- Pre-authentication at the front door unless the register records the service as public by design
- Automated detection when any of the above stops being true: a new public listener, a detached WAF or authentication rule, or a DNS record pointing at an origin

Why AI Compounds Risk:
Internet-wide reconnaissance is now continuous and automated. Adversaries use AI-driven tooling to enumerate hostnames from certificate-transparency logs and DNS, fingerprint what they find, and produce working exploits for newly disclosed vulnerabilities quickly enough that a pre-authentication flaw in any reachable application is tested long before a patch cycle completes. Exposure is no longer bounded by how interesting a system is — only by whether it answers.

AI also multiplies what answers. AI-assisted development produces internal tools, dashboards, agent endpoints, and MCP servers faster than security review can keep pace, each one tempted to ship with its own login page behind a default public load balancer. Agentic systems raise the stakes of every such endpoint: an anonymous request that reaches an agent or tool server is not merely a web request but a prompt-injection attempt against something holding tools and credentials, and an anonymous request that reaches an inference endpoint spends the organization's compute budget (Denial of Wallet).

Front-door-only ingress collapses the problem. Hundreds of applications of uneven quality become unreachable to anonymous clients, and the attack surface shrinks to a few hardened front doors and the identity provider — components that can be patched, monitored, and tested once on behalf of everything behind them. The reasoning that makes AI-NET-08's gateway unbypassable for outbound AI traffic applies equally inbound: automated reconnaissance routinely recovers origin addresses from historical DNS records, certificates, and cloud address ranges, so a front door that can be walked around will be.

Examples:
1. Maintain an exposure register and reconcile it automatically, at least daily, against cloud inventory (load balancers, CDN distributions, public addresses, API gateways) and public DNS. A reachable service with no register entry, no owner, or no front door is opened as an incident and unpublished until it qualifies.
2. Place every non-public web application, administrative console, non-production environment, and agent interface behind an identity-aware proxy or zero-trust access service (e.g., OIDC authentication at the load balancer, an identity provider's access gateway, or a cloud provider's identity-aware proxy) enforcing phishing-resistant MFA, so that unauthenticated requests are redirected to the identity provider and never reach application code.
3. Lock origins to their front doors: remove public addresses from origin hosts, restrict ingress to the front door's managed prefix list or private connectivity, and require mutual TLS or a rotated secret header between front door and origin. Prove it on a schedule by requesting each origin directly from an external vantage point and alerting on any response.
4. Publish machine-facing endpoints (inbound webhooks, partner APIs, MCP servers, inference APIs) through the same front doors with machine authentication — signature verification, mutual TLS, or OAuth client credentials — plus per-client rate limits and source allowlists where the sender publishes its ranges. An agent that must serve anonymous visitors (e.g., a public chat widget) is registered as public by design and compensated with origin-restricted embedding, per-visitor rate and spend caps, and a tool set limited to public data.
5. Prevent drift with policy-as-code: deny, in infrastructure pipelines and cloud organization policies, the creation of public load balancers, public addresses, and open ingress rules outside the approved front-door accounts and subnets. Alert within minutes when a deployment detaches a WAF or authentication rule from a front door or stands up a new public listener, and route the event into the AI-DET-01 detection pipeline.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
