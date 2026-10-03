# BENCHMARK — EUV Technology 6-week curriculum, reproduced from zero

Date: 2026-10-03 | Repro: `docker compose up euvlab` or `python experiments/run_all.py`
Live snapshot: `data/raw/live_snapshot.json` (3/3 HTTP 200 on 2026-10-03)

## B1. Resolution (EXP-01, k1=0.4, λ=13.5 nm)
| System | NA | R (nm HP) | DoF (nm) | Claim | Verdict |
|---|---|---|---|---|---|
| DUV 193nm | 1.35 | 57.19 | 105.9 | — | reference |
| NXE | 0.33 | 16.36 | 124.0 | ASML 13 nm lines | PASS (RET pushes below Abbe) |
| EXE | 0.55 | 9.82 | 44.6 | ASML 8 nm | PASS |
| Hyper-NA | 0.75 | 7.20 | 24.0 | roadmap | computed |

Photon: 91.84 eV. Bragg period d=6.75 nm (≈6.9 nm with capping — PASS).

## B2. Source (EXP-02)
CE saturates 4.84% (literature 4-6% — PASS). P_IF: 10 kW→242 W, 25 kW→606 W
(derated ≈ ASML 250 W NXE / 500 W+ EXE class — PASS, upper-bound model documented).

## B3. Optics (EXP-03)
R50 = 0.655 (Mo/Si 0.60-0.75 — PASS). T10 = 0.020 (2%, 1.5-5% — PASS).
**Hidden pattern 1 — saturation knee:** gain 40→50 = 0.0318, 50→60 = 0.0163.
>50 bilayers buys <2% absolute. Industrial 40-50 choice is optimal, not arbitrary.

## B4. Lithography RLS + Mask3D (EXP-04)
| Dose | fail proxy | WPH@250W |
|---|---|---|
| 15 | 0.352 | — | 
| 30 | 0.124 | 233 (upper bound; ASML ~170 with full overhead) |
| 60 | 0.015 | — |
NILS 18 nm pitch: 2.723 (0.33) → 3.431 (0.55) = +26.0% — exactly Maguire & Smith.
Mask3D bias: 1.0 → 0.55 — matches He & Zeng direction.
**Hidden pattern 2 — RLS asymmetry:** 2× dose (30→60) cuts failures 8× for
~2× time; 0.5× dose (30→15) triples failures. High-NA NILS gain is cheapest
stochastic mitigator (no throughput cost).
**Hidden pattern 3 — DoF collapse:** 124 nm → 44.6 nm (0.33→0.55). Focus budget,
not photon budget, binds Hyper-NA. Predicts focus-metrology premium.

## B5. Metrology + live (EXP-05)
Sensitivity EUV/DUV = 14.3× (PASS). Inversion err 0.50→0.25 nm (20→80 angles).
Live: asml_euv 200, rwth_tos 200, openalex 200 — PASS.
**Hidden pattern 4 — metrology dividend:** same wavelength that forces vacuum
and mirrors pays back 14× scatterometry leverage; EUV metrology is not
auxiliary but the control loop that makes HVM yield possible.

## Limits (honest)
- Kinematic Bragg proxy, not full Fresnel/RCWA.
- WPH is upper bound (12 s overhead, 3% wafer transmission, 100 fields).
- Stochastic proxy uses incident photons; absorbed fraction and resist blur omitted.
- Network checks are existence proofs, not data pulls.
