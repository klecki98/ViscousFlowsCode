import matplotlib.pyplot as plt
import numpy as np



def theta(eta, Pr):
    return np.exp(-Pr*eta)

def f1(eta):
    return 1 - np.exp(-eta)

etas = np.linspace(0, 10, 1000)
Prs = [0.5, 1.0, 2.0]

plt.plot(etas, f1(etas), label='f\'')
for Pr in Prs:
    plt.plot(etas, theta(etas, Pr), label=r'$\theta$, Pr = {}'.format(Pr))
plt.legend()
plt.xlabel('$\eta_2$')
plt.ylabel('Value')
plt.title('Asymptotic Solution')
plt.savefig('figures/5F.png')
plt.show()