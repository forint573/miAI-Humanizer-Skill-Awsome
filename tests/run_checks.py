#!/usr/bin/env python3
"""
run_checks.py — automated checks for HumanCopywrite.

Dependency-free (standard library only). Validates the skill package structure
and exercises the heuristic scanner end-to-end. Exits non-zero on any failure
so it can gate CI.

Usage:
  python tests/run_checks.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "human-copywrite"
SCANNER = SKILL_DIR / "scripts" / "copy_scan.py"

failures: list[str] = []
passes = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global passes
    if condition:
        passes += 1
        print(f"  PASS  {name}")
    else:
        failures.append(name if not detail else f"{name} — {detail}")
        print(f"  FAIL  {name}" + (f" — {detail}" if detail else ""))


def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal YAML frontmatter parser: top-level `key: value` pairs only."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in block:
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def section(title: str) -> None:
    print(f"\n{title}")


# --- 1. Package structure ---------------------------------------------------
section("Skill structure")

expected_files = [
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "README.md",
    SKILL_DIR / "references" / "process-bleed.md",
    SKILL_DIR / "references" / "website-copy.md",
    SKILL_DIR / "references" / "voice-setup.md",
    SKILL_DIR / "references" / "substance.md",
    SKILL_DIR / "references" / "integrity.md",
    SKILL_DIR / "references" / "ai-tells.md",
    SKILL_DIR / "references" / "qa-scorecard.md",
    SKILL_DIR / "references" / "voice-calibration.md",
    SKILL_DIR / "references" / "translation-handoff.md",
    SKILL_DIR / "scripts" / "copy_scan.py",
    SKILL_DIR / "tests" / "test-prompts.md",
]
for path in expected_files:
    check(f"exists: {path.relative_to(ROOT)}", path.is_file())


# --- 2. SKILL.md frontmatter ------------------------------------------------
section("SKILL.md frontmatter")

skill_md = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
fm = parse_frontmatter(skill_md)
check("has frontmatter name", "name" in fm)
check("has frontmatter description", "description" in fm)
check(
    "name matches folder",
    fm.get("name") == SKILL_DIR.name,
    f"frontmatter name={fm.get('name')!r}, folder={SKILL_DIR.name!r}",
)
desc_len = len(fm.get("description", ""))
check(
    "description within practical length (<=1024)",
    0 < desc_len <= 1024,
    f"length={desc_len}",
)


# --- 3. Referenced files actually exist -------------------------------------
section("Internal references resolve")

for ref in ["references/process-bleed.md", "references/website-copy.md",
            "references/voice-setup.md", "references/substance.md",
            "references/integrity.md", "references/ai-tells.md",
            "references/qa-scorecard.md", "references/voice-calibration.md",
            "references/translation-handoff.md", "scripts/copy_scan.py"]:
    check(f"SKILL.md mentions {ref}", ref in skill_md)


# --- 3b. Model calibration structure (v4) ------------------------------------
section("Model calibration structure (v4)")

check("SKILL.md has an output contract", "## The output contract" in skill_md)
check("SKILL.md has an edit bar", "## The edit bar" in skill_md)
check("SKILL.md defines the cluster threshold", "150-word span" in skill_md)
check("SKILL.md has reference load triggers", "## When to load references" in skill_md)
check("SKILL.md states whole-deliverable scope", "entire deliverable" in skill_md)
check("SKILL.md has a fact-safety section", "## Fact safety" in skill_md)
check(
    "fact safety keeps user specifics and flags them",
    "list it under `Verify`" in skill_md,
)
check("output contract names its exceptions", "Two exceptions" in skill_md)
check(
    "scanner instruction is gated on script execution",
    "When you can execute scripts" in skill_md,
)
check(
    "SKILL.md teaches the transcript-transplant rule",
    "transcript transplant" in skill_md,
)
check("SKILL.md has the source sheet", "source sheet" in skill_md)
check("SKILL.md wires MY_OWN_VOICE.md", "MY_OWN_VOICE.md" in skill_md)

pb_md = (SKILL_DIR / "references" / "process-bleed.md").read_text(encoding="utf-8")
check("process-bleed has eight leak types", "Eight leak types" in pb_md)
check("process-bleed includes the transcript transplant", "Transcript transplant" in pb_md)

voice_setup_md = (SKILL_DIR / "references" / "voice-setup.md").read_text(encoding="utf-8")
check("voice-setup carries the MY_OWN_VOICE template", "# MY_OWN_VOICE" in voice_setup_md)

ai_tells_md = (SKILL_DIR / "references" / "ai-tells.md").read_text(encoding="utf-8")
bar_tags = ai_tells_md.count("**Bar:")
check("ai-tells items carry bar tags (>=33)", bar_tags >= 33, f"found {bar_tags}")
check("ai-tells has always-bar items", "**Bar: always" in ai_tells_md)
check("ai-tells has cluster-bar items", "**Bar: cluster" in ai_tells_md)

voice_md = (SKILL_DIR / "references" / "voice-calibration.md").read_text(encoding="utf-8")
check("voice guide has the propose-directions move", "Propose voice directions" in voice_md)


# --- 4. Scanner compiles ----------------------------------------------------
section("Scanner compiles")

compile_proc = subprocess.run(
    [sys.executable, "-m", "py_compile", str(SCANNER)],
    capture_output=True, text=True,
)
check("copy_scan.py compiles", compile_proc.returncode == 0, compile_proc.stderr.strip())


def run_scanner(text: str) -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCANNER)],
        input=text, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"scanner failed: {proc.stderr}")
    return json.loads(proc.stdout)


# --- 5. Scanner flags a known-bad draft -------------------------------------
section("Scanner flags a bad draft")

bad = (
    "Based on our discussion, in this guide we will explore the framework "
    "we landed on. Here is the rewritten copy you asked for. Experts say it "
    "is a world-class, seamless, robust solution that will leverage synergy. "
    "It's not just fast, it's transformative — truly best-in-class."
)
result = run_scanner(bad)
summary = result["summary"]
warnings = " ".join(result["warnings"]).lower()

check("flags process bleed", summary.get("process_bleed", 0) > 0)
check("flags assistant wrapper", summary.get("assistant_wrapper", 0) > 0)
check("flags em dash", summary.get("dash_usage", 0) > 0)
check("flags vague authority", summary.get("vague_authority", 0) > 0)
check("flags hype cluster", summary.get("generic_hype", 0) >= 3)
check("flags formulaic structure", summary.get("formulaic_structure", 0) > 0)
check("emits human-readable warnings", len(result["warnings"]) >= 4)
check("warning text mentions process", "process" in warnings)


# --- 5b. Scanner flags empty claims -----------------------------------------
section("Scanner flags empty claims")

empty = (
    "We are committed to excellence and passionate about quality. Our tailored "
    "solutions help you succeed and consistently exceed your expectations."
)
empty_result = run_scanner(empty)
empty_warnings = " ".join(empty_result["warnings"]).lower()
check("flags empty claims", empty_result["summary"].get("empty_claim", 0) >= 2)
check("empty-claim warning mentions negation", "negation" in empty_warnings)


# --- 5c. Scanner flags high-liability claims and manufactured pressure -------
section("Scanner flags risky claims and manufactured pressure")

risky = (
    "Our supplement is clinically proven and FDA-approved. Results are "
    "guaranteed and 100% risk-free, with a money-back guarantee. We are the #1 "
    "choice. Only 3 left, offer ends tonight. Trusted by 40,000 happy customers."
)
risky_result = run_scanner(risky)
risky_summary = risky_result["summary"]
risky_warnings = " ".join(risky_result["warnings"]).lower()
check("flags risky claims", risky_summary.get("risky_claim", 0) >= 2)
check("flags manufactured pressure", risky_summary.get("manufactured_pressure", 0) >= 2)
check(
    "harm warnings name the remedy",
    ("verify" in risky_warnings or "liability" in risky_warnings) and "scarcity" in risky_warnings,
)


# --- 5d. Scanner flags session narration (transcript transplant) -------------
section("Scanner flags session narration")

transplant = (
    "Then we added Slack alerts so the team gets notified. In this session we "
    "built the retry timeline view and polished the dashboard."
)
transplant_result = run_scanner(transplant)
check(
    "flags session narration as process bleed",
    transplant_result["summary"].get("process_bleed", 0) >= 2,
    f"hits={transplant_result['summary'].get('process_bleed', 0)}",
)


# --- 5e. Eval harness self-test ----------------------------------------------
section("Eval harness (offline self-test)")

eval_proc = subprocess.run(
    [sys.executable, str(ROOT / "tests" / "eval" / "score.py"), "--self-test"],
    capture_output=True, text=True,
)
check("eval scorer self-test passes", eval_proc.returncode == 0,
      (eval_proc.stdout + eval_proc.stderr).strip()[-200:])


# --- 5f. Portable build --------------------------------------------------------
section("Portable single-file build")

portable_proc = subprocess.run(
    ["bash", str(ROOT / "scripts" / "build_portable.sh")],
    capture_output=True, text=True, cwd=ROOT,
)
check("portable build succeeds", portable_proc.returncode == 0,
      (portable_proc.stdout + portable_proc.stderr).strip()[-200:])
portable_path = ROOT / "dist" / "human-copywrite-portable.md"
if portable_path.is_file():
    portable_text = portable_path.read_text(encoding="utf-8")
    check("portable build has no frontmatter", "name: human-copywrite" not in portable_text[:300])
    check("portable build carries the edit bar", "## The edit bar" in portable_text)
    check("portable build carries the tell catalog", "Diagnostic Catalog" in portable_text)
    check("portable build carries the voice setup", "MY_OWN_VOICE" in portable_text)
else:
    check("portable build output exists", False, str(portable_path))


# --- 6. Scanner stays quiet on clean copy -----------------------------------
section("Scanner stays quiet on clean copy")

clean = (
    "The app saves your work every minute. You can export any project to CSV "
    "in one click. Setup takes about five minutes on a fresh machine."
)
clean_result = run_scanner(clean)
problem_groups = {"process_bleed", "assistant_wrapper", "dash_usage",
                  "vague_authority", "formulaic_structure",
                  "risky_claim", "manufactured_pressure"}
clean_hits = {g: clean_result["summary"].get(g, 0) for g in problem_groups}
check(
    "no problem warnings on clean copy",
    all(v == 0 for v in clean_hits.values()),
    f"unexpected hits: { {k: v for k, v in clean_hits.items() if v} }",
)


# --- Summary ----------------------------------------------------------------
print(f"\n{'=' * 48}")
if failures:
    print(f"FAILED: {len(failures)} check(s), {passes} passed")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print(f"OK: all {passes} checks passed")
