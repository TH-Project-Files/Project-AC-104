# AI-ACC-02: Implement Concurrent Login Restrictions

**Category:** Identity & Access (Layer 5: Access Session)  
**Implementation Group:** IG 1  
**Aggregate Risk Level:** 2-Medium  
**CIS v8 Safeguards:** 6.1, 6.8  
**NIST CSF Subcategories:** PR.AA

---

## Details
Detailed Description:
Implement Concurrent Login Restrictions is a security measure that limits the number of simultaneous active sessions a single user account can maintain across different devices or locations. This control prevents "shadow access," where unauthorized users masquerade as legitimate ones, and ensures that user activity can be accurately attributed to a unique individual.

Why AI Compounds Risk:
AI exacerbates this risk because AI agents and autonomous browsers often operate with full user-level privileges, inheriting the user's digital identity across multiple SaaS applications and internal tools. These agents can perform background tasks, automated workflows, and internal reconnaissance without triggering traditional session-focused alerts or interactive login signals, effectively acting as an over-privileged insider threat.

Examples:
1. Use third-party identity management tools to define maximum session counts (e.g., limiting to 1 session for VPN or Wi-Fi) and set policies to either deny new logins or terminate the oldest active session when limits are reached.
2. Configure application-level settings to restrict concurrent logins per application or realm.
3. Implement Identity Provider (IDP) security features like IP filtering, certificate-based authentication, and automated session invalidation tokens that overwrite and expire previous sessions upon a new login from a different device.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
