import numpy as np
import matplotlib.pyplot as plt

Rexs = np.linspace(0, 1e7, 10000)
Rex_trans = 1.8e6

def Ret(Rex):
    if Rex <= Rex_trans:
        A=0.45
        n=1
        return (A*Rex)**(1/(n+1))
    else:
        A=0.0076
        n=1/6
        Rex_start = (1/A)*(Ret(Rex_trans)**(n+1))
        return (A*(Rex-Rex_trans+Rex_start))**(1/(n+1))


A=0.0076
n=1/6
Rex_start = (1/A)*(Ret(Rex_trans)**(n+1))
print(Rex_trans-Rex_start)

plt.plot(Rexs, [Ret(Rex) for Rex in Rexs], label=r"$Re_\theta$")
plt.scatter([Rex_trans-Rex_start],0, label="Virtual origin")
plt.legend()
plt.xlabel(r'$Re_x$')
plt.ylabel(r'$Re_\theta$')
plt.title(r'$Re_\theta$ vs $Re_x$')
plt.savefig('figures/6D.png')
plt.show()

