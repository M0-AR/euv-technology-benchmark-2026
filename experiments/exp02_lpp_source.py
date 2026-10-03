"""EXP-02: LPP source IF power vs drive — anchored to ASML 250W NXE / 500W+ EXE.
Verifies: 25kW CO2 * 5% CE * 0.5 collector ~ 625W theoretical; derated -> 250W class.
Pass: CE saturates 4-6%; IF(25kW) in [200,700]W.
"""
import csv, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from euvlab import lpp_conversion_efficiency, if_power_model

ces = [(i, round(lpp_conversion_efficiency(i), 4)) for i in [0.2, 0.5, 1.0, 2.0]]
powers = []
for drive in [10, 20, 25, 30, 40]:
    ce = lpp_conversion_efficiency(1.0)
    p = if_power_model(drive, ce)
    powers.append((drive, round(ce * 100, 2), round(p, 1)))

os.makedirs("data/processed", exist_ok=True)
with open("data/processed/exp02_source.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["drive_kW", "CE_pct", "P_IF_W"])
    w.writerows(powers)

ce_peak = lpp_conversion_efficiency(2.0)
assert 0.04 <= ce_peak <= 0.065, f"CE {ce_peak} outside literature 4-6.5%"
p25 = if_power_model(25, lpp_conversion_efficiency(1.0))
assert 200 <= p25 <= 700, f"P_IF {p25}W unrealistic vs ASML 250-500W class"
print("EXP-02 PASS:", powers)
