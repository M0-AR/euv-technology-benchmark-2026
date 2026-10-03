"""EXP-03: Multilayer + system transmission — verifies Mo/Si ~68-70% and T~2-4%.
Pass: R(50 bilayers) in [0.6,0.75]; T(10 mirrors) in [0.015,0.05].
Hidden-pattern probe: optimal bilayers knee at N~40-50 (diminishing returns).
"""
import csv, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from euvlab import multilayer_reflectivity, system_transmission

curve = [(n, round(multilayer_reflectivity(n), 4)) for n in [10, 20, 30, 40, 50, 60, 80]]
systems = [(n, round(system_transmission(n), 4)) for n in [6, 8, 10, 12]]

os.makedirs("data/processed", exist_ok=True)
with open("data/processed/exp03_optics.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["N_bilayers", "R"])
    w.writerows(curve)

r50 = multilayer_reflectivity(50)
t10 = system_transmission(10)
assert 0.60 <= r50 <= 0.75, f"R50={r50} outside Mo/Si literature"
assert 0.015 <= t10 <= 0.05, f"T10={t10} outside 10-mirror chain expectation"
gain_40_50 = multilayer_reflectivity(50) - multilayer_reflectivity(40)
gain_50_60 = multilayer_reflectivity(60) - multilayer_reflectivity(50)
assert gain_50_60 < gain_40_50, "expected saturation knee not found"
print("EXP-03 PASS: R50=", r50, "T10=", t10, "knee gains:", round(gain_40_50, 4), round(gain_50_60, 4))
