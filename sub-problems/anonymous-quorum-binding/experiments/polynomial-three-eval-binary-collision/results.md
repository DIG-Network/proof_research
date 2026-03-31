# Results — polynomial-three-eval-binary-collision

## Outcome: **PASS**

## Parameters

- Field: **𝔽_97**
- **n = 20** nodes `0..19` for Lagrange interpolation
- Query points **r₁ = 90**, **r₂ = 91**, **r₃ = 92** (none equal to a node mod 97)
- Pigeonhole check: **2²⁰ = 1 048 576 > 97³ = 912 673**

## Observation

Brute-force enumeration over all **2²⁰** binary leaf vectors, bucketing by **(P(r₁), P(r₂), P(r₃))**, finds the **first** collision at shared triple **(47, 73, 95)** with **Hamming distance 8** between the two patterns.

## Conclusion

**Three** independent Lagrange evaluations still do **not** injectively label arbitrary **{0,1}²⁰** participation vectors under this linear encoding. Extends **022** (one point) and **024** (two points, **2ⁿ > p²**).

## Repro

```bash
python script.py
```

Runtime ~6–7 s on a typical laptop (full mask sweep).
