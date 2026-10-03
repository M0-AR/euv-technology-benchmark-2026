"""Core EUV physics: Abbe, DoF, photon energy, Bragg, Fresnel zone.
Sources:
- Abbe R = k1*lambda/NA (RWTH Week1/Week3; Sattler 2010 EUVL review).
- DoF = k2*lambda/NA^2 (standard lithography).
- E = hc/lambda; h=4.135667696e-15 eV*s, c=299792458 m/s.
- Bragg 2*d*sin(theta)=m*lambda; at near-normal theta~90deg -> d=lambda/2.
- Fresnel zone plate r_n = sqrt(n*lambda*f).
"""
import math

H_EV_S = 4.135667696e-15
C_M_S = 299792458.0
HC_EV_NM = 1239.841984  # h*c in eV*nm


def photon_energy_ev(wavelength_nm: float) -> float:
    return HC_EV_NM / wavelength_nm


def abbe_resolution_nm(wavelength_nm: float, na: float, k1: float = 0.4) -> float:
    """Half-pitch resolution. k1=0.4 typical single-exposure EUV."""
    return k1 * wavelength_nm / na


def depth_of_focus_nm(wavelength_nm: float, na: float, k2: float = 1.0) -> float:
    return k2 * wavelength_nm / (na ** 2)


def bragg_period_nm(wavelength_nm: float = 13.5, order: int = 1, theta_deg: float = 90.0) -> float:
    theta = math.radians(theta_deg)
    return order * wavelength_nm / (2.0 * math.sin(theta))


def fresnel_zone_outer_nm(wavelength_nm: float, focal_mm: float, zones: int) -> float:
    """Outermost zone radius r_N = sqrt(N*lambda*f). Returns nm."""
    f_nm = focal_mm * 1e6
    return math.sqrt(zones * wavelength_nm * f_nm)


def rayleigh_range_check() -> dict:
    """Benchmark table: NXE 0.33 NA vs EXE 0.55 NA at 13.5 nm, k1=0.4."""
    lam = 13.5
    out = {}
    for name, na in [("NXE_0p33", 0.33), ("EXE_0p55", 0.55)]:
        out[name] = {
            "R_nm": round(abbe_resolution_nm(lam, na), 2),
            "DoF_nm": round(depth_of_focus_nm(lam, na), 1),
            "photon_eV": round(photon_energy_ev(lam), 2),
            "bragg_d_nm": round(bragg_period_nm(lam), 3),
        }
    return out
