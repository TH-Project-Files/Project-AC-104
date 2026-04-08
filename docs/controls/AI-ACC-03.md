# AI-ACC-03: Enforce Aggressive Token Rotation: Implement automated rotation for all privileged credentials and shorten session token lifetimes to neutralize the persistence of AI-generated infostealers.

**Project:** Argus Centurion (AC-104)  
**Category:** Layer 5: Access Session  
**Implementation Group:** IG 2  
**Risk Level:** 1-High  
**Framework Mappings:** CIS v8: `6.1, 6.8` | NIST CSF: `PR.AA`

---

## Control Details
Detailed Description:
Aggressive token rotation involves automatically replacing refresh tokens every time they are used and significantly reducing the lifespan of active session tokens. By ensuring that each credential is valid for only a single use or a very narrow time window, organizations can invalidate stolen tokens before attackers can exploit them, effectively neutralizing the persistence of malware that harvests these secrets.

Why AI Compounds Risk:
AI exacerbates this risk by increasing the velocity and volume of non-human identity creation, which often leads to token sprawl and incomplete inventories. Furthermore, AI-generated infostealers can be developed more quickly and with more sophisticated evasion techniques, allowing them to silently scrape high-entropy tokens from AI configuration files and developer environments at scale.

Examples:
1. Configure OAuth 2.0 authorization servers to issue one-time-use refresh tokens that are immediately invalidated upon exchange for a new pair.
2. Set short access token lifetimes, such as 15 to 30 minutes, to shrink the window of opportunity for an attacker using a captured session.
3. Implement automated rotation for privileged non-human identities, such as service accounts and API keys, using centralized secrets management tools that track every creation and rotation event.

---
*Part of the Argus Centurion (AC-104) Open Source Security Framework.*
