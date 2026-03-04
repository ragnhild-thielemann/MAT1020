#%%

import numpy as np
import matplotlib.pyplot as plt
r_1 = 0.1
r_2 = 0.2


C = 1/100*np.array([[0.5,-1],[-1,8]])


def optimal(r):
    return np.array([(r-r_2)/(r_2-r_1),(2*r_2 - r_1 + r)/(r_2 - r_1)]) #oppretter w som en søylevektor


def Var(r):
    w = optimal(r) #lager arrayen for den optimale portefølgefronten
    varians =  w[0]**2 * C[0][0] + w[1]**2 + C[1][1] *w[1]**2 + 2*w[1]*w[0]*C[1][0]
    st = np.sqrt(varians)
    return st
r_verdier = np.linspace(-1,1,100)

plt.plot(Var(r_verdier),r_verdier)




