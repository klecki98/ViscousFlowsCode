import numpy as np
import matplotlib.pyplot as plt

def analyze(eta):
    A = A1*np.sinh(a*eta)*np.cos(a*eta)+A2*np.cosh(a*eta)*np.sin(a*eta)
    B = B1*np.sinh(a*eta)*np.cos(a*eta)+B2*np.cosh(a*eta)*np.sin(a*eta)
    Amp = (A**2 + B**2)**0.5
    phi = np.arccos(A/Amp)
    return A, B, Amp, phi

a = np.pi
A1 = (np.sinh(a)*np.cos(a)+(1/np.tanh(a))*np.tan(a)*np.cosh(a)*np.sin(a))**(-1)
A2 = A1*(1/np.tanh(a))*np.tan(a)
B1 = A2
B2 = -A1

print(A1,A2,B1,B2)

etas = np.linspace(0,1,4000)

tanphi0=((1/np.tanh(a))*np.tan(a)-1)/((1/np.tanh(a))*np.tan(a)+1)
print(tanphi0)
print(np.arctan(tanphi0)+np.pi)

As,Bs,Amps,phis = analyze(etas)
plt.plot(etas,As, label='A')
plt.plot(etas,Bs, label='B')
plt.plot(etas,Amps, label='Amp')
plt.plot(etas,phis, label=r'$\phi$')
plt.xlabel(r"$\eta$")
plt.ylabel('Values of A, B, Amp, $\phi$')
plt.title('Values of A, B, Amp, $\phi$ vs $\eta$')
plt.legend()
plt.show()

for i in range(5):
    label = r"$\omega t=$"+str(i)+r"$\times \pi /4$"
    plt.plot(etas,As*np.cos(i*np.pi/4)+Bs*np.sin(i*np.pi/4), label=label)
plt.xlabel(r"$\eta$")
plt.ylabel(r"$U/U_0$")
plt.title(r"$U/U_0$ vs $\eta$ for different $\omega t$")
plt.legend()
plt.show()

# print(A,B)
# print(phis)
# print(A/Amp, np.cos(phi))
# print(B/Amp, np.sin(phi))