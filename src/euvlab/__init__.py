"""EUVLab: first-principles + empirically-anchored EUV models.
All constants and anchor points cite public sources (see SOURCES.md).
No value is hand-tuned: every number is either a physical constant,
a textbook formula, or a 2024-2026 published anchor verified by experiment.
"""
from .physics import (
    abbe_resolution_nm, depth_of_focus_nm, photon_energy_ev,
    bragg_period_nm, fresnel_zone_outer_nm, rayleigh_range_check,
)
from .source import lpp_conversion_efficiency, if_power_model, dose_to_throughput_wph
from .optics import multilayer_reflectivity, grazing_reflectivity_proxy, system_transmission
from .litho import nisl_proxy, stochastic_fail_proxy, mask3d_bias_proxy
from .metrology import scatterometry_sensitivity, reflectometry_inversion_error

__all__ = [
    "abbe_resolution_nm", "depth_of_focus_nm", "photon_energy_ev",
    "bragg_period_nm", "fresnel_zone_outer_nm", "rayleigh_range_check",
    "lpp_conversion_efficiency", "if_power_model", "dose_to_throughput_wph",
    "multilayer_reflectivity", "grazing_reflectivity_proxy", "system_transmission",
    "nisl_proxy", "stochastic_fail_proxy", "mask3d_bias_proxy",
    "scatterometry_sensitivity", "reflectometry_inversion_error",
]
