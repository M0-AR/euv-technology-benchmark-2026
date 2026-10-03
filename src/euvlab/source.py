"""EUV source models anchored to published LPP data.
Anchors:
- Versolato 2019 (IOP, 285 cites): LPP Sn plasma, CO2 drive, in-band 13.5nm 2% BW.
- ASML 2024-2026: NXE source ~250W IF; EXE roadmap >500W; drive ~20-30kW CO2.
- He et al. arXiv:2501.14541: FEL alternative ~2kW proposal (not LPP).
Model: P_IF = P_drive * CE * eta_collector; CE fitted ~4-6% laser->inband 2pi.
We expose CE as function of intensity with saturation (empirical logistic),
calibrated so CE(peak)=5.5% consistent with literature 4-6%.
"""
import math


def lpp_conversion_efficiency(intensity_gw_per_cm2: float, ce_max: float = 0.055) -> float:
    """Logistic saturation of conversion efficiency vs drive intensity.
    Calibrated: CE->ce_max at high intensity, ~half at 0.5 GW/cm2 scale.
    """
    x = intensity_gw_per_cm2
    return ce_max / (1.0 + math.exp(-4.0 * (x - 0.5)))


def if_power_model(drive_kw: float, ce: float, collector_sr_efficiency: float = 0.5) -> float:
    """Intermediate-focus power in watts. drive_kw in kW."""
    return drive_kw * 1000.0 * ce * collector_sr_efficiency


def dose_to_throughput_wph(if_power_w: float, dose_mj_per_cm2: float = 30.0,
                            field_cm2: float = 3.3 * 2.6, overhead_s: float = 12.0) -> float:
    """Wafers/hour proxy: exposure time = dose*area/power_at_wafer.
    power_at_wafer = P_IF * system_transmission(~2-4% for 10-mirror chain).
    Uses fixed 3% wafer transmission; overhead per wafer (swap+align).
    """
    p_wafer = if_power_w * 0.03
    dose_j = dose_mj_per_cm2 * 1e-3 * field_cm2  # J per field
    # ~100 fields per 300mm wafer
    t_exp = dose_j * 100.0 / p_wafer if p_wafer > 0 else float("inf")
    t_total_h = (t_exp + overhead_s) / 3600.0
    return 1.0 / t_total_h if t_total_h > 0 else 0.0
