import numpy as np
import matplotlib.pyplot as plt


kappa = 0.41
B = 5.0

def dydu(u_plus):
    return 1+np.exp(-kappa*B)*(np.exp(kappa*u_plus)-1-kappa*u_plus-(1/2)*kappa**2*u_plus**2)

def y_plus(u_plus):
    # Spalding's law of the wall
    return u_plus+np.exp(-kappa*B)*(np.exp(kappa*u_plus)-1-kappa*u_plus-(1/2)*kappa**2*u_plus**2-(1/6)*kappa**3*u_plus**3)

def visc(u_plus):
    return dydu(u_plus)-1

def visc_approx(u_plus):
    return (kappa**4*np.exp(-kappa*B)*u_plus**3)/6

def lmix(u_plus):
    return np.sqrt(dydu(u_plus)**2-dydu(u_plus))

def lmix_approx(u_plus):
    return (kappa**2*np.exp(-kappa*B/2)*u_plus**1.5)/np.sqrt(6)

def u_plus(y_plus):
    return (1/kappa) * np.log(y_plus) + B

def van_driest(y_plus):
    return kappa*y_plus*(1-np.exp(-y_plus/24.5))

u_plus_vals = np.linspace(1e-3, u_plus(10000), 1000)

plt.figure()
plt.loglog([y_plus(u) for u in u_plus_vals], [visc(u) for u in u_plus_vals],'b', label=r"$\frac{\nu_T}{\nu}$")
plt.loglog([y_plus(u) for u in u_plus_vals], [visc_approx(u) for u in u_plus_vals],'b--', label=r"$\frac{\nu_T}{\nu}$ approx")
plt.loglog([y_plus(u) for u in u_plus_vals], [lmix(u) for u in u_plus_vals],'m', label=r"$l_{mix} v^* / \nu$")
plt.loglog([y_plus(u) for u in u_plus_vals], [lmix_approx(u) for u in u_plus_vals],'m--', label=r"$l_{mix} v^* / \nu$ approx")
plt.loglog([y_plus(u) for u in u_plus_vals], [van_driest(y_plus(u)) for u in u_plus_vals],'m:', label=r"van Driest")
#plt.loglog([y_plus(u) for u in u_plus_vals], u_plus_vals, label=r"$u^+$")
plt.xlabel(r"$y^+$")
plt.ylabel(r"value")
plt.title("turbulent boundary layer")
plt.legend()
plt.savefig("figures/8a.png")


u_plus_vals = np.linspace(0, u_plus(100), 1000)
plt.figure()
plt.plot([y_plus(u) for u in u_plus_vals], [visc(u) for u in u_plus_vals],'b', label=r"$\frac{\nu_T}{\nu}$")
#plt.semilogy([y_plus(u) for u in u_plus_vals], [visc_approx(u) for u in u_plus_vals],'b--', label=r"$\frac{\nu_T}{\nu}$ approx")
plt.plot([y_plus(u) for u in u_plus_vals], [lmix(u) for u in u_plus_vals],'m', label=r"$l_{mix} v^* / \nu$")
#plt.semilogy([y_plus(u) for u in u_plus_vals], [lmix_approx(u) for u in u_plus_vals],'m--', label=r"$l_{mix}$ approx")
#plt.semilogy([y_plus(u) for u in u_plus_vals], u_plus_vals, label=r"$u^+$")
plt.xlabel(r"$y^+$")
plt.ylabel(r"value")
plt.title("turbulent boundary layer")
plt.legend()
#plt.ylim(1e-3, 1e2)
plt.savefig("figures/8a_2.png")
plt.show()