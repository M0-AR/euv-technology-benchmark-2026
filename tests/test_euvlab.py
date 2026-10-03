import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from euvlab import abbe_resolution_nm, photon_energy_ev, multilayer_reflectivity, system_transmission

def test_abbe_nxe():
    assert abs(abbe_resolution_nm(13.5, 0.33) - 16.36) < 0.05

def test_photon():
    assert 91.0 < photon_energy_ev(13.5) < 92.5

def test_optics_band():
    assert 0.60 <= multilayer_reflectivity(50) <= 0.75
    assert 0.015 <= system_transmission(10) <= 0.05
