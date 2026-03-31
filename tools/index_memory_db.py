#!/usr/bin/env python3
"""
Initialize ./memory.db using the schema and indexing flow described in persona.md
(Vector Memory + Historical Indexing H1, H3–H7, H10).

Skips H8 (constraint derivation — requires judgment) and H9 (lineage inference).

Embedding model: OpenAI `text-embedding-3-small` (1536 dims) when `OPENAI_KEY` or
`OPENAI_API_KEY` is set; otherwise deterministic hash embeddings (not semantically meaningful).
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = REPO_ROOT / "memory.db"
JOURNAL = REPO_ROOT / "research-journal"
INDEX_MD = JOURNAL / "index.md"
BREAKTHROUGHS = JOURNAL / "BREAKTHROUGHS.md"
SUB_PROBLEMS = REPO_ROOT / "sub-problems"

EMBED_DIM = 1536

SCHEMA_SQL = """
CREATE VIRTUAL TABLE IF NOT EXISTS mem USING vec0(
    id          TEXT PRIMARY KEY,
    embedding   FLOAT[1536],
    record_type TEXT,
    slug        TEXT,
    outcome     TEXT,
    summary     TEXT,
    path        TEXT,
    created_at  TEXT
);

CREATE TABLE IF NOT EXISTS notes (
    id          TEXT PRIMARY KEY,
    slug        TEXT NOT NULL,
    record_type TEXT NOT NULL,
    note_type   TEXT NOT NULL,
    body        TEXT NOT NULL,
    path        TEXT,
    created_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS raw_data (
    id          TEXT PRIMARY KEY,
    slug        TEXT NOT NULL,
    data_type   TEXT NOT NULL,
    label       TEXT NOT NULL,
    value       TEXT NOT NULL,
    unit        TEXT,
    notes       TEXT,
    created_at  TEXT NOT NULL
);

CREATE VIRTUAL TABLE IF NOT EXISTS mem_fts USING fts5(
    id,
    slug,
    record_type,
    note_type,
    body,
    content='notes',
    content_rowid='rowid'
);

CREATE TRIGGER IF NOT EXISTS notes_ai AFTER INSERT ON notes BEGIN
    INSERT INTO mem_fts(rowid, id, slug, record_type, note_type, body)
    VALUES (new.rowid, new.id, new.slug, new.record_type, new.note_type, new.body);
END;

CREATE TRIGGER IF NOT EXISTS notes_au AFTER UPDATE ON notes BEGIN
    INSERT INTO mem_fts(mem_fts, rowid, id, slug, record_type, note_type, body)
    VALUES ('delete', old.rowid, old.id, old.slug, old.record_type, old.note_type, old.body);
    INSERT INTO mem_fts(rowid, id, slug, record_type, note_type, body)
    VALUES (new.rowid, new.id, new.slug, new.record_type, new.note_type, new.body);
END;

CREATE TABLE IF NOT EXISTS constraints (
    id              TEXT PRIMARY KEY,
    constraint_type TEXT NOT NULL,
    area            TEXT NOT NULL,
    statement       TEXT NOT NULL,
    confidence      TEXT NOT NULL,
    established_by  TEXT NOT NULL,
    refuted_by      TEXT,
    status          TEXT NOT NULL,
    created_at      TEXT NOT NULL,
    updated_at      TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lineage (
    child_slug      TEXT NOT NULL,
    parent_slug     TEXT NOT NULL,
    relationship    TEXT NOT NULL,
    rationale       TEXT NOT NULL,
    PRIMARY KEY (child_slug, parent_slug)
);

CREATE TABLE IF NOT EXISTS constraint_links (
    experiment_slug TEXT NOT NULL,
    constraint_id   TEXT NOT NULL,
    role            TEXT NOT NULL,
    note            TEXT,
    PRIMARY KEY (experiment_slug, constraint_id, role)
);

CREATE VIRTUAL TABLE IF NOT EXISTS constraint_fts USING fts5(
    id,
    area,
    statement,
    content='constraints',
    content_rowid='rowid'
);

CREATE TRIGGER IF NOT EXISTS constraints_ai AFTER INSERT ON constraints BEGIN
    INSERT INTO constraint_fts(rowid, id, area, statement)
    VALUES (new.rowid, new.id, new.area, new.statement);
END;

CREATE TRIGGER IF NOT EXISTS constraints_au AFTER UPDATE ON constraints BEGIN
    INSERT INTO constraint_fts(constraint_fts, rowid, id, area, statement)
    VALUES ('delete', old.rowid, old.id, old.area, old.statement);
    INSERT INTO constraint_fts(rowid, id, area, statement)
    VALUES (new.rowid, new.id, new.area, new.statement);
END;
"""


def _pack_embedding(vec: list[float]) -> bytes:
    if len(vec) != EMBED_DIM:
        raise ValueError(f"expected {EMBED_DIM} dims, got {len(vec)}")
    return struct.pack("<" + "f" * EMBED_DIM, *vec)


def hash_embedding(text: str) -> bytes:
    """Deterministic unit vector — for schema tests only."""
    vals: list[float] = []
    seed = hashlib.sha256(text.encode("utf-8")).digest()
    while len(vals) < EMBED_DIM:
        seed = hashlib.sha256(seed).digest()
        for i in range(0, len(seed) - 3, 4):
            w = int.from_bytes(seed[i : i + 4], "little") / 2**32 * 2.0 - 1.0
            vals.append(w)
            if len(vals) >= EMBED_DIM:
                break
    a = np.array(vals[:EMBED_DIM], dtype=np.float32)
    n = float(np.linalg.norm(a)) + 1e-8
    a = a / n
    return struct.pack("<" + "f" * EMBED_DIM, *a.tolist())


def _openai_api_key() -> str | None:
    return os.environ.get("OPENAI_KEY") or os.environ.get("OPENAI_API_KEY")


class Embedder:
    def __init__(self) -> None:
        key = _openai_api_key()
        self._use_openai = bool(key)
        self._client = None
        if self._use_openai and key:
            from openai import OpenAI

            self._client = OpenAI(api_key=key)

    def embed_batch(self, texts: list[str]) -> list[bytes]:
        if not texts:
            return []
        if not self._use_openai:
            return [hash_embedding(t) for t in texts]
        assert self._client is not None
        out: list[bytes] = []
        batch_size = 64
        for i in range(0, len(texts), batch_size):
            chunk = texts[i : i + batch_size]
            resp = self._client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk,
                dimensions=EMBED_DIM,
            )
            by_idx = {item.index: item.embedding for item in resp.data}
            for j in range(len(chunk)):
                out.append(_pack_embedding(by_idx[j]))
        return out


def parse_journal_index() -> list[dict[str, str]]:
    raw = INDEX_MD.read_text(encoding="utf-8")
    rows: list[dict[str, str]] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|\s*-+", line):
            continue
        if "Date" in line and "Slug" in line:
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        parts = [p for p in parts if p]
        if len(parts) < 5:
            continue
        date_s, slug, context, outcome, entry_cell = parts[0], parts[1], parts[2], parts[3], parts[4]
        m = re.search(r"\(([^)]+\.md)\)", entry_cell)
        rel_entry = m.group(1) if m else entry_cell.strip()
        rows.append(
            {
                "date": date_s,
                "slug": slug,
                "context": context,
                "outcome": outcome,
                "entry_relpath": rel_entry,
            }
        )
    rows.sort(key=lambda r: r["date"])
    return rows


def _field(body: str, label: str) -> str | None:
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+?)(?=\n\*\*|\n##|\Z)", body, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else None


def build_experiment_summary(slug: str, outcome: str, entry_body: str) -> str:
    hyp = _field(entry_body, "Hypothesis tested") or _field(entry_body, "Hypothesis")
    finding = _field(entry_body, "Finding")
    impl = _field(entry_body, "Implications")
    bits = [
        f"Experiment {slug}. Outcome: {outcome}.",
        hyp and f"Hypothesis: {hyp[:1200]}",
        finding and f"Finding: {finding[:1200]}",
        impl and f"Implications: {impl[:600]}",
    ]
    return " ".join(b for b in bits if b)


def _slugify(s: str, max_len: int = 96) -> str:
    t = re.sub(r"[^a-zA-Z0-9._-]+", "-", s.lower()).strip("-")
    return (t[:max_len].rstrip("-") or hashlib.sha256(s.encode()).hexdigest()[:16])


def parse_breakthrough_sections() -> list[dict[str, str]]:
    if not BREAKTHROUGHS.exists():
        return []
    text = BREAKTHROUGHS.read_text(encoding="utf-8")
    out: list[dict[str, str]] = []
    for m in re.finditer(r"^##\s+\[([^\]]+)\]\s+(.+)$", text, re.MULTILINE):
        date_part, title_part = m.group(1).strip(), m.group(2).strip()
        title = f"[{date_part}] {title_part}"
        body = text[m.end() :]
        nxt = re.search(r"^##\s+\[", body, re.MULTILINE)
        body = body[: nxt.start()] if nxt else body
        desc = _field(body, "Description") or ""
        novel = _field(body, "Why this is novel") or ""
        disc = _field(body, "Discovered in") or ""
        slug = _slugify(f"{date_part}-{title_part}")
        out.append(
            {
                "title": title,
                "slug": slug,
                "summary": f"{desc}\n{novel}".strip()[:8000],
                "path": disc.strip("` ") or "",
            }
        )
    return out


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def insert_mem(
    cur: Any,
    eid: str,
    blob: bytes,
    record_type: str,
    slug: str,
    outcome: str | None,
    summary: str,
    path: str,
    created_at: str,
) -> None:
    # vec0 metadata columns reject SQL NULL; use empty string for unknown outcome.
    out = outcome if outcome is not None else ""
    cur.execute(
        """
        INSERT OR IGNORE INTO mem (id, embedding, record_type, slug, outcome, summary, path, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (eid, blob, record_type, slug, out, summary, path, created_at),
    )


def index_notes_for_slug(
    cur: Any,
    slug: str,
    record_type: str,
    exp_dir: Path,
    created_at: str,
    note_counter: dict[str, int],
) -> None:
    notes_path = exp_dir / "notes.md"
    if not notes_path.exists():
        return
    body = notes_path.read_text(encoding="utf-8").strip()
    if not body:
        return
    for para in re.split(r"\n\s*\n", body):
        line = para.strip()
        if not line:
            continue
        note_counter[slug] = note_counter.get(slug, 0) + 1
        nid = f"{slug}/note-{note_counter[slug]:03d}"
        ntype = "observation"
        low = line.lower()
        if "dead" in low and "end" in low:
            ntype = "dead_end"
        cur.execute(
            """
            INSERT OR IGNORE INTO notes (id, slug, record_type, note_type, body, path, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (nid, slug, record_type, ntype, line[:20000], str(notes_path.relative_to(REPO_ROOT)), created_at),
        )


def index_raw_data_for_slug(cur: Any, slug: str, exp_dir: Path, created_at: str, data_counter: dict[str, int]) -> None:
    results_path = exp_dir / "results.md"
    if not results_path.exists():
        return
    body = results_path.read_text(encoding="utf-8").strip()
    if not body:
        return
    for i, line in enumerate(body.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        data_counter[slug] = data_counter.get(slug, 0) + 1
        rid = f"{slug}/data-{data_counter[slug]:03d}"
        cur.execute(
            """
            INSERT OR IGNORE INTO raw_data (id, slug, data_type, label, value, unit, notes, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                rid,
                slug,
                "result" if i == 1 else "metric",
                f"line-{i}",
                line[:10000],
                None,
                None,
                created_at,
            ),
        )


def rebuild_fts_and_verify(conn: Any) -> None:
    conn.execute("INSERT INTO mem_fts(mem_fts) VALUES ('rebuild')")
    conn.execute("INSERT INTO mem_fts(mem_fts) VALUES ('optimize')")
    conn.execute("INSERT INTO constraint_fts(constraint_fts) VALUES ('rebuild')")
    conn.execute("INSERT INTO constraint_fts(constraint_fts) VALUES ('optimize')")
    row = conn.execute("PRAGMA integrity_check").fetchone()
    if row[0] != "ok":
        raise RuntimeError(f"integrity_check failed: {row}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Build memory.db from repo artifacts (persona.md schema).")
    ap.add_argument("--force", action="store_true", help="Remove existing memory.db first")
    args = ap.parse_args()

    import sqlite3
    import sqlite_vec

    if args.force and DB_PATH.exists():
        DB_PATH.unlink()

    embedder = Embedder()
    if not embedder._use_openai:
        print(
            "WARNING: OPENAI_KEY / OPENAI_API_KEY not set — using deterministic hash embeddings. "
            "Set OPENAI_KEY for semantic search.",
            file=sys.stderr,
        )

    conn = sqlite3.connect(str(DB_PATH))
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    cur = conn.cursor()
    cur.executescript(SCHEMA_SQL)
    conn.commit()

    note_counter: dict[str, int] = {}
    data_counter: dict[str, int] = {}

    # --- H3 experiments from journal index ---
    index_rows = parse_journal_index()
    summaries: list[str] = []
    meta: list[dict[str, Any]] = []
    for r in index_rows:
        entry_path = JOURNAL / r["entry_relpath"]
        if not entry_path.exists():
            entry_body = ""
        else:
            entry_body = entry_path.read_text(encoding="utf-8")
        summary = build_experiment_summary(r["slug"], r["outcome"], entry_body)
        summaries.append(summary)
        exp_dir = SUB_PROBLEMS / r["context"] / "experiments" / r["slug"]
        meta.append(
            {
                "slug": r["slug"],
                "outcome": r["outcome"],
                "summary": summary,
                "created_at": r["date"],
                "exp_dir": exp_dir,
                "results_path": str((exp_dir / "results.md").relative_to(REPO_ROOT))
                if (exp_dir / "results.md").exists()
                else str(exp_dir.relative_to(REPO_ROOT)),
            }
        )

    blobs = embedder.embed_batch(summaries)
    for m, b in zip(meta, blobs, strict=True):
        insert_mem(
            cur,
            f"experiment/{m['slug']}",
            b,
            "experiment",
            m["slug"],
            m["outcome"],
            m["summary"],
            m["results_path"],
            m["created_at"],
        )
        if m["exp_dir"].is_dir():
            index_notes_for_slug(cur, m["slug"], "experiment", m["exp_dir"], m["created_at"], note_counter)
            index_raw_data_for_slug(cur, m["slug"], m["exp_dir"], m["created_at"], data_counter)
    conn.commit()
    print(f"Indexed {len(meta)} experiments.")

    # --- H4 hypotheses ---
    hyp_jobs: list[tuple[Path, str, str | None]] = []
    for p in SUB_PROBLEMS.glob("*/experiments/*/hypothesis.md"):
        slug = p.parent.name
        outcome = None
        for r in index_rows:
            if r["slug"] == slug:
                outcome = r["outcome"]
                break
        hyp_jobs.append((p, slug, outcome))
    if hyp_jobs:
        h_summaries = [j[0].read_text(encoding="utf-8").strip()[:6000] for j in hyp_jobs]
        h_blobs = embedder.embed_batch(h_summaries)
        for (p, slug, outcome), blob, summ in zip(hyp_jobs, h_blobs, h_summaries, strict=True):
            created = next((r["date"] for r in index_rows if r["slug"] == slug), iso_now()[:10])
            insert_mem(
                cur,
                f"hypothesis/{slug}",
                blob,
                "hypothesis",
                slug,
                outcome,
                summ,
                str(p.relative_to(REPO_ROOT)),
                created,
            )
        conn.commit()
    print(f"Indexed {len(hyp_jobs)} hypotheses.")

    # --- H5 sub-problems ---
    sp_jobs: list[tuple[str, str, str, str | None, Path]] = []
    for status_md in SUB_PROBLEMS.glob("*/status.md"):
        slug = status_md.parent.name
        ps = status_md.parent / "problem-statement.md"
        if not ps.exists():
            continue
        st = status_md.read_text(encoding="utf-8")
        outcome = None
        if re.search(r"\bSOLVED\b", st, re.I):
            outcome = "SOLVED"
        elif re.search(r"\bABANDONED\b", st, re.I):
            outcome = "ABANDONED"
        summary = ps.read_text(encoding="utf-8").strip()[:8000]
        sp_jobs.append((slug, summary, str(ps.relative_to(REPO_ROOT)), outcome, status_md.parent))
    if sp_jobs:
        s_blobs = embedder.embed_batch([x[1] for x in sp_jobs])
        sol_batch: list[tuple[str, str, str, str]] = []
        for (slug, summary, relp, outcome, folder), blob in zip(sp_jobs, s_blobs, strict=True):
            created = iso_now()[:10]
            insert_mem(
                cur,
                f"sub-problem/{slug}",
                blob,
                "sub-problem",
                slug,
                outcome,
                summary,
                relp,
                created,
            )
            sol = folder / "solution.md"
            if sol.exists():
                sol_summary = sol.read_text(encoding="utf-8").strip()[:8000]
                sol_batch.append((slug, sol_summary, str(sol.relative_to(REPO_ROOT)), created))
        if sol_batch:
            sol_blobs = embedder.embed_batch([t[1] for t in sol_batch])
            for (slug, sol_summary, sol_relp, created), sb in zip(sol_batch, sol_blobs, strict=True):
                insert_mem(
                    cur,
                    f"solution/{slug}",
                    sb,
                    "solution",
                    slug,
                    "SOLVED",
                    sol_summary,
                    sol_relp,
                    created,
                )
        conn.commit()
    print(f"Indexed {len(sp_jobs)} sub-problems (+ solutions where present).")

    # --- H6 spaces ---
    space_paths = list(SUB_PROBLEMS.glob("*/experiments/*/space-definition.md"))
    if space_paths:
        s_summ = [p.read_text(encoding="utf-8").strip()[:8000] for p in space_paths]
        s_blobs = embedder.embed_batch(s_summ)
        for p, blob, summ in zip(space_paths, s_blobs, s_summ, strict=True):
            slug = p.parent.name
            created = next((r["date"] for r in index_rows if r["slug"] == slug), iso_now()[:10])
            insert_mem(
                cur,
                f"space/{slug}",
                blob,
                "space",
                slug,
                None,
                summ,
                str(p.relative_to(REPO_ROOT)),
                created,
            )
        conn.commit()
    print(f"Indexed {len(space_paths)} space definitions.")

    # --- H7 breakthroughs ---
    br = parse_breakthrough_sections()
    if br:
        b_blobs = embedder.embed_batch([x["summary"] for x in br])
        for b, blob in zip(br, b_blobs, strict=True):
            insert_mem(
                cur,
                f"breakthrough/{b['slug']}",
                blob,
                "breakthrough",
                b["slug"],
                None,
                b["summary"],
                b["path"] or "research-journal/BREAKTHROUGHS.md",
                iso_now()[:10],
            )
        conn.commit()
    print(f"Indexed {len(br)} breakthrough sections.")

    rebuild_fts_and_verify(conn)
    conn.commit()

    n_mem = cur.execute("SELECT COUNT(*) FROM mem").fetchone()[0]
    n_exp = cur.execute("SELECT COUNT(*) FROM mem WHERE record_type='experiment'").fetchone()[0]
    n_notes = cur.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    n_raw = cur.execute("SELECT COUNT(*) FROM raw_data").fetchone()[0]
    conn.close()

    print(f"Done. Database: {DB_PATH}")
    print(f"Stats: mem={n_mem} (experiments={n_exp}), notes={n_notes}, raw_data={n_raw}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
