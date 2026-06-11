"""One-time editorial cleanup for AC-104 v1.2.0 (review §7).

Transforms: domain taxonomy convergence, template unification, technical-register
retitling, NIST CSF 2.0 vocabulary conversion, artifact fixes, weak-claim rewrites.
Applies consistently to docs/controls/*.md, data/AC-104-v1.2.0.csv, docs/controls_list.md.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTROLS = ROOT / "docs" / "controls"
CSV = ROOT / "data" / "AC-104-v1.2.0.csv"
LIST = ROOT / "docs" / "controls_list.md"

# --- 1. Domain taxonomy (by ID prefix); old layer kept as sub-tag -------------
PREFIX_DOMAIN = {
    "GOV": "Governance & People", "VND": "Governance & People",
    "LOG": "Governance & People", "USR": "Governance & People",
    "DET": "Governance & People", "DEF": "Governance & People",
    "REC": "Governance & People",
    "ACC": "Identity & Access", "AUTH": "Identity & Access",
    "PAM": "Identity & Access", "NHI": "Identity & Access",
    "NET": "Networking", "TRN": "Networking", "DLK": "Networking",
    "END": "Endpoints",
    "APP": "Applications & Data", "MSG": "Applications & Data",
    "LLM": "Applications & Data", "AGT": "Applications & Data",
    "MCP": "Applications & Data", "RAG": "Applications & Data",
}

def domain_for(cid: str) -> str:
    return PREFIX_DOMAIN[cid.split("-")[1]]

# --- 2. Technical-register titles (old -> new); comma-free new titles ----------
TITLES = {
    "AI-LLM-01": ("Put strict network filters around your internal AI models so hackers can't steal or copy the AI's core logic.",
                  "Enforce network isolation and strict API access controls around internal model infrastructure to prevent model theft and extraction."),
    "AI-LLM-02": ("Put speed limits on AI agents so they don't get stuck in endless loops or crash internal systems.",
                  "Enforce rate limiting and execution constraints on AI agents to prevent runaway loops and resource exhaustion."),
    "AI-LLM-03": ("Give AI agents only the bare minimum permissions needed to do their jobs.",
                  "Enforce least-privilege permissions for AI agents."),
    "AI-LLM-04": ("Keep detailed records of everything AI agents do, including the prompts they receive and actions they take.",
                  "Implement comprehensive audit logging of AI agent prompts and actions."),
    "AI-LLM-05": ("Test any fake (synthetic) or anonymized data to make sure hackers can't reverse-engineer it to find real people's identities.",
                  "Adversarially test synthetic and anonymized datasets against re-identification attacks."),
    "AI-LLM-07": ("Automatically scan and clean up the text users send to AI to stop them from sharing too much sensitive information.",
                  "Implement automated prompt scanning and sensitive-data redaction on AI inputs."),
    "AI-LLM-08": ("Require a human to review and approve any important or risky actions taken by AI.",
                  "Require human-in-the-loop review and approval for high-risk AI actions."),
    "AI-LLM-09": ("Create strict 'allow-lists' so AI agents can only talk to approved websites or internal systems.",
                  "Enforce deny-by-default allowlists restricting AI agent egress to approved endpoints and systems."),
    "AI-LLM-10": ("Thoroughly test and review the code and instructions for AI agents before letting them run in the real world.",
                  "Mandate pre-deployment testing and review of AI agent code and instructions."),
    "AI-LLM-11": ("Continuously scan and classify sensitive company data so you know exactly what information AI tools might access.",
                  "Continuously discover and classify sensitive data accessible to AI systems."),
    "AI-LLM-12": ("Put strict safety checks in place when letting AI talk directly to your company databases (like translating plain text into SQL queries).",
                  "Enforce parameterized queries and least-privilege database access for natural-language-to-SQL workflows."),
    "AI-LLM-13": ("Ensure that when AI tools talk to each other or use plugins, they prove who they are and only share the minimum necessary data.",
                  "Require authenticated and minimally-scoped agent-to-agent and plugin interactions."),
    "AI-LLM-14": ("Set up alerts to notify security teams if an AI agent starts behaving unexpectedly or out-of-bounds.",
                  "Implement behavioral anomaly alerting for out-of-bounds AI agent activity."),
    "AI-LLM-15": ("Protect the specialized databases that feed knowledge to your AI (Vector Stores) with encryption and strict access rules.",
                  "Encrypt and enforce strict access controls on vector stores and embedding databases."),
    "AI-LLM-16": ("Regularly test internal AI systems by having security teams pretend to be hackers (Red Teaming) to find weak spots.",
                  "Conduct recurring red-team exercises against internal AI systems."),
    "AI-LLM-17": ("Force AI tools that write or run code to do so in a secure, isolated bubble (sandbox) so they can't break anything on the network.",
                  "Sandbox all AI-generated code execution in isolated runtimes."),
    "AI-LLM-18": ("Keep different users' AI chats strictly separated so one person's data doesn't accidentally leak into another person's chat.",
                  "Enforce strict per-user session and context isolation in multi-tenant AI applications."),
    "AI-LLM-19": ("Keep a 'nutrition label' (Bill of Materials) for your AI models and verify that no one has tampered with their code or plugins.",
                  "Maintain an AI Bill of Materials (AIBOM) and verify model and plugin integrity."),
    "AI-LLM-20": ("Track exactly where your AI training data comes from to ensure hackers haven't poisoned it with malicious information.",
                  "Enforce training-data provenance tracking to detect and prevent data poisoning."),
    "AI-LLM-21": ("Install data loss prevention (DLP) tools to stop AI agents from accidentally or maliciously leaking sensitive company data.",
                  "Deploy semantic-aware DLP on AI agent inputs and outputs to prevent data leakage."),
    "AI-ACC-06": ("Implement Context-Aware Authentication (e.g. typing cadence, location)",
                  "Implement Context-Aware Authentication (e.g. location, device posture, time-of-access)"),
    "AI-AUTH-03": ("Enable immediate, un-mutable out-of-band notifications for all critical account changes (e.g., password reset, MFA device addition).",
                   "Enable immediate multi-channel out-of-band notifications for all critical account changes (e.g., password reset, MFA device addition)."),
    "AI-GOV-14": ("Implement Cryptographic Provenance (e.g., C2PA standards) for all official university executive media to establish verifiable digital trust.",
                  "Implement Cryptographic Provenance (e.g., C2PA standards) for all official executive and corporate media to establish verifiable digital trust."),
}

# --- 3. NIST CSF 1.1 / invented vocabulary -> CSF 2.0 (longest first) ----------
NIST_MAP = [
    ("PR.PT-4", "PR.PS"), ("PR.DS-2", "PR.DS"), ("PR.DS-5", "PR.DS"),
    ("PR.DS-6", "PR.DS"), ("DE.CM-1", "DE.CM"), ("DE.CM-8", "DE.CM"),
    ("ID.RA-1", "ID.RA"), ("ID.RA-3", "ID.RA"), ("ID.RA-5", "ID.RA"),
    ("ID.SC-1", "GV.SC"), ("ID.SC", "GV.SC"), ("PR.AC", "PR.AA"),
    ("PR.PT", "PR.PS"), ("PR.IP", "PR.PS"), ("PR.MA", "PR.PS"),
    ("PR.NW", "PR.IR"), ("DE.CT", "DE.CM"), ("DE.AS", "DE.CM"),
]

# --- 4. Content fixes (exact-string; applied to md and, csv-escaped, to CSV) ---
CONTENT_FIXES = [
    # APP-04 redaction artifacts
    (r"site:\[suspicious link removed\]", "site:example.com"),
    ("site:[suspicious link removed]", "site:example.com"),
    # GOV-14 university scoping (title handled in TITLES)
    ("official university media", "official corporate media"),
    # ACC-06 typing-cadence claim
    ("and behavioral patterns like typing cadence", "and network context"),
    # AUTH-03 un-mutable reframe
    ("These notifications must be un-mutable, meaning an attacker cannot suppress or turn them off even if they gain access to the account settings.",
     "Deliver these alerts to multiple, pre-registered out-of-band channels (e.g., push plus a secondary email or SMS) so that an attacker who controls one channel cannot suppress them all, and remove the ability for end-users to disable security alerts through self-service settings."),
    ("Configure your Identity Provider (IdP) to send mandatory, un-suppressible push alerts",
     "Configure your Identity Provider (IdP) to send mandatory push alerts (not suppressible through self-service settings)"),
    # USR-06 modernization
    ("The goal is to identify whether the correspondent is a human or an automated AI bot by observing if the entity can handle complex, emotional, or highly contextual nuances that typically trip up artificial intelligence.",
     "Because modern LLMs handle humor, idiom, and contextual nuance convincingly, the training emphasizes procedural verification—moving the interaction to an authenticated, out-of-band channel (see AI-USR-04)—over conversational 'gotcha' tests, while teaching the behavioral red flags that persist regardless of conversational fluency."),
    ("1. Conduct role-play simulations where employees must interact with known AI bots and attempt to \"break\" the bot's logic using non-sequiturs, complex emotional queries, or requests for meta-communication about the conversation itself.\n2. Educate staff to look for \"machine-like\" consistency or lack of situational awareness, such as an entity providing perfect, immediate responses to complex data requests while failing to understand simple, culturally specific jokes or idiomatic expressions.\n3. Implement \"Human Verification\" drills in standard communication workflows, where staff are trained to occasionally insert specific \"logic traps\" or context-heavy questions into suspicious email threads to see if the recipient responds with the rigid, pattern-based logic characteristic of an LLM.",
     "1. Train staff that the reliable test is procedural, not conversational: a legitimate correspondent can always move to an authenticated channel (a known phone number, or a video call with the liveness checks defined in AI-USR-04), while bots and impersonators will resist or deflect out-of-band verification.\n2. Educate staff on behavioral red flags that persist even in fluent AI conversation: manufactured urgency, refusal to use established channels, requests that bypass normal process, and inconsistency about shared history or recent in-person interactions.\n3. Run periodic simulations where employees interact with current-generation LLM bots to demonstrate that fluency, humor, and cultural context are no longer reliable discriminators—reinforcing that out-of-band verification, not conversational testing, is the dependable control."),
    # LLM-18 draft "Why" + misnumbered examples
    ("Why AI Compounds Risk:\nWhy AI Exacerbates the Risk:\n\nExamples:\n1. Data Training Loops: Many AI models use human inputs to improve and retrain themselves, meaning sensitive data shared by one user could potentially be generated as an answer for a different user in the future.\n2. Context and Memory Features: Modern AI assistants often use persistent memory or long context windows to recall past interactions; without strict separation, these features can mistakenly retrieve and display private details from a separate user's session.\n3. LLM Scope Violations: AI agents often have the ability to call external tools or databases; poor session management can lead to the AI unintentionally retrieving and leaking internal organizational data to unauthorized employees during a prompt.\n4. Corporate Implementation Examples:\n5. Unique Session Identifiers:",
     "Why AI Compounds Risk:\nSession-isolation failures are amplified by three AI-specific mechanisms. Data training loops: models that learn from user inputs can surface one user's sensitive data in another user's answers. Context and memory features: persistent memory and long context windows can mistakenly retrieve private details from a separate user's session. Scope violations: agents that call external tools or databases under poor session management can retrieve and leak internal data to unauthorized employees during a prompt.\n\nExamples:\n1. Unique Session Identifiers:"),
    ("6. Enterprise Managed Environments:", "2. Enterprise Managed Environments:"),
    ("7. Robust Backend Security Rules:", "3. Robust Backend Security Rules:"),
]

FOOTER = "---\n*Part of the Argus Centurion (AC-104) Open Source Security Framework.*\n"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8-sig")


def write(p: Path, text: str, bom: bool) -> None:
    p.write_text(text, encoding="utf-8-sig" if bom else "utf-8", newline="\n")


def has_bom(p: Path) -> bool:
    return p.read_bytes()[:3] == b"\xef\xbb\xbf"


def convert_nist(text: str) -> str:
    for old, new in NIST_MAP:
        text = text.replace(old, new)
    # collapse adjacent duplicates produced by conversion (e.g. "PR.DS, PR.DS")
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r"\b([A-Z]{2}\.[A-Z]{2}), \1\b", r"\1", text)
    return text


def apply_content_fixes(text: str, csv_mode: bool = False) -> str:
    for old, new in CONTENT_FIXES:
        text = text.replace(old, new)
        if csv_mode:
            text = text.replace(old.replace('"', '""'), new.replace('"', '""'))
    return text


def apply_titles(text: str, csv_mode: bool = False) -> str:
    for cid, (old, new) in TITLES.items():
        text = text.replace(old, new)
        if csv_mode:
            text = text.replace(old.replace('"', '""'), new.replace('"', '""'))
    return text


def process_md(p: Path) -> None:
    cid = p.stem
    bom = has_bom(p)
    text = read(p)

    # Template unification: newer-template files (ID-only H1, Rec Desc section)
    m = re.search(r"## Recommendation Description\n(.*?)\n(?=\n|##)", text, re.S)
    if m:
        title = m.group(1).strip().splitlines()[0].strip()
        text = re.sub(rf"^# {re.escape(cid)}\s*$", f"# {cid}: {title}",
                      text, count=1, flags=re.M)
        text = re.sub(r"## Recommendation Description\n.*?\n\n", "", text,
                      count=1, flags=re.S)
    # Strip Implementation Status tracking block (belongs in the CSV tracker)
    text = re.sub(r"\n## Implementation Status\n(?:.*\n)*?\*\*Notes/Evidence:\*\*[^\n]*\n?",
                  "\n", text)
    # Older-template fields -> unified (newer) field names
    text = re.sub(r"^\*\*Project:\*\* Argus Centurion \(AC-104\)\s*\n", "",
                  text, flags=re.M)
    text = text.replace("**Risk Level:**", "**Aggregate Risk Level:**")
    text = re.sub(
        r"\*\*Framework Mappings:\*\* CIS v8: `([^`]*)` \| NIST CSF: `([^`]*)`",
        r"**CIS v8 Safeguards:** \1  \n**NIST CSF Subcategories:** \2",
        text)
    text = text.replace("## Control Details", "## Details")

    # Taxonomy: Category -> Domain (old layer)
    text = re.sub(r"^\*\*Category:\*\* (Layer [^\n]+?)\s*$",
                  lambda mm: f"**Category:** {domain_for(cid)} ({mm.group(1).rstrip()})  ",
                  text, flags=re.M)

    # GOV-02 CIS mapping fix (data classification belongs to CIS Control 3)
    if cid == "AI-GOV-02":
        text = text.replace("15.1, 17.1", "3.2, 3.7")

    text = convert_nist(text)
    text = apply_titles(text)
    text = apply_content_fixes(text)

    # Consistent footer
    if "Part of the Argus Centurion" not in text:
        if not text.endswith("\n"):
            text += "\n"
        text += "\n" + FOOTER
    write(p, text, bom)


def process_csv(p: Path) -> None:
    bom = has_bom(p)
    text = read(p)
    lines = text.split("\n")
    out, current = [], None
    for line in lines:
        m = re.match(r"^(AI-[A-Z]+-\d+),([^,\"]+),", line)
        if m:
            current = m.group(1)
            old_cat = m.group(2)
            line = line.replace(f"{current},{old_cat},",
                                f"{current},{domain_for(current)} ({old_cat}),", 1)
        if current == "AI-GOV-02":
            line = line.replace("15.1, 17.1", "3.2, 3.7")
        out.append(line)
    text = "\n".join(out)
    text = convert_nist(text)
    text = apply_titles(text, csv_mode=True)
    text = apply_content_fixes(text, csv_mode=True)
    write(p, text, bom)


def process_list(p: Path) -> None:
    bom = has_bom(p)
    text = read(p)

    def fix_row(mm):
        cid, link, cat = mm.group(1), mm.group(2), mm.group(3).strip()
        return f"| **[{cid}]({link})** | {domain_for(cid)} ({cat}) |"

    text = re.sub(r"\| \*\*\[(AI-[A-Z]+-\d+)\]\(([^)]+)\)\*\* \| (Layer [^|]+) \|",
                  fix_row, text)
    text = apply_titles(text)
    write(p, text, bom)


def main() -> None:
    for p in sorted(CONTROLS.glob("AI-*.md")):
        process_md(p)
    process_csv(CSV)
    process_list(LIST)
    print("done")


if __name__ == "__main__":
    sys.exit(main())
