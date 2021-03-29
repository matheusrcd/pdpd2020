import pylhe
import matplotlib.pyplot as plt
import numpy as np


lhe_file = pylhe.readLHE('Events/run_pphaa/unweighted_events.lhe')

def a_momenta(photons):
    total_momentum = 0
    p = [0, 0, 0]
    for a in photons:
        p[0] += a.px
        p[1] += a.py
        p[2] += a.pz
    total_momentum = np.sqrt(p[0]**2 + p[1]**2 + p[2]**2)
    return total_momentum


invariant_mass = []
for event in lhe_file:
    photons = []
    e_photons = []
    for ptc in event.particles:
        if ptc.id == 22:
            photons.append(ptc)
            e_photons.append(ptc.e)
    invariant_mass.append(np.sqrt(sum(e_photons)**2 - a_momenta(photons)**2))


# histogram for "p  p > H > a a"
plt.hist(invariant_mass, bins = 100)
plt.xlabel('Mass (GeV)')
plt.ylabel('N Events')
plt.title('Invariant Mass (p p > h, h > a a)', fontweight="bold")
plt.savefig('photons_invariant_mass.png')

plt.show()