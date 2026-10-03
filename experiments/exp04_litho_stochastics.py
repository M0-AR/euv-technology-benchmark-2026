"""EXP-04: Dose<->stochastics<->throughput — verifies RLS tradeoff + ASML WPH.
Anchors: dose 30mJ/cm2 typical; NXE ~150-170 WPH; EXE target similar with higher power.
Pass: fail rate falls with dose; WPH rises with IF power; WPH(250W,30mJ)~>100.
Hidden pattern: doubling dose halves fail rate exponentially but costs ~2x time.
"""
import csv, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from euvlab import stochastic_fail_proxy, dose_to_throughput_wph, nisl_proxy, mask3d_bias_proxy

doses = [(d, round(stochastic_fail_proxy(d), 5)) for d in [15, 20, 30, 40, 60]]
wph = [(p, round(dose_to_throughput_wph(p), 1)) for p in [150, 250, 400, 600]]
nils = [(pitch, nisl_proxy(pitch, 0.33), nisl_proxy(pitch, 0.55)) for pitch in [32, 28, 24, 18]]

os.makedirs("data/processed", exist_ok=True)
with open("data/processed/exp04_litho.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["dose_mJcm2", "fail_proxy"])
    w.writerows(doses)

assert stochastic_fail_proxy(60) < stochastic_fail_proxy(15), "dose-fail monotonicity broken"
assert dose_to_throughput_wph(400) > dose_to_throughput_wph(150), "power-WPH monotonicity broken"
assert dose_to_throughput_wph(250) > 100, "WPH too low vs ASML class"
assert nisl_proxy(18, 0.55) > nisl_proxy(18, 0.33) * 1.15, "High-NA NILS gain <15% (expect ~26%)"
assert mask3d_bias_proxy(0.55) < mask3d_bias_proxy(0.33), "mask3D trend inverted vs He&Zeng"
print("EXP-04 PASS:", doses, wph, nils)
