# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

This is a pure mathematics/cryptography research workspace — not a traditional software product. It contains standalone Python experiment scripts and Markdown documentation for research on compact threshold signature verification.

### Structure

- `persona.md` — AI research agent persona and methodology
- `session-state.md` — current research session tracker
- `research-journal/` — immutable experiment entries and digests
- `main-problem/` — formal problem statement
- `sub-problems/` — two active research tracks:
  - `anonymous-quorum-binding/` — ~45 experiments
  - `verifier-oracle-model/` — ~58 experiments
- Each experiment lives in `sub-problems/<track>/experiments/<slug>/script.py`

### Running experiments

All experiment scripts are standalone Python files. Run with:

```bash
python3 sub-problems/<track>/experiments/<slug>/script.py
```

Exit code 0 = PASS (hypothesis confirmed), exit code 1 = FAIL (hypothesis falsified). Both are valid scientific outcomes — exit 1 does **not** indicate a broken script.

### Dependencies

- **Python 3.12+** (system)
- **numpy** — used by ~10 experiments for linear algebra / spectral computations
- **networkx** — used by a few experiments for graph generation

No `requirements.txt` exists; dependencies are installed via `pip install numpy networkx`.

### No services to run

There are no servers, databases, build steps, or background processes. The "application" is running individual experiment scripts.

### Git authentication

Always configure the git remote to use the `GH_PAT_TOKEN` secret for push/fetch operations:

```bash
git remote set-url origin "https://x-access-token:${GH_PAT_TOKEN}@github.com/DIG-Network/proof_research"
```

### Lint / test

There is no formal linter or test suite configured. Correctness is validated by running experiment scripts directly.
