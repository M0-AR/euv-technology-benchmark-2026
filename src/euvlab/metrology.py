"""EUV metrology proxies: scatterometry sensitivity + reflectometry inversion.
Anchors:
- NIST EUV scatterometry; KMLabs HHG coherent scatterometry note;
  arXiv:2504.12133 (coherent EUV scatterometry sensitivity to nm-scale).
- Tabletop EUV reflectometer (multimodal: intensity/scatterometry/CDI).
Proxy: sensitivity dR/dCD scales as 1/lambda; inversion error falls as
sqrt(N_angles) and rises with noise.
"""
import math


def scatterometry_sensitivity(wavelength_nm: float = 13.5, pitch_nm: float = 32.0) -> float:
    """Sensitivity ~ pitch/lambda normalised so DUV(193nm,32nm pitch)=1.
    EUV then scores ~14.3x, capturing the 1/lambda advantage documented by
    EUV then scores ~14.3x, capturing the 1/lambda advantage documented by
    NIST EUV scatterometry and arXiv:2504.12133 coherent EUV scatterometry.
    """
    return round((pitch_nm / wavelength_nm) / (32.0 / 193.0), 4)


def reflectometry_inversion_error(n_angles: int = 20, noise_pct: float = 1.0) -> float:
    """RMS CD error (nm) proxy: err = 0.5*sqrt(20/N)*noise."""
    return round(0.5 * math.sqrt(20.0 / max(1, n_angles)) * noise_pct, 4)
