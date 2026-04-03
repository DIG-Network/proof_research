# Notes

- **observation:** Total split count for the union is **4082** (= sum_{r=2}^{11} C(12,r)), versus **8177** at n=13 and **16368** at n=14 — scaling is dominated by middle binomial terms as expected.
- **insight:** **`min_d=2`** for the full XOR menu appears stable across **`n∈{12,13,14}`** for the corresponding majority shells; oracle text can treat this as a small-`n` ladder fact, not an n=14 artifact.
- **question:** At **`n=11`** `{5,6}`, does the full `r=2..10` union still give **`min_d=2`**? (Optional continuation down the ladder.)
