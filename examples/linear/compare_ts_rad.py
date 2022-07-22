
from boutdata import collect
import numpy as np
import matplotlib.pyplot as plt
import os

var = "Ne"
ylabel = r"Electron density [m$^{-3}$]"
inds = [(2,8,0), (32, 8, 0), (54, 8, 0), (12, 0, 0), (12,8,0)]
path = os.path.join("ann-iso/annulus-isothermal-he-yvar", ".")
norm = collect("Nnorm", path=path)

data1 = norm * collect(var, path=path, xind = inds[0][0], yind=inds[0][1], zind=inds[0][2]).squeeze()
data2 = norm * collect(var, path=path, xind=inds[1][0], yind=inds[1][1], zind=inds[1][2]).squeeze()
data3 = norm * collect(var, path=path, xind=inds[2][0], yind=inds[2][1], zind=inds[2][2]).squeeze()
data4 = norm * collect(var, path=path, xind=inds[3][0], yind=inds[3][1], zind=inds[3][2]).squeeze()
data5 = norm * collect(var, path = path, xind=inds[4][0], yind=inds[4][1], zind=inds[4][2]).squeeze()
x_data = 1e3 * collect("t_array", path = path) / collect("Omega_ci", path = path)

fig, ax = plt.subplots()

plt.plot(x_data,data1, axes = ax, c = 'b', label = str(inds[0][0]) + "_" + str(inds[0][1]))
plt.plot(x_data, data2, axes = ax, c ='r', label = str(inds[1][0]) + "_" + str(inds[1][1]))
plt.plot(x_data, data3, axes = ax, c = 'g', label = str(inds[2][0]) + "_" + str(inds[2][1]))
plt.plot(x_data, data4, axes = ax, c = 'c', label = str(inds[3][0]) + "_" + str(inds[3][1]))
plt.plot(x_data, data5, axes = ax, c = 'k', label = str(inds[4][0]) + "_" + str(inds[4][1]))

plt.xlabel("Time [ms]")
plt.ylabel(ylabel)
plt.legend()

plt.savefig("Plots/" + "rad_ts_comp.png")

