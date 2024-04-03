import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(1, 500, 500)
# Rg1 = np.loadtxt("R_g_N=100_m=1_n=5.txt", delimiter='\t')
# Rg2 = np.loadtxt("R_g_N=100_m=1_n=10.txt", delimiter='\t')
# Rg3 = np.loadtxt("R_g_N=100_m=1_n=20.txt", delimiter='\t')
# Rg4 = np.loadtxt("R_g_N=100_m=1_n=50.txt", delimiter='\t')

# Rg1_mean = [np.array(np.sqrt(np.mean(Rg1)))] * 500
# Rg2_mean = [np.array(np.sqrt(np.mean(Rg2)))] * 500
# Rg3_mean = [np.array(np.sqrt(np.mean(Rg3)))] * 500
# Rg4_mean = [np.array(np.sqrt(np.mean(Rg4)))] * 500

# plt.plot(x, np.sqrt(Rg1), label = 'n=5')
# plt.plot(x, np.sqrt(Rg2), label = "n=10")
# plt.plot(x, np.sqrt(Rg3), label = "n=20")
# plt.plot(x, np.sqrt(Rg4), label = "n=50")


# plt.plot(x, Rg1_mean, "--", )
# plt.plot(x, Rg2_mean,"--" , )
# plt.plot(x, Rg3_mean, "--", )
# plt.plot(x, Rg4_mean, "--", )

# plt.xlabel("Step")
# plt.ylabel("$R_g$")
# plt.legend()
# #plt.show()
# plt.savefig('R_g_m=1')



# sf1_full = np.loadtxt("sf_full_n=5.txt")
# sf2_full = np.loadtxt("sf_full_n=10.txt")
# sf3_full = np.loadtxt("sf_full_n=20.txt")
# sf4_full = np.loadtxt("sf_full_n=50.txt")
# k = sf1_full[0]

# plt.loglog(sf1_full[0], sf1_full[1], label = 'n=5')
# plt.loglog(sf2_full[0], sf2_full[1], label = 'n=10')
# plt.loglog(sf3_full[0], sf3_full[1], label = 'n=20')
# plt.loglog(sf4_full[0], sf4_full[1], label = 'n=50')

# #plt.loglog(k, 10.5*k**(-1))
# plt.xlabel("k")
# plt.ylabel("$S(k)$")
# #plt.xlim(0.07, 0.7)
# plt.legend()
# #plt.show()
# plt.savefig('S_f_full_m=1')


sf1_half = np.loadtxt("sf_half_n=5.txt")
sf2_half = np.loadtxt("sf_half_n=10.txt")
sf3_half = np.loadtxt("sf_half_n=20.txt")
sf4_half = np.loadtxt("sf_half_n=50.txt")

plt.loglog(sf1_half[0], sf1_half[1], label = 'n=5')
plt.loglog(sf2_half[0], sf2_half[1], label = 'n=10') 
plt.loglog(sf3_half[0], sf3_half[1], label = 'n=20') 
plt.loglog(sf4_half[0], sf4_half[1], label = 'n=50') 
plt.xlabel("k")
plt.ylabel("$S(k)$")
plt.legend()
#plt.show()
plt.savefig('S_f_half_m=1')