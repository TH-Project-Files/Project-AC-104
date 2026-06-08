# AI-USR-11

**Category:** Layer 0: User Facing Controls  
**Implementation Group:** IG 2  
**Aggregate Risk Level:** 3-Low  
**CIS v8 Safeguards:** 6.1  
**NIST CSF Subcategories:** PR.AA  

## Recommendation Description
Require Possession-Factor Based Authentication (e.g., hardware tokens, device-bound keys) rather than Knowledge-Based ID for Service Desk verification and high-risk requests.

## Details
Detailed Description:
Shift identity verification for IT Service Desk interactions (e.g., password resets, MFA device additions) and critical financial requests away from knowledge-based factors (passwords, security questions, employee IDs) toward possession-based factors (something the user *has*). This ensures that even if an attacker successfully uses AI to mimic an employee's voice or steal their knowledge factors, they cannot bypass the physical hardware requirement to authorize the action.

Why AI Compounds Risk:
AI models can instantaneously scrape the internet, cross-reference breach databases, and solve knowledge-based verification questions. AI voice cloning and deepfakes completely defeat traditional knowledge-based identity verification over the phone, making the IT Helpdesk a massive vulnerability for social engineering. A true possession factor is cryptographically or physically bound to the user, making it immune to AI simulation and deepfakes.

Examples:
1. IT Service Desk Verification: When a user calls the helpdesk for a password reset or to register a new MFA device, the agent must verify their identity by sending a secure push notification or OTC to the user's pre-registered manager or an existing, trusted corporate device, rather than asking for their date of birth.
2. High-Value Financial Transfers: Enforce an out-of-band verification tool that sends a One-Time Code (OTC) or cryptographic push notification to a pre-registered personal mobile device before allowing a wire transfer.
3. Infrastructure Changes: Enforce FIDO2/WebAuthn hardware security keys (e.g., YubiKeys) for all privileged IT administrators and executives before allowing high-risk infrastructure changes.

## Implementation Status
- **Policy Defined:** 0
- **Control Implemented:** 0
- **Control Automated:** 0
- **Control Reported:** 0

**Assigned To:**   
**Notes/Evidence:**   
