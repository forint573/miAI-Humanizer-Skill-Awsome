#!/usr/bin/env python3
"""
score.py — model-agnostic scorer for the human-copywrite eval.

Scores a piece of copy on "always-bar violations": the objective failures the
skill fixes on sight (process bleed and session narration, assistant wrapper,
em/en dashes, vague authority, unbacked high-liability claims, manufactured
pressure, formulaic structure), plus clustered hype and empty claims. Task
files add require/forbid regexes for behavior the scanner cannot see (caveat
survival, placeholders instead of invented facts).

Dependency-free; reuses the skill's own heuristic scanner so the eval and the
skill judge by one standard. Lower is better; 0 always-bar violations and a
task pass is the target.

Usage:
  python tests/eval/score.py <output.md> [--task <task-id>] [--json]
  python tests/eval/score.py --self-test
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
ROOT = EVAL_DIR.parent.parent
SCANNER_PATH = ROOT / "human-copywrite" / "scripts" / "copy_scan.py"

# Groups where a single hit is an always-bar violation.
ALWAYS_GROUPS = [
    "process_bleed",
    "assistant_wrapper",
    "dash_usage",
    "vague_authority",
    "risky_claim",
    "manufactured_pressure",
    "formulaic_structure",
]
# Groups that violate only as a cluster, with their thresholds.
CLUSTER_GROUPS = {"generic_hype": 3, "empty_claim": 2}


def load_scanner():
    spec = importlib.util.spec_from_file_location("copy_scan", SCANNER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_tasks() -> dict:
    data = json.loads((EVAL_DIR / "tasks.json").read_text(encoding="utf-8"))
    return {t["id"]: t for t in data["tasks"]}


def score_text(text: str, task: dict | None = None) -> dict:
    scanner = load_scanner()
    summary = scanner.scan(text)["summary"]

    always = sum(summary.get(g, 0) for g in ALWAYS_GROUPS)
    clustered = {
        g: summary.get(g, 0)
        for g, threshold in CLUSTER_GROUPS.items()
        if summary.get(g, 0) >= threshold
    }
    always += sum(clustered.values())

    require_failed: list[str] = []
    forbid_hits: list[str] = []
    if task:
        for pattern in task.get("require", []):
            if not re.search(pattern, text):
                require_failed.append(pattern)
        for pattern in task.get("forbid", []):
            if re.search(pattern, text):
                forbid_hits.append(pattern)

    return {
        "always_bar_violations": always,
        "groups": {g: summary.get(g, 0) for g in ALWAYS_GROUPS if summary.get(g)},
        "clustered": clustered,
        "require_failed": require_failed,
        "forbid_hits": forbid_hits,
        "task_pass": always == 0 and not require_failed and not forbid_hits,
    }


def self_test() -> int:
    """Validate the harness on bundled fixtures: the raw-slop fixture must
    score high, and the skill-written target rewrite must score clean."""
    failures = []

    bad = (EVAL_DIR / "fixtures" / "raw-slop.md").read_text(encoding="utf-8")
    bad_score = score_text(bad)
    print(f"raw-slop fixture: {bad_score['always_bar_violations']} always-bar violations (expected >= 8)")
    if bad_score["always_bar_violations"] < 8:
        failures.append("raw-slop fixture scored suspiciously clean; scorer may be broken")

    tasks = load_tasks()
    good = (EVAL_DIR / "fixtures" / "target-rewrite.md").read_text(encoding="utf-8")
    good_score = score_text(good, tasks["clean-nothing"])
    print(f"target-rewrite fixture: {good_score['always_bar_violations']} always-bar violations (expected 0), task_pass={good_score['task_pass']}")
    if good_score["always_bar_violations"] != 0 or not good_score["task_pass"]:
        failures.append(f"target rewrite should score clean, got {good_score}")

    transcript_output = "We built Relay in this session. Then we added retry timelines and finally wired up Slack alerts."
    transplant_score = score_text(transcript_output, tasks["homepage-from-session"])
    print(f"transplant sample: forbid_hits={len(transplant_score['forbid_hits'])} (expected >= 1)")
    if not transplant_score["forbid_hits"]:
        failures.append("transcript-transplant output was not caught by the homepage task's forbid list")

    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print("self-test OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", help="copy output to score")
    parser.add_argument("--task", help="task id from tasks.json for require/forbid checks")
    parser.add_argument("--json", action="store_true", help="print the full JSON result")
    parser.add_argument("--self-test", action="store_true", help="validate the harness on bundled fixtures")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.file:
        parser.error("provide a file to score, or --self-test")

    task = load_tasks().get(args.task) if args.task else None
    if args.task and task is None:
        parser.error(f"unknown task id: {args.task}")

    result = score_text(Path(args.file).read_text(encoding="utf-8"), task)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"always-bar violations: {result['always_bar_violations']}")
        if result["groups"]:
            print(f"  by group: {result['groups']}")
        if result["clustered"]:
            print(f"  clustered: {result['clustered']}")
        if result["require_failed"]:
            print(f"  missing required: {result['require_failed']}")
        if result["forbid_hits"]:
            print(f"  forbidden matches: {result['forbid_hits']}")
        print(f"task pass: {result['task_pass']}" if task else "task pass: (no --task given)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
