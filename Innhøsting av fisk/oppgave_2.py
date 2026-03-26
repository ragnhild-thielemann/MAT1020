#%%

import numpy as np
from scipy import integrate

def f(u,r):
    return r*np.sqrt(r**2 + np.sin(u)*2*r + 1)

a = integrate.dblquad(f,0,1,0,2*np.pi)
print(a)