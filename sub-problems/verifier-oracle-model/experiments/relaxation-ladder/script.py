#!/usr/bin/env python3
"""
Map relaxation IDs to barriers (journal entries) and main-problem compliance.
"""

from __future__ import annotations

RELAXATIONS = [
    {
        "id": "R1",
        "name": "Linear or n log n proof size",
        "barriers": "003 (VC budget), 004 (witness-heavy F_Link)",
        "main_compliant": False,
        "reason": "Violates compact |pi| = o(n)",
    },
    {
        "id": "R2",
        "name": "Reveal S or n-bit mask in pi",
        "barriers": "002, 004 (avoid hidden-subset Link)",
        "main_compliant": False,
        "reason": "Breaks desired signer anonymity / sublinear if bitmask Theta(n)",
    },
    {
        "id": "R3",
        "name": "Verifier sees all pk_i or precomputed aggregates",
        "barriers": "002,004,008 (direct check / registration)",
        "main_compliant": False,
        "reason": "Violates verifier model in main problem-statement",
    },
    {
        "id": "R4",
        "name": "SNARK/STARK or grey circuit verifier",
        "barriers": "005, 003 (sublinear proof of Link predicate)",
        "main_compliant": False,
        "reason": "Excluded by main problem",
    },
    {
        "id": "R5",
        "name": "Trusted-setup polynomial commitment",
        "barriers": "003 (batch openings)",
        "main_compliant": False,
        "reason": "Excluded by main problem",
    },
    {
        "id": "R6",
        "name": "TEE or trusted third party",
        "barriers": "generic soundness offload",
        "main_compliant": False,
        "reason": "Excluded by main problem",
    },
    {
        "id": "R7",
        "name": "Novel efficient Link + threshold attestation",
        "barriers": "all; not constructed",
        "main_compliant": True,
        "reason": "Target if it exists under stated assumptions",
    },
]


def main() -> None:
    print("=== relaxation-ladder ===\n")
    for r in RELAXATIONS:
        ok = "COMPLIANT" if r["main_compliant"] else "violates main"
        print(f"{r['id']}: {r['name']}")
        print(f"    Barriers (journal): {r['barriers']}")
        print(f"    vs main problem: {ok}")
        print(f"    Note: {r['reason']}\n")

    compliant = [r["id"] for r in RELAXATIONS if r["main_compliant"]]
    assert compliant == ["R7"]
    print("VERDICT: PASS (documentation) -- only R7 listed as fully main-compliant slot;")
    print("         INCONCLUSIVE whether R7 is achievable (no construction in repo).")

if __name__ == "__main__":
    main()
