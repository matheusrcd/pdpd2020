import pylhe
import matplotlib.pyplot as plt
import numpy as np


lhe_file = pylhe.readLHE('Events/run_pphSS/unweighted_events.lhe')

def S_momenta(dmatter):
    total_momentum = 0
    p = [0, 0, 0]
    for S in dmatter:
        p[0] += S.px
        p[1] += S.py
        p[2] += S.pz
    total_momentum = np.sqrt(p[0]**2 + p[1]**2 + p[2]**2)
    return total_momentum

invariant_mass = []
for event in lhe_file:
    dmatter = []
    e_dmatter = []
    for ptc in event.particles:
        if ptc.id == 9000005:
            dmatter.append(ptc)
            e_dmatter.append(ptc.e)
    invariant_mass.append(np.sqrt(sum(e_dmatter)**2 - S_momenta(dmatter)**2))


# histogram for "p  p > H > S S"
plt.hist(invariant_mass, bins = 100)
plt.xlabel('Mass (GeV)')
plt.ylabel('N Events')
plt.title('Invariant Mass (p p > h, h > S S)', fontweight="bold")
plt.savefig('dm_invariant_mass.png')

plt.show()