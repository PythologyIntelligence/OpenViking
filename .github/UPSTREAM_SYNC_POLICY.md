# Pythology Upstream Sync Policy — Mnemosyne / OpenViking

This repository is a Pythology-maintained fork of volcengine/OpenViking.

## Rule

Upstream changes never flow directly into main.

volcengine/OpenViking:main -> automation/upstream-sync -> Pull Request + security review -> main

The scheduled workflow may stage upstream changes and create/update a pull request.
It must never merge that pull request automatically.

## Fail closed

If an upstream merge conflicts, the workflow fails for manual review.
Explicit review is required for changes touching authentication, tenancy, API keys,
server exposure/CORS, storage, memory mutation, model/VLM/embedding providers,
outbound HTTP, telemetry, VikingBot, shell/sandbox/tools/skills/plugins/MCP,
deployment defaults, GitHub Actions, release automation, or licence terms.

Pythology hardening takes precedence over upstream defaults. Mnemosyne is initially
a memory/context service, not a general agent runtime, so VikingBot remains opt-in.

Repository admins should separately protect main with PR review, conversation
resolution, status checks, and blocks on force-push and deletion.
