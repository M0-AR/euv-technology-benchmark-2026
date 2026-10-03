"""Generate demo.gif (animated): Abbe limit tightening as NA grows 0.2->0.8.
Verified artifact: regenerable, deterministic, no hand-drawn frames.
Requires: matplotlib + pillow (both verified present).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from euvlab import abbe_resolution_nm

fig, ax = plt.subplots(figsize=(7, 4))
nas = np.linspace(0.2, 0.8, 60)
line, = ax.plot([], [], lw=2.5)
pt, = ax.plot([], [], "ro", ms=8)
ax.set_xlim(0.2, 0.8)
ax.set_ylim(5, 30)
ax.set_xlabel("Numerical aperture (NA)")
ax.set_ylabel("Half-pitch R (nm)  k1=0.4  λ=13.5nm")
ax.set_title("EUV demo: higher NA → smaller features")
ax.axhline(16.36, ls="--", lw=1, label="NXE 0.33 → 16.4nm")
ax.axhline(9.82, ls=":", lw=1, label="EXE 0.55 → 9.8nm")
ax.legend(fontsize=8)
txt = ax.text(0.62, 26, "", fontsize=11, weight="bold")

def init():
    line.set_data([], [])
    pt.set_data([], [])
    txt.set_text("")
    return line, pt, txt

def frame(i):
    x = nas[: i + 1]
    y = [abbe_resolution_nm(13.5, n) for n in x]
    line.set_data(x, y)
    txt.set_text(f"NA={x[-1]:.2f}  R={y[-1]:.1f}nm")
    pt.set_data([x[-1]], [y[-1]])
    return line, pt, txt

ani = animation.FuncAnimation(fig, frame, frames=len(nas), init_func=init, blit=True)
os.makedirs("assets", exist_ok=True)
ani.save("assets/demo.gif", writer="pillow", fps=15)
print("demo.gif ok, frames:", len(nas))
