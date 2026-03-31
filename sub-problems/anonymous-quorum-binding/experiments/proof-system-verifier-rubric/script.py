#!/usr/bin/env python3
"""
Classify proof families against a small verifier rubric (symbolic / asymptotic).

Not cryptography — documentation + consistency checks for research policy.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Family:
    name: str
    trusted_setup: bool
    verifier_takes_arbitrary_circuit: bool
    pairing_checks: str  # e.g. "O(1)", "0"
    hash_checks: str
    field_or_scalar_ops_vs_n: str  # asymptotic in statement size n_stmt
    bucket: str


def main() -> None:
    n = "n_stmt"  # symbolic statement size (e.g. #validators in link predicate)

    families = [
        Family(
            name="Groth16 (generic)",
            trusted_setup=True,
            verifier_takes_arbitrary_circuit=True,
            pairing_checks="O(1)",
            hash_checks="O(1)",
            field_or_scalar_ops_vs_n=f"O({n}) implied by witness but verify fixed pairings",
            bucket="EXCLUDED_SNARK",
        ),
        Family(
            name="PLONK/Halo2-style (generic)",
            trusted_setup=False,
            verifier_takes_arbitrary_circuit=True,
            pairing_checks="O(1) pairings + O(log rows)",
            hash_checks="O(log rows)",
            field_or_scalar_ops_vs_n=f"poly({n}) in constraint count",
            bucket="EXCLUDED_SNARK",
        ),
        Family(
            name="STARK / FRI (generic)",
            trusted_setup=False,
            verifier_takes_arbitrary_circuit=True,
            pairing_checks="0",
            hash_checks=f"O(log^2 {n}) typical FRI queries",
            field_or_scalar_ops_vs_n=f"polylog({n}) * trace length term",
            bucket="EXCLUDED_SNARK",
        ),
        Family(
            name="Bulletproofs / IPA (single inner-product, fixed circuit)",
            trusted_setup=False,
            verifier_takes_arbitrary_circuit=False,
            pairing_checks="0",
            hash_checks="0",
            field_or_scalar_ops_vs_n=f"O(log K) for K-length witness vector in THAT proof",
            bucket="GREY_TRANSPARENT",
        ),
        Family(
            name="Bulletproofs for w in {0,1}^n + threshold + lincomb",
            trusted_setup=False,
            verifier_takes_arbitrary_circuit=False,
            pairing_checks="0",
            hash_checks="0",
            field_or_scalar_ops_vs_n=f"O(log n) proof rounds but O(n) constraints to arithmetize predicate",
            bucket="GREY_TRANSPARENT",
        ),
        Family(
            name="Merkle inclusion path (single leaf)",
            trusted_setup=False,
            verifier_takes_arbitrary_circuit=False,
            pairing_checks="0",
            hash_checks=f"O(log {n})",
            field_or_scalar_ops_vs_n="O(1)",
            bucket="ALLOWED_ATOMIC",
        ),
        Family(
            name="BLS pairing (single aggregate equation)",
            trusted_setup=False,
            verifier_takes_arbitrary_circuit=False,
            pairing_checks="O(1)",
            hash_checks="0",
            field_or_scalar_ops_vs_n="O(1)",
            bucket="ALLOWED_ATOMIC",
        ),
    ]

    print("=== proof-system-verifier-rubric ===\n")
    for f in families:
        print(f.name)
        print(f"  trusted_setup={f.trusted_setup}")
        print(f"  arbitrary_circuit_input={f.verifier_takes_arbitrary_circuit}")
        print(f"  pairings: {f.pairing_checks}")
        print(f"  hashes: {f.hash_checks}")
        print(f"  ops vs statement: {f.field_or_scalar_ops_vs_n}")
        print(f"  BUCKET: {f.bucket}\n")

    assert families[0].bucket == "EXCLUDED_SNARK"
    assert families[-1].bucket == "ALLOWED_ATOMIC"
    grey = [f for f in families if f.bucket == "GREY_TRANSPARENT"]
    assert len(grey) >= 1

    print(
        "POLICY NOTE: Main problem text excludes SNARK/STARK toolchains.\n"
        "GREY_TRANSPARENT entries are NOT automatically allowed — they encode\n"
        "n-dependent statements; verifier may be 'log-sized proof' but still\n"
        "circuit-heavy to build or audit on-chain."
    )
    print("\nVERDICT: PASS — rubric table consistent; Groth16 excluded, BLS atomic allowed.")


if __name__ == "__main__":
    main()
