#!/usr/bin/env python3
"""Fail closed if Pythology Mnemosyne security invariants drift."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(path, needle, reason):
    p = ROOT / path
    if not p.exists():
        errors.append(f"{path}: missing ({reason})")
        return
    text = p.read_text(encoding="utf-8")
    if needle not in text:
        errors.append(f"{path}: invariant missing: {reason}")

require(
    "deploy/docker/openviking-entrypoint.sh",
    'WITH_BOT="${OPENVIKING_WITH_BOT:-0}"',
    "VikingBot must remain opt-in by default",
)
require(
    "openviking/server/config.py",
    "enabled: bool = False",
    "observability/tracing configuration must retain a disabled default",
)
require(
    ".github/CODEOWNERS",
    "/openviking/server/ @PythologyIntelligence",
    "high-risk server code must be Pythology-owned",
)
require(
    ".github/UPSTREAM_SYNC_POLICY.md",
    "never flow directly into main",
    "upstream changes must be staged for review",
)
require(
    ".github/workflows/upstream-sync.yml",
    "automation/upstream-sync",
    "upstream sync must use the review branch",
)
require(
    "PYTHOLOGY_SECURITY.md",
    "Memory cannot grant authority.",
    "memory cannot grant runtime authority",
)

workflow = ROOT / ".github/workflows/upstream-sync.yml"
if workflow.exists():
    text = workflow.read_text(encoding="utf-8")
    for token in ("gh pr merge", "--auto-merge", "merge --auto"):
        if token in text:
            errors.append(f"upstream-sync workflow contains forbidden auto-merge token: {token}")

if errors:
    print("Mnemosyne security invariants FAILED:", file=sys.stderr)
    for error in errors:
        print(f" - {error}", file=sys.stderr)
    raise SystemExit(1)

print("Mnemosyne security invariants OK")
