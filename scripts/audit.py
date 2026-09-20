#!/usr/bin/env python3
"""Content audit for the built site (CLAUDE.md § 11).

Greps the BUILT _site/ (HTML and, where pdftotext is available, PDF) for
withdrawn claims (T4), self-reported claims that must never appear here (T3),
private material, and stale time-sensitive wording.

This list is a snapshot, hand-derived from job-application's
02-personal-wiki/profile/02-claims.md T4 table and CLAUDE.md § 4/§ 11. It is
NOT read live from that repo: this repo must never depend on job-application
at build time (CLAUDE.md § 5 — the two repos are separate on purpose, and a
public CI run has no access to the private repo anyway). That means this
list goes stale exactly the way CLAUDE.md § 11 warns about, silently, unless
a human re-derives it against the current T4 table before every push that
might be affected. Re-derived 2026-09-20 against the T4 table as of that
date — check it again next time a claim is withdrawn or a private detail
changes.

Exit code 0: clean. Exit code 1: at least one match, printed with its file
and pattern so the offending line can be found and fixed at the source
(the .qmd, not this script).
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent / "_site"


@dataclass
class Rule:
    category: str  # T4, T3, Private, Stale
    label: str  # short human name for the finding
    pattern: re.Pattern[str]


def rx(*patterns: str) -> re.Pattern[str]:
    return re.compile("|".join(patterns), re.IGNORECASE)


# --- T4: withdrawn claims -----------------------------------------------
# One rule per row of 02-claims.md's T4 table (job-application repo) as of
# 2026-09-20. Patterns are deliberately narrow enough to avoid flagging the
# true, correctly-scoped wording that replaced each withdrawn claim.
T4_RULES = [
    Rule("T4", "first author on both interventional papers",
         rx(r"first author on (both|two) interventional")),
    Rule("T4", "IMPETUS as first-author",
         rx(r"first[- ]author.{0,40}IMPETUS", r"IMPETUS.{0,40}first[- ]author")),
    Rule("T4", "SAS reading ability",
         rx(r"\bread(ing)?\b.{0,20}\bSAS\b", r"\bSAS\b.{0,20}\bproficien")),
    Rule("T4", "20+ sample-size calculations",
         rx(r"\b20\s*\+\s*(sample[- ]size|power)\b")),
    Rule("T4", "non-inferiority design",
         rx(r"non[- ]inferiority")),
    Rule("T4", "sole study statistician (unqualified)",
         rx(r"\bsole\b.{0,20}\bstudy statistician\b", r"\bonly statistician\b",
            r"\bentire methodology single-handed\b")),
    Rule("T4", "GCP certification in progress",
         rx(r"\bGCP\b.{0,20}(in progress|certified|certification)",
            r"\bGCP\b(?!.{0,15}\bgap\b)")),
    Rule("T4", "ran/led the consulting service",
         rx(r"\b(ran|led|leitete)\b.{0,25}\b(consulting service|statistischen Beratung)\b")),
    Rule("T4", "immunology expertise",
         rx(r"\bimmunology expertise\b", r"\bimmunologische Expertise\b")),
    Rule("T4", "Shockwave registry",
         rx(r"\bShockwave\b")),
    Rule("T4", "multiplicity control in nearly all work",
         rx(r"\bmultiplicity control\b.{0,30}\b(nearly all|most|all)\b")),
    Rule("T4", "available in/from October (stale date)",
         rx(r"\bavailable (in|from) October\b", r"\bverf(ü|ue)gbar ab Oktober\b")),
    Rule("T4", "metabolomics manuscript as submitted/under review",
         # EN "under review" / "submitted"; DE "in Begutachtung" / "eingereicht" —
         # only a problem when attached to the metabolomics/GGM manuscript context.
         rx(r"metabolomic\w*[^.]{0,80}\b(under review|submitted)\b",
            r"\b(under review|submitted)\b[^.]{0,80}metabolomic",
            r"[Mm]etabolomic\w*[^.]{0,80}(in Begutachtung|eingereicht)",
            r"(in Begutachtung|eingereicht)[^.]{0,80}[Mm]etabolomic")),
    Rule("T4", "PhD submission date",
         rx(r"\bend 2026\b.{0,20}\b(PhD|doctorate|Promotion|dissertation)",
            r"\bearly 2027\b.{0,20}\b(PhD|doctorate|Promotion|dissertation)",
            r"\bEnde 2026\b.{0,20}\bPromotion", r"\bAnfang 2027\b.{0,20}\bPromotion")),
    Rule("T4", "Research Associate / Wissenschaftlicher Mitarbeiter at Helmholtz",
         rx(r"Research Associate.{0,20}Helmholtz", r"Wissenschaftlicher Mitarbeiter.{0,20}Helmholtz")),
    Rule("T4", "genomic analysis of familial pancreatic cancer (unqualified)",
         rx(r"\b(ran|conducted|performed|led)\b.{0,25}genomic analys(is|es)")),
    Rule("T4", "ING internship",
         rx(r"\bING\b.{0,15}(Insurance|Versicherung)")),
    Rule("T4", "Helmholtz counted as a year",
         rx(r"\bHelmholtz\b[^.]{0,60}\b(a|one|1)\s+year\b",
            r"\bHelmholtz\b[^.]{0,60}\b(ein|1)\s+Jahr\b")),
    Rule("T4", "advanced/proficient Python",
         rx(r"\b(advanced proficiency in|proficient in)\s+Python\b",
            r"\bfortgeschrittene\b.{0,15}\bPython\b")),
    Rule("T4", "Azure/cloud as experience",
         rx(r"\bAzure\b.{0,30}\b(experience|Erfahrung)\b(?!.{0,20}\bgap\b)")),
    Rule("T4", "HPC cluster / Slurm for the M.Sc. thesis",
         rx(r"\bHPC\b.{0,20}\bcluster\b", r"\bSlurm\b")),
    Rule("T4", "recurrent-event sample-size planning (pre-2023 FAMOUS calc)",
         rx(r"recurrent-event sample-size planning",
            r"Fallzahlplanung f(ü|ue)r rekurrente Ereignisse")),
    Rule("T4", "doctoral research since 2023 / seit 2023",
         rx(r"\bsince 2023\b.{0,15}\b(research|doctoral)",
            r"\bseit 2023\b", r"\b2023\s*[-–—]\s*present\b")),
    Rule("T4", "authored statistical sections of a study protocol",
         rx(r"authored the statistical sections of a study protocol",
            r"Erstellung.{0,10}(Abschnitte|statistischen Abschnitte).{0,10}Studienprotokoll")),
    Rule("T4", "doctorate berufsbegleitend/part-time",
         rx(r"\bberufsbegleitend\b", r"\bpart[- ]time\b.{0,30}\b(PhD|doctorate|Promotion|dissertation)")),
]

# --- T3: self-reported, never on this site --------------------------------
T3_RULES = [
    Rule("T3", "RAG", rx(r"\bRAG\b(?!\w)")),
    Rule("T3", "agentic workflows", rx(r"\bagentic workflows?\b")),
    Rule("T3", "LLM tooling", rx(r"\bLLM tooling\b")),
]

# --- Private material -------------------------------------------------
PRIVATE_RULES = [
    Rule("Private", "street address", rx(r"\bDagobertstra(ß|ss)e\b")),
    Rule("Private", "phone number", rx(r"\+49\s*151\s*54107067", r"0151[\s./-]?54107067")),
    Rule("Private", "date of birth", rx(r"\bGeburtsdatum\b")),
    Rule("Private", "grades",
         rx(r"\b2[.,]52\b", r"\bbefriedigend\b", r"\bSecond Class Honours\b", r"\b49[.,]5\s*%")),
]

# --- Stale time-sensitive wording --------------------------------------
STALE_RULES = [
    Rule("Stale", "available immediately / ab sofort",
         rx(r"\bavailable immediately\b", r"\bab sofort\b")),
]

ALL_RULES = T4_RULES + T3_RULES + PRIVATE_RULES + STALE_RULES


def extract_text(path: Path) -> str | None:
    if path.suffix == ".pdf":
        if shutil.which("pdftotext") is None:
            print(f"WARN: pdftotext not found, skipping PDF text check for {path}",
                  file=sys.stderr)
            return None
        result = subprocess.run(
            ["pdftotext", str(path), "-"], capture_output=True, text=True, check=False
        )
        if result.returncode != 0:
            print(f"WARN: pdftotext failed on {path}: {result.stderr.strip()}",
                  file=sys.stderr)
            return None
        return result.stdout
    if path.suffix in (".html", ".htm", ".xml"):
        return path.read_text(encoding="utf-8", errors="replace")
    return None


def main() -> int:
    if not SITE_DIR.exists():
        print(f"ERROR: {SITE_DIR} does not exist — render the site first "
              "(quarto render, then cd de && quarto render).", file=sys.stderr)
        return 2

    findings: list[tuple[Path, Rule, str]] = []
    for path in sorted(SITE_DIR.rglob("*")):
        if not path.is_file():
            continue
        if "site_libs" in path.parts:  # vendored JS/CSS, not content
            continue
        text = extract_text(path)
        if text is None:
            continue
        for rule in ALL_RULES:
            m = rule.pattern.search(text)
            if m:
                findings.append((path.relative_to(SITE_DIR), rule, m.group(0)))

    if not findings:
        print(f"Audit clean — 0 matches across {sum(1 for _ in SITE_DIR.rglob('*') if _.is_file())} built files.")
        return 0

    print(f"AUDIT FAILED — {len(findings)} finding(s):\n", file=sys.stderr)
    for rel_path, rule, matched_text in findings:
        print(f"  [{rule.category}] {rule.label}", file=sys.stderr)
        print(f"    file: _site/{rel_path}", file=sys.stderr)
        print(f"    matched: {matched_text!r}\n", file=sys.stderr)
    print(
        "Fix at the source (the .qmd), not in the build output. If a match is a "
        "false positive (the surrounding sentence is actually fine), narrow the "
        "rule's pattern in scripts/audit.py rather than deleting the rule.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
