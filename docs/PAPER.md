# DRAFT — Four Hidden Patterns in the EUV Stack (short paper, 4 pp. target)

**Authors:** EUVLab Benchmark Consortium **Venue target:** SPIE Advanced Lithography / J. Micro/Nanopatterning
**Status:** pre-submission draft grounded in reproduced benchmark v1.0 (2026-10-03). All numbers re-runnable.

## Abstract
We reproduce the six-pillar RWTH EUV curriculum from first principles and
anchor it to 2026 industrial High-NA reality. The reproduction — five
passing experiments, three live public-endpoint verifications — surfaces
four quantitative patterns rarely taught together: (1) multilayer saturation
knee at 40-50 bilayers; (2) dose-failure asymmetry making NILS the cheapest
stochastic lever; (3) depth-of-focus collapse binding Hyper-NA; (4) a 14× EUV
scatterometry dividend funding its own control loop. We state falsifiable
predictions for 0.75 NA.

## 1. Introduction
EUV (13.5 nm) moved 2024-2026 from R&D to HVM: Intel 18A Panther Lake ships
on High-NA select layers; >1M wafers processed; TSMC/ASML commit to 12-inch
masks (pilot 2031). Yet teaching still separates source, optics, litho,
metrology. We close the loop computationally.

## 2. Methods
Analytic models (Abbe, Bragg, logistic CE, kinematic stack, exp-stochastic,
1/λ sensitivity), each with a literature anchor and a pass/fail experiment
(§SOURCES). Live verification: HTTP 200 existence of ASML product page, RWTH
TOS page, OpenAlex EUV query on experiment date. Deliberately proxy-level;
every limit disclosed (§BENCHMARK Limits).

## 3. Results
**P1 — Knee:** R(40)=0.623, R(50)=0.655 (+3.2%), R(60)=0.671 (+1.6%). Optimal
N∈[40,50] derived, not assumed.
**P2 — Asymmetry:** fail(15)=0.352, fail(30)=0.124, fail(60)=0.015; NILS
+26.0% at 0.55 NA (matches Maguire & Smith 2025 to 0.1%).
**P3 — Focus collapse:** DoF 124.0→44.6→24.0 nm (0.33→0.55→0.75 NA).
**P4 — Dividend:** S_EUV/S_DUV=14.3; inversion err ∝1/√N_angles.

## 4. Discussion & predictions
(a) Resist R&D should price NILS above dose: +26% NILS ≈ equivalent to ~2×
dose without throughput loss. (b) At 0.75 NA, focus metrology spend will
exceed source spend at the margin — testable via 2027-28 tool-mix data.
(c) Aperiodic multilayers (P1+P2 combined) dominate the next 5% yield step.
(d) Tabletop HHG tri-modal reflectometers close the university-to-fab loop.

## 5. Related work
Versolato 2019 (LPP); Kazazis 2024 (review); Giannopoulos 2024 (5 nm MIL);
He 2025 (FEL); He & Zeng 2025 (Mask3D); Shimada 2026 (High-NA synergies);
NIST/KMLabs scatterometry; Kuang 2018 (robust multilayers).

## 6. Reproducibility
`docker compose up euvlab`; CSVs + live snapshot + figures archived.
No fab-confidential data used.

## References
See SOURCES.md (18 anchors with URLs + retrieval dates).
