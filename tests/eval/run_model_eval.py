#!/usr/bin/env python3
"""
run_model_eval.py — measure what the skill does for a model, on your own keys.

Runs the task set in tasks.json twice against an OpenAI-compatible chat API:
once bare (no system prompt) and once with the portable skill build as the
system prompt. Scores both runs with score.py and prints the per-task and
total deltas. This is the test behind the README's claim about budget models:
run it and read the numbers instead of believing the pitch.

Setup:
  bash scripts/build_portable.sh              # builds dist/human-copywrite-portable.md
  export EVAL_API_KEY=...                     # your key
  export EVAL_MODEL=glm-5.2                   # the model id your provider uses
  export EVAL_BASE_URL=...                    # OpenAI-compatible base URL

Known OpenAI-compatible bases (verify against your provider's current docs):
  GLM (Zhipu):    https://open.bigmodel.cn/api/paas/v4
  DeepSeek:       https://api.deepseek.com
  Kimi (Moonshot): https://api.moonshot.ai/v1

Usage:
  python tests/eval/run_model_eval.py            # both runs + delta table
  python tests/eval/run_model_eval.py --bare-only | --skill-only

Outputs land in tests/eval/out/<model>/<bare|skill>/<task>.md so you can read
the copy, not just the numbers. Dependency-free (urllib).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
ROOT = EVAL_DIR.parent.parent
PORTABLE = ROOT / "dist" / "human-copywrite-portable.md"

sys.path.insert(0, str(EVAL_DIR))
from score import load_tasks, score_text  # noqa: E402


def chat(base_url: str, api_key: str, model: str, messages: list, retries: int = 2) -> str:
    payload = json.dumps({"model": model, "messages": messages, "stream": False}).encode("utf-8")
    request = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                body = json.loads(response.read().decode("utf-8"))
            return body["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as err:
            if err.code in (429, 500, 502, 503) and attempt < retries:
                time.sleep(5 * (attempt + 1))
                continue
            raise
    raise RuntimeError("unreachable")


def build_user_message(task: dict) -> str:
    prompt = task["prompt"]
    if task.get("fixture"):
        fixture_text = (EVAL_DIR / task["fixture"]).read_text(encoding="utf-8")
        prompt = f"{prompt}\n\n{fixture_text}"
    return prompt


def strip_reasoning(text: str) -> str:
    """Drop <think>...</think> blocks some reasoning models emit inline."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()


def run_variant(variant: str, system_prompt: str | None, tasks: dict, cfg: dict) -> dict:
    out_dir = EVAL_DIR / "out" / cfg["model"].replace("/", "_") / variant
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for task_id, task in tasks.items():
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": build_user_message(task)})
        print(f"  {variant}/{task_id} ...", flush=True)
        output = strip_reasoning(chat(cfg["base_url"], cfg["api_key"], cfg["model"], messages))
        (out_dir / f"{task_id}.md").write_text(output, encoding="utf-8")
        results[task_id] = score_text(output, task)
    return results


def print_table(tasks: dict, bare: dict | None, skill: dict | None) -> None:
    def cell(results, task_id):
        if not results or task_id not in results:
            return "-"
        r = results[task_id]
        flags = len(r["require_failed"]) + len(r["forbid_hits"])
        return f"{r['always_bar_violations']}v/{flags}f {'PASS' if r['task_pass'] else 'fail'}"

    width = max(len(t) for t in tasks) + 2
    print(f"\n{'task'.ljust(width)}{'bare'.ljust(18)}with skill")
    for task_id in tasks:
        print(f"{task_id.ljust(width)}{cell(bare, task_id).ljust(18)}{cell(skill, task_id)}")

    def totals(results):
        if not results:
            return None
        return (
            sum(r["always_bar_violations"] for r in results.values()),
            sum(1 for r in results.values() if r["task_pass"]),
        )

    for label, results in (("bare", bare), ("with skill", skill)):
        t = totals(results)
        if t:
            print(f"{label}: {t[0]} always-bar violations total, {t[1]}/{len(tasks)} tasks passed")
    print("(v = always-bar violations, f = failed require/forbid checks; 0v + PASS everywhere is the bar)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--bare-only", action="store_true")
    parser.add_argument("--skill-only", action="store_true")
    args = parser.parse_args()

    cfg = {
        "base_url": os.environ.get("EVAL_BASE_URL", ""),
        "api_key": os.environ.get("EVAL_API_KEY", ""),
        "model": os.environ.get("EVAL_MODEL", ""),
    }
    missing = [k for k, v in cfg.items() if not v]
    if missing:
        print(f"error: set EVAL_BASE_URL, EVAL_API_KEY, EVAL_MODEL (missing: {', '.join(missing)})")
        return 2

    system_prompt = None
    if not args.bare_only:
        if not PORTABLE.is_file():
            print("error: dist/human-copywrite-portable.md not found; run: bash scripts/build_portable.sh")
            return 2
        system_prompt = PORTABLE.read_text(encoding="utf-8")

    tasks = load_tasks()
    print(f"model: {cfg['model']} @ {cfg['base_url']}  ({len(tasks)} tasks)")
    bare = run_variant("bare", None, tasks, cfg) if not args.skill_only else None
    skill = run_variant("skill", system_prompt, tasks, cfg) if not args.bare_only else None
    print_table(tasks, bare, skill)
    return 0


if __name__ == "__main__":
    sys.exit(main())
