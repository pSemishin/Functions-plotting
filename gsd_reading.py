import gsd.hoomd
import numpy as np
import freud
import matplotlib.pyplot as plt
traj = gsd.hoomd.open('/home/pavel/Mol_mod/Hoomd_cycles/Hmd/hmd/output_n=5.gsd')
# print(len(traj))

# frame = traj[0]
# print(frame.configuration.step)
# print(frame.particles.N)
# print(frame.particles.position)
# print(frame.particles.types)
# print(f'связи - {frame.bonds.group}')
id = traj[0].particles.typeid
box = traj[0].configuration.box
moment = traj[0].particles.moment_inertia 
R_g = []
#print(moment)

L_box = 100.0
bins = 100
k_min = 0.004
k_max = 1.0
big_box = freud.box.Box(Lx=L_box,Ly=L_box,Lz=L_box, xy=0.0, xz=0.0, yz=0.0, is2D=False)
sfDebye = freud.diffraction.StaticStructureFactorDebye(
    num_k_values=bins, k_max=k_max, k_min=k_min
    )
for frame in traj:
    ring_coord = []
    coords = frame.particles.position[id==0]

    for i in range(len(coords)):
        
        if len(ring_coord) < 1:
            ring_coord.append(list(coords[i]))
        else:
            dx = coords[i,0] - ring_coord[-1][0]
            dy = coords[i,1] - ring_coord[-1][1]
            dz = coords[i,2] - ring_coord[-1][2]
            if dx > box[0]/2:
                coords[i,0] -= box[0]
            if dx < -box[0]/2:
                coords[i,0] += box[0]
            if dy > box[1]/2:
                coords[i,1] -= box[1]
            if dy < -box[1]/2:
                coords[i,1] += box[1]
            if dz > box[2]/2:
                coords[i,2] -= box[2]
            if dz < -box[2]/2:
                coords[i,2] += box[2]
            ring_coord.append(list(coords[i]))
    ring_coord = np.array(ring_coord)
    # c_x = np.sum(ring_coord[:,0]) / len(ring_coord)
    # c_y = np.sum(ring_coord[:,1]) / len(ring_coord)
    # c_z = np.sum(ring_coord[:,2]) / len(ring_coord)
  
    # ring_coord[:,0] = (ring_coord[:,0]-c_x)**2
    # ring_coord[:,1] = (ring_coord[:,1]-c_y)**2
    # ring_coord[:,2] = (ring_coord[:,2]-c_z)**2
    ring_coord[:,0] = ring_coord[:,0]-ring_coord[0,0]
    ring_coord[:,1] = ring_coord[:,1]-ring_coord[0,1]
    ring_coord[:,2] = ring_coord[:,2]-ring_coord[0,2]

    sfDebye.compute((big_box, ring_coord[:len(ring_coord)//2]),reset=False)
    print(len(ring_coord))
    break
q = sfDebye.k_values
Sf = sfDebye.S_k

plt.plot(q, Sf)
plt.show()
plt.close()

np.savetxt("sf_half_n=5.txt", np.vstack([q, Sf]))

for n in [5, 10, 20, 50]:
    X = np.loadtxt(f"sf_half_n={n}.txt")
    # plt.plot(X[0,1:], np.diff(X[1])/np.diff(X[0])/50, label=f"n={n}")
    # plt.plot(X[0], X[1]*X[0], label=f"n={n}")
    plt.plot(X[0], X[1]/100, label=f"n={n}")
# for n in [5, 10, 20, 50]:
#     X = np.loadtxt(f"sf_full_n={n}.txt")
# #     plt.plot(X[0,1:], np.diff(X[1])/np.diff(X[0])/50, label=f"n={n}")
#     # plt.plot(X[0], X[1]*X[0], label=f"n={n}")
#     plt.plot(X[0], X[1]/200, label=f"n={n}")
# # plt.loglog()
plt.legend()
plt.show()
plt.close()


# for atom in ring_coord:
#     R_g.append((np.sum(ring_coord[:,:])) / len(ring_coord))
# R_g = np.array(R_g)
# np.savetxt('R_g_N=200_m=1_n=50.txt', R_g)
    
 