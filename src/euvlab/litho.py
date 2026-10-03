"""Lithography proxies: NILS, stochastic failure, mask-3D bias.
Anchors:
- Rayleigh NILS for dense L/S ~ pi at best focus; High-NA gains +26% NILS
  for 18nm pitch (Maguire & Smith SPIE 2025, aperiodic multilayer).
- Stochastic: photon shot noise ~1/sqrt(N); N = dose*area/E_photon.
  At 30mJ/cm2, 16nm box N~5200 incident photons (91.8eV); only a fraction
  absorbed => effective N smaller. Proxy: fail_rate = exp(-N/Nc), Nc=2500
  calibrated so 15mJ->~0.35, 30mJ->~0.12, 60mJ->~0.016 (visible RLS knee).
- Mask3D: He & Zeng 2025 (Micromachines): higher NA 0.55 raises contrast,
  suppresses absorber shadow vs 0.33. Proxy bias_0.33=1.0, bias_0.55=0.55.
"""
import math
from .physics import HC_EV_NM


def nisl_proxy(pitch_nm: float, na: float, wavelength_nm: float = 13.5) -> float:
    base = math.pi * (1.0 - 0.15 * (16.0 / pitch_nm))
    na_gain = 1.0 + 0.26 * max(0.0, (na - 0.33) / 0.22)
    return round(base * na_gain, 3)


def stochastic_fail_proxy(dose_mj_cm2: float, cd_nm: float = 16.0,
                           wavelength_nm: float = 13.5) -> float:
    e_j = (HC_EV_NM / wavelength_nm) * 1.602176634e-19
    area_cm2 = (cd_nm * 1e-7) ** 2
    dose_j_cm2 = dose_mj_cm2 * 1e-3
    n_photons = dose_j_cm2 * area_cm2 / e_j
    nc = 2500.0
    return round(math.exp(-n_photons / nc), 5)


def mask3d_bias_proxy(na: float) -> float:
    if na <= 0.33:
        return 1.0
    # linear interpolation 0.33->1.0, 0.55->0.55 (He & Zeng trend)
    t = min(1.0, (na - 0.33) / 0.22)
    return round(1.0 - 0.45 * t, 3)
