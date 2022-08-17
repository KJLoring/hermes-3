from boutdata import collect
import numpy as np
import matplotlib.pyplot as plt
import os

path = "ann-iso/ann-he-tvar-v5"
yind = 8 #location along length of machine (range 0-15)
#zind = 0 #azimuthal angle (range 0-63)

#electron density
n = collect("Ne", path = path, yind = yind).squeeze() #squeeze out the y dimension

#potential
phi = collect("phi", path = path, yind = yind).squeeze() #squeeze out the y dimension

#picking out only one z:
#n = n[:, :, zind]
#n = n.squeeze()

#phi = phi[:, :, zind]
#phi = phi.squeeze()

#radius 
g_33 = collect("g_33", path=path, yind=yind).squeeze()
radius = np.sqrt(g_33) * collect("rho_s0", path=path)


#how many radial points are there (s/b 64 for both xlen and zlen for standard resolution)
xlen = n[0,:,zind].size
zlen = n[0,0,:].size

#define placeholder for data
cos_nphi_2d = np.zeros([n.shape[0], n.shape[1]]) # for only doing x, zind fixed

cos_nphi_3d = np.zeros([n.shape[0], n.shape[1], n.shape[2]]) #for doing both x and z and then eventually avg over z

#compute cosine of angle difference and append to a data placeholder
for z in range(0,zlen):
    for x in range(0,xlen):
        n_xz_signal = n[:, x, z] #pulling 1D temporal density signal at position (x,z)
        phi_xz_signal = phi[:, x, z] #1D temporal potential signal at position (x,z)
        
        #compute dft of each 1D signal
        n_xz_dft = np.fft.fft(n_xz_signal)
        phi_xz_dft = np.fft.fft(phi_xz_signal)
        
        #compute angle of fourier transform
        n_xz_angle = np.angle(n_xz_dft)
        phi_xz_angle = np.angle(phi_xz_dft)
        
        #subtract the angle arrays from one another
        ang_diff_xz = n_xz_angle - phi_xz_angle
        
        #cosine of difference in angles
        cos_nphi_xz = np.cos(ang_diff_xz)
        
        #append to data placeholder
        cos_nphi_3d[:, x, z] = cos_nphi_xz

        
#collect time
time = collect("t_array", path = path)
time = 1e3 * time / collect("Omega_ci", path = path)

#timestep size [ms maybe?]
dt = time[2] - time[1]

freqs = np.fft.fftfreq(n=n[:,0,0].size, d=dt) #includes negative frequencies

#gather only the positive frequencies
if timeseries.size%2 == 0: 
    neg_start = (timeseries.size/2)
else:
    neg_start = int((timeseries.size + 1)/2)

freqs_pos = freqs[0:neg_start]

#slice off portion of cos_nphi_3D which corresponds to negative frequencies:
cos_nphi_3d_pf = cos_nphi_3d[0:neg_start, :, :]

#slice off portion of 3D array corresponding to single zind (z=0)
#will come back later and average over z
cos_nphi_2d_pf = cos_nphi_3d_pf[:, :, 0].reshape([cos_nphi_3d_pf.shape[0], cos_nphi_3d_pf.shape[1]])

plt.contour(radius, freqs_pos, cos_nphi_2d_pf)
plt.colorbar()
plt.xlim([0.15, 0.30])
plt.yscale("log")
plt.show()