import numpy as np
import matplotlib.pyplot as plt


def sutherland(T):
    T0=288
    S=111
    return ((T/T0)**(1.5))*(T0+S)/(T+S)

def powerlaw(T):
    T0=288
    S=111
    n=1.5-(1/(1+S/T0))
    return (T/T0)**n

def error(T):
    suth=sutherland(T)
    return (powerlaw(T)-suth)/suth


Ts = np.linspace(100,700,50000)
errors = error(Ts)



for i in range(len(Ts)-1):
    if (errors[i+1]<0.05 and errors[i]>0.05) or (errors[i+1]>0.05 and errors[i]<0.05):
        print((Ts[i]+Ts[i+1])/2)



plt.plot(Ts,sutherland(Ts),label="Sutherland")
plt.plot(Ts,powerlaw(Ts), label="Power Law")
plt.legend()
plt.xlabel('T (K)')
plt.ylabel(r'$\mu / \mu_0$')
plt.title('Viscosity calculations')
plt.show()



plt.plot(Ts, errors)
plt.xlabel('T (K)')
plt.ylabel('Relative error')
plt.title('Relative error of power law')
plt.show()
