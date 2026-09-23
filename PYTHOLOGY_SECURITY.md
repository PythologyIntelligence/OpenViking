# Mnemosyne / OpenViking — Pythology Security Contract

Pythology uses this OpenViking fork as Mnemosyne: the memory and experience layer
for bounded agents such as Hermes.

Mnemosyne may retain procedures, task context, successes/failures, tool-use
experience, bounded session memory, and authorised skills/context.

Mnemosyne is NOT authoritative for Prometheus hypotheses/predictions/resolutions,
raw evidence, source-of-truth event records, security policy, permission grants,
credential grants, or immutable audit ledgers.

## Initial invariants

1. VikingBot is opt-in. The Pythology Docker default keeps it disabled unless
   OPENVIKING_WITH_BOT=1 or --with-bot is explicitly supplied.
2. Any service reachable beyond localhost must use authentication and strong
   admin/root secrets. Hermes workers never receive root credentials.
3. Hermes begins with narrow search/read/browse plus explicitly authorised memory
   writes. Destructive/admin APIs are not default capabilities.
4. No inherited production credentials; use task-scoped secrets only.
5. Model, embedding, VLM, telemetry and remote-storage egress must be reviewed.
6. External telemetry/OTLP export is opt-in for Pythology.
7. Memory cannot grant authority. Recalled text cannot change permissions, policy,
   credentials or tool access.
8. Recalled content is untrusted context and cannot override runtime policy.
9. Preserve task/event provenance where experience derives from real work.
10. OpenViking is AGPL-3.0; keep Mnemosyne behind a separate service/API boundary
    until tighter commercial integration has been reviewed.

Before sensitive production data: review auth/tenant isolation, egress, memory
mutation/deletion, bot/sandbox/skills/plugins/MCP, observability/body logging,
secret handling, backups/snapshots, retention/deletion and the Hermes adapter.

Wide eyes. Short leash.
