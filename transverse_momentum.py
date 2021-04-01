import pylhe
import matplotlib.pyplot as plt
import numpy as np

# LHE File for "p p > H  j, H > S S"
lhe_hjss = pylhe.readLHE("Events/run_pphjSS/unweighted_events.lhe")

transverse_momentum = []
for event in lhe_hjss:
    j = event.particles[-1]
    pt = np.sqrt(j.px**2 + j.py**2)
    transverse_momentum.append(pt)

# histogram for "p p > H  j, H > S S"
plt.hist(transverse_momentum, bins = 100)
plt.xlabel('Transverse Momentum (GeV)')
plt.ylabel('N Events')
plt.title('Invariant Mass (p p > H  j, H > S S)', fontweight="bold")
plt.savefig('pphjSS_transverse_momentum.png')
plt.show()