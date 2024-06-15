import numpy as np
import matplotlib.pyplot as plt


def calc(u):
    int_pos = u - 5*np.log(u+1)-10/(u+1)+5/((u+1)**2)-5/(3*(u+1)**3)+1/(4*(u+1)**4)
    int_neg = 10 - 5 + 5./3 - 0.25
    scale = ((1+u)/u)**5
    # print(int_pos + int_neg)
    # print(np.trapz(integrand(np.linspace(0,u,100000)),dx=u/100000))
    return 0.45*scale*(int_pos+int_neg)

def par(u):
    return np.sqrt(calc(u))

def integrand(u):
    return (u/(1+u))**5

def thetabyx(u):
    return par(u)/np.sqrt(u)

def thetabyl(u):
    return par(u)/np.sqrt(u/(1+u))

def calc_lambda(u):
    return calc(u)/(u*(1+u))


def calc_lambda2(u,y):
    return (y**2)*(1-u/(1+u))

# plot
us = np.linspace(15e-3,10,1000)
ys = thetabyx(us)
yls = thetabyl(us)
x_ac = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 4, 6, 8, 10]
y_ac = [0.292,0.310,0.325,0.339,0.351,0.362,0.403,0.452,0.482,0.503,0.519]

for i in range(len(x_ac)):
    print((thetabyx(x_ac[i]+5e-3)-y_ac[i])/y_ac[i])

print("lambda")
for i in range(len(x_ac)):
    print((calc_lambda(x_ac[i]+15e-3)-calc_lambda2(x_ac[i],y_ac[i]))/calc_lambda2(x_ac[i],y_ac[i]))


l_ac = []
for i in range(len(x_ac)):
    l_ac.append(calc_lambda2(x_ac[i],y_ac[i]))
ls = calc_lambda(us)

plt.plot(us,ys,label=r'$\frac{\theta} {x} \sqrt{u_e x / \nu}$')
plt.plot(us,yls,label=r'$\frac{\theta} {L} \sqrt{U_0 L / \nu}$')
plt.plot(x_ac,y_ac,'o',label='Data')
plt.xlabel('x/L')
plt.ylabel('Value')
plt.title('Development of Boundary Layer')
plt.legend()
plt.savefig('figures/4F1.png')
plt.show()

plt.plot(us,ls,label=r'$\lambda$')
plt.plot(x_ac,l_ac,'o',label='Data')
plt.xlabel('x/L')
plt.ylabel('Value')
plt.title('Correlation Parameter')
plt.legend()
plt.savefig('figures/4F2.png')
plt.show()