"""EXP-01: Abbe resolution vs NA — verifies RWTH Week1/Week3 claim.
Pass criteria: NXE 0.33 -> 16.36nm HP; EXE 0.55 -> 9.82nm HP (k1=0.4, 13.5nm).
Matches ASML specs: NXE prints 13nm lines, EXE 8nm with aggressive k1/RET.
"""
import csv, os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from euvlab import abbe_resolution_nm, depth_of_focus_nm, photon_energy_ev

LAM = 13.5
rows = []
for name, na in [("DUV_193nm_1.35", 1.35), ("NXE_0.33", 0.33), ("EXE_0.55", 0.55), ("HyperNA_0.75", 0.75)]:
    lam = 193.0 if "DUV" in name else LAM
    r = abbe_resolution_nm(lam, na)
    dof = depth_of_focus_nm(lam, na)
    rows.append((name, na, round(r, 2), round(dof, 1), round(photon_energy_ev(lam), 2)))

os.makedirs("data/processed", exist_ok=True)
with open("data/processed/exp01_abbe.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["system", "NA", "R_hp_nm_k1_0.4", "DoF_nm", "photon_eV"])
    w.writerows(rows)

# Verification asserts (fail loudly if physics broken)
assert abs(abbe_resolution_nm(13.5, 0.33) - 16.36) < 0.05, "NXE Abbe mismatch"
assert abs(abbe_resolution_nm(13.5, 0.55) - 9.82) < 0.05, "EXE Abbe mismatch"
assert photon_energy_ev(13.5) > 90 and photon_energy_ev(13.5) < 93, "EUV photon ~91.8eV"
print("EXP-01 PASS:", rows)
