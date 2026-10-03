import subprocess, sys, os
exps = ["exp01_abbe_resolution.py", "exp02_lpp_source.py", "exp03_multilayer.py",
        "exp04_litho_stochastics.py", "exp05_metrology_live.py"]
here = os.path.dirname(os.path.abspath(__file__))
ok = True
for e in exps:
    print("=" * 60 + "\nRUN", e)
    r = subprocess.run([sys.executable, os.path.join(here, e)], cwd=os.path.join(here, ".."))
    if r.returncode != 0:
        ok = False
        print("FAILED:", e)
print("ALL PASS" if ok else "SOME FAILED")
sys.exit(0 if ok else 1)
