import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

Ue=11.197
nu = 15e-6


ys = []
u_norms = []


f = open("7B_data.txt")
for line in f:
    data = line.split(" ")
    ys.append(float(data[1])*1e-3)
    u_norms.append(float(data[2]))
f.close()


us = [u_norm*Ue for u_norm in u_norms] 


plt.semilogx([y*Ue/nu for y in ys], u_norms)
plt.xlabel(r"$Re_y$")
plt.ylabel(r"$\frac{u}{U_e}$")
plt.title("Velocity profile")
plt.savefig("figures/7B.png")

# 2.50mm last in inner
lim1 = 6
lim2 = 13

kappa = 0.41
B = 5.0

def u_plus(y_plus):
    return (1/kappa) * np.log(y_plus) + B

def y_plus(y, v_star, nu):
    return y*v_star/nu

def y_plus2(u_plus):
    # Spalding's law of the wall
    return u_plus+np.exp(-kappa*B)*(np.exp(kappa*u_plus)-1-kappa*u_plus-(1/2)*kappa**2*u_plus**2-(1/6)*kappa**3*u_plus**3)

def u_plus2(u, v_star):
    return u/v_star

def u_fun(y, v_star):
    # returns u
    return u_plus(y_plus(y, v_star, nu))*v_star

def y_fun(u, v_star):
    # returns y
    return y_plus2(u_plus2(u, v_star))*nu/v_star

param, param_cov = curve_fit(u_fun, ys[lim1:lim2], us[lim1:lim2], bounds=(0, np.inf))

v_star = param[0]

print("v_star: ", v_star)
print(param_cov)
print("Cf: ", 2*((v_star/Ue)**2))


plt.semilogx([y*Ue/nu for y in ys[lim1:lim2]], [u_fun(y, v_star)/Ue for y in ys[lim1:lim2]], label="fit")
plt.savefig("figures/7B_data.png")
ys_fit = np.linspace(ys[0], ys[-1], 10000)
us_fit = np.linspace(us[0], us[-1], 10000)

plt.figure()
plt.semilogx([y_plus(y, v_star, nu) for y in ys], [u_plus2(u, v_star) for u in us], label="data")
plt.semilogx([y_plus(y, v_star, nu) for y in ys_fit], [u_plus(y_plus(y, v_star, nu)) for y in ys_fit], label="fit")
plt.xlabel(r"$y^+$")
plt.ylabel(r"$u^+$")
plt.title("Velocity profile")
plt.legend()
plt.savefig("figures/7B_fit.png")


u_plus_fit = [u_plus(y_plus(y, v_star, nu)) for y in ys_fit]
y_plus_fit = [y_plus(y, v_star, nu) for y in ys_fit]

diffs = []
for i in range(len(ys)):
    diffs.append(u_plus2(us[i], v_star)-np.interp(y_plus(ys[i],v_star,nu), y_plus_fit, u_plus_fit))

# print(diffs)
print("Max_diff scaled: ", np.max(diffs))
print("Max_diff: ", np.max(diffs)*v_star)


param, param_cov = curve_fit(y_fun, us[:lim2], ys[:lim2], bounds=(0, np.inf))

v_star = param[0]

print("v_star: ", v_star)
print(param_cov)
print("Cf: ", 2*((v_star/Ue)**2))

plt.figure()
plt.semilogx([y_plus(y, v_star, nu) for y in ys], [u_plus2(u, v_star) for u in us], label="data")
plt.semilogx([y_plus2(u_plus2(u,v_star)) for u in us_fit], [(u_plus2(u,v_star)) for u in us_fit], label="fit")
plt.xlabel(r"$y^+$")
plt.ylabel(r"$u^+$")
plt.title("Velocity profile")
plt.legend()
plt.savefig("figures/7B_fit2.png")


u_plus_fit = [(u_plus2(u,v_star)) for u in us_fit]
y_plus_fit = [y_plus2(u_plus2(u,v_star)) for u in us_fit]

diffs = []
for i in range(len(ys)):
    diffs.append(u_plus2(us[i], v_star)-np.interp(y_plus(ys[i],v_star,nu), y_plus_fit, u_plus_fit))

# print(diffs)
print("Max_diff scaled: ", np.max(diffs))
print("Max_diff: ", np.max(diffs)*v_star)
