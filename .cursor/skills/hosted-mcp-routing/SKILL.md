---
name: hosted-mcp-routing
description: >-
  Use when calling hosted Streamable HTTP MCP tools (Chia graph RAG, Coinset, prompt queue, planner,
  ledger, scratch, spec, verify, deploy, cron, session, handoff). Walks orchestration: pick mount,
  pass project, order multi-step flows, avoid Chia-vs-Coinset mistakes.
---

# Hosted MCP routing and orchestration

## Mandatory first reads (project rules)

1. **`hosted-mcp-orchestration.mdc`** — mount matrix, `project` vs no-`project`, session-per-path, **workflows** (cron, queue, handoff, spec→planner→verify), **anti-patterns**.
2. **`mcp-tools-when-to-use-always.mdc`** — confirm exact **tool name** and server for the step you are on.
3. **`hosted-mcp-overview.mdc`** — secrets and production limits.

For one tool’s triggers and argument hints: **`.cursor/rules/mcp-tools/<tool-with-hyphens>.mdc`**.

## Decision shortcuts

| Situation | Action |
|-----------|--------|
| Protocol / docs / “how does X work on Chia?” | `chia_knowledge_*` on **`chia-knowledge`** |
| Live height, coin, mempool, push tx | `coinset_*` on **`coinset`** — **not** Chia RAG |
| Same stable id on planner, ledger, queue, scratch, … | Set **`project`** once; reuse everywhere it is required |
| More than one MCP call in a row | Follow the matching **recipe** in **`hosted-mcp-orchestration.mdc`** |
| Unsure of Coinset operation names | `coinset_operations` then `coinset_post` |
| Quick HTTP sanity check, no audit row | **`probe_*`** |
| Recorded check / regression / spec link | **`verify_*`** |
| Scheduled tick | `cron_tick_snapshot` → domain tools → `cron_iteration_checkpoint` (mind loop vs ledger note in playbook) |
| New session after long context | `session_restore` → `session_sanity_check` |

## Execution habits

- Open the correct **Cursor MCP server** for the tool prefix (one HTTP path = one server).
- Never reuse **`Mcp-Session-Id`** across different `/mcp/...` paths.
- If a tool errors as **disabled** (e.g. release webhook, shell verify), **stop and explain** — do not retry blindly.
- Use **`tools/list`** + **`inputSchema`** on that server when arguments are ambiguous.

## When this skill applies

Attach or follow when the user or task involves **any** hosted MCP tool, multi-step agent ops, cron ticks, queue workers, deployment records, or Chia questions that might need **both** docs and chain.
