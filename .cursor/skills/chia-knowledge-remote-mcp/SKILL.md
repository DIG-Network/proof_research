---
name: chia-knowledge-remote-mcp
description: Use the hosted Chia Knowledge Graph RAG MCP over Streamable HTTP (Elastic Beanstalk / Docker) when the local stdio MCP is not available.
---

# Chia Knowledge — remote MCP

When the **chia-knowledge** MCP is deployed with `MCP_TRANSPORT=http`, clients that support **MCP Streamable HTTP** can connect to:

- **MCP (Chia graph RAG):** `https://<your-host>/mcp/chia`
- **MCP (Coinset live chain API):** `https://<your-host>/mcp/coinset` — `coinset_post`, `coinset_operations` ([Coinset docs](https://www.coinset.org/docs))
- **MCP (prompt queue):** `https://<your-host>/mcp/queue`
- **Health:** `GET https://<your-host>/health`

Production (CloudFront): `https://d3ob29frtjgqt9.cloudfront.net` — see `deploy/README-CLOUDFRONT.md` and `deploy/README-EB.md` if the URL changes. Sessions are **per path**; do not mix `Mcp-Session-Id` across mounts (e.g. `/mcp/chia` vs `/mcp/coinset`).

Configure the remote connector in your MCP client per that product’s “remote MCP” or “HTTP transport” docs. Local development still uses repo `.mcp.json` (stdio + `CHIA_KNOWLEDGE_DB`).

**Tools:** same as local — `graph_rag_retrieve`, `blended_knowledge_lookup`, `get_rag_subgraph`, `get_rag_learning_context`, etc.

**Deploy / Docker:** root `Dockerfile`, `RAG/nuggets-graph-rag-mcp/DEPLOY_ELASTIC_BEANSTALK.md`, `docs/claude-remote-mcp-chia-knowledge.md`.
