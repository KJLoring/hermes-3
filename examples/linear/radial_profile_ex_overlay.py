from boutdata import collect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d_blue = pd.read_csv("Data/Experimental_Data/blue_dots.csv")
d_red = pd.read_csv("Data/Experimental_Data/red_dots.csv")
d_yellow = pd.read_csv("Data/Experimental_Data/yellow_dots.csv")

#datasets = [("D sim", "ann-gaus/ann-gaus-v29-e1-d", 'k--'),
		#("He sim", "ann-gaus/ann-gaus-v29-e1", 'k.-')]

datasets = [("he_yvar", "ann-iso/ann-iso-gaus-yvar-v2", 'r--')]

yind = 8

for label, path, style in datasets:
	n = collect("Ne", path = path, yind = yind).squeeze()
	nnorm = collect("Nnorm", path = path)
	nav = np.mean(n, axis=(0,2)) * nnorm
	
	g_33 = collect("g_33", path = path, yind = yind).squeeze()
	radius = np.sqrt(g_33) * collect('rho_s0', path = path)
	plt.plot(radius, nav, style, label = label)

plt.scatter(d_blue['radius'], d_blue['density']*1e18)
plt.scatter(d_red['radius'], d_red['density']*1e18)
plt.scatter(d_yellow['radius'], d_yellow['density']*1e18)

plt.axis([0.15, 0.30, 0, 3e18])

plt.xlabel('Radius [m]')
plt.ylabel(r'Average Plasma Density [m$^{-3}$]')
plt.legend()

plt.savefig("Plots/rad_profile.png")

 

