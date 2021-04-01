import pylhe
import matplotlib.pyplot as plt
import numpy as np

# LHE File for "p p > Z  j, Z > vm vm~"
lhe_zjvv = pylhe.readLHE("Events/run_ppZjvmvm~/unweighted_events.lhe")

transverse_momentum = []
for event in lhe_zjvv:
    j = event.particles[-1]
    pt = np.sqrt(j.px**2 + j.py**2)
    transverse_momentum.append(pt)

# histogram for "p p > Z  j, Z > vm vm~"
plt.hist(transverse_momentum, bins = 100)
plt.xlabel('Transverse Momentum (GeV)')
plt.ylabel('N Events')
plt.title('Invariant Mass (p p > Z  j, Z > vm vm~)', fontweight="bold")
plt.savefig('ppzjvm_transverse_momentum.png')
plt.show()