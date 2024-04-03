import freud
import gsd.hoomd
import matplotlib.pyplot as plt
import numpy as np
import time

bins = 100
k_max = 40
k_min = 3
name = 'Sf_n=5'

sfDirect = freud.diffraction.StaticStructureFactorDirect(
    bins=bins, k_max=k_max, k_min=k_min
)

with gsd.hoomd.open(f"/home/pavel/Mol_mod/Hoomd_cycles/Hmd/hmd/output_n=5.gsd", "r") as traj:
    frame = traj[-1] 
    box = frame.configuration.box
    typeid = frame.particles.typeid
    coord = frame.particles.position[typeid==0]
t1 = time.time()
sfDirect.compute((box, coord), reset=True)
t2 = time.time()
print('lead time: ', t2-t1)
k = sfDirect.bin_centers/box[0]
sf_k = sfDirect.S_k
np.savetxt(name+'.txt', np.vstack([k, sf_k]))
plt.plot(k, sf_k, label="Direct")
plt.show()
