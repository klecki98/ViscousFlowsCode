import numpy as np



# Initial conditions
fw2 = 0.0
fw0 = -np.sqrt(2)

# Functions
def f1(eta,f0,fw2=fw2,fw0=fw0):
    return (0.5*eta**2)+fw2*eta-(0.5*f0**2)+(0.5*fw0**2)

def f0_plus(f0,f1,deta):
    # Euler method
    return f0 + deta*f1

def f2(eta,f0,f1,fw2=fw2):
    if eta==0.0:
        return fw2
    return eta-f0*f1+fw2

# Initialize
eta = 0.0
xlim = 5.0
deta = 10**-5
f1s = []
f0s = [fw0]
f2s = [fw2]
f1s.append(f1(eta,f0s[-1]))

# Loop
while eta<=xlim:
    f0s.append(f0_plus(f0s[-1],f1s[-1],deta))
    f1s.append(f1(eta,f0s[-1]))
    f2s.append(f2(eta,f0s[-1],f1s[-1]))
    eta += deta

# Print displacement thickness
print((len(f1s)-sum(f1s))*deta)

# Plot
import matplotlib.pyplot as plt
etas = np.linspace(0,xlim,len(f1s))
plt.plot(etas,f1s,label=r'$f_w=-\sqrt{2}$')

fw0 = np.sqrt(2)
eta = 0.0
f1s = []
f0s = [fw0]
f2s = [fw2]
f1s.append(f1(eta,f0s[-1]))

# Loop
while eta<=xlim:
    f0s.append(f0_plus(f0s[-1],f1s[-1],deta))
    f1s.append(f1(eta,f0s[-1]))
    f2s.append(f2(eta,f0s[-1],f1s[-1]))
    eta += deta

# Print displacement thickness
print((len(f1s)-sum(f1s))*deta)

plt.plot(etas,f1s,label=r'$f_w=\sqrt{2}$')
plt.xlabel(r"$\eta$")
plt.ylabel(r"$f^{/}$")
plt.title(r"$f^{/}$ vs $\eta$")
plt.legend()
plt.savefig("figures/3C.png")
plt.show()



