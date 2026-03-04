#%%

import numpy as np
import matplotlib.pyplot as plt
r_1 = 0.1
r_2 = 0.2

C = 1/100*np.array([[0.5,-1],[-1,8]])


def p(r):
    return np.array([(r-r_2)/(r_1-r_2),(r_1-r)/(r_1 - r_2)]) #oppretter w som en søylevektor


def Var(r): #regner uten å gjøre algebraen for et eksplisitt utrykk
    w = p(r) #lager arrayen for den optimale portefølgefronten gitt en ønsket avkastning r
    varians =  w[0]**2 * C[0][0] +  C[1][1] *w[1]**2 + 2*w[1]*w[0]*C[1][0]
    st = np.sqrt(varians)
    return st
r_verdier = np.linspace(-0.1,0.4,100)



def eks(r):
    return np.sqrt(8.5*r**2 - 1.9*r + 0.115)

plt.plot(Var(r_verdier),r_verdier,".",color = "hotpink",label = "Ved direkte utrening i python")
plt.plot(eks(r_verdier),r_verdier, label = "Chat sin analytiske løsning")
plt.xlabel ("Standardavvik")
plt.ylabel ("Forventet avkasning")
plt.title ("Forventet avkasnting og standardavvik")
plt.grid()
plt.legend()
plt.show()