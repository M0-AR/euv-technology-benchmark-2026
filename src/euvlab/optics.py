"""EUV optics: Mo/Si multilayer Bragg reflector + system transmission.
Anchors:
- Mo/Si period ~6.9nm (lambda/2=6.75nm + capping correction), 40-50 bilayers,
  peak R ~70% at 13.5nm near-normal (Kuang et al. 2018 robust design).
- System: 10 mirrors (illuminator 4 + projector 6-8) => T ~ 0.7^10 ~ 2.8%.
- Grazing-incidence (collector): total external reflection, R proxy declines with angle.
Model is analytic (kinematic Bragg stack), not full Fresnel solver — documented limit.
"""
import math


def multilayer_reflectivity(n_bilayers: int = 50, r_interface: float = 0.999,
                            r_ideal: float = 0.75) -> float:
    """Saturating stack reflectivity: R = R_ideal*(1-exp(-N/N0)), N0~20.
    r_interface penalises per-bilayer roughness cumulatively.
    Calibrated: r_interface=0.999 -> R50~0.65, matching Mo/Si 68-70% class
    (Kuang et al. 2018; interface roughness ~0.3nm rms per bilayer).
    """
    n0 = 20.0
    base = r_ideal * (1.0 - math.exp(-n_bilayers / n0))
    return base * (r_interface ** n_bilayers)


def grazing_reflectivity_proxy(angle_deg: float, cutoff_deg: float = 20.0) -> float:
    """Proxy R~1 for theta<<cutoff, falls as (cutoff/theta)^4 beyond."""
    if angle_deg <= 0:
        return 1.0
    if angle_deg <= cutoff_deg:
        return 0.95
    return 0.95 * (cutoff_deg / angle_deg) ** 4


def system_transmission(n_mirrors: int = 10, r_per_mirror: float = 0.68,
                        gas_transmission: float = 0.95) -> float:
    return (r_per_mirror ** n_mirrors) * gas_transmission
