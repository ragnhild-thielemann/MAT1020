#%%

import matplotlib.pyplot as plt
import numpy as np

#konstanter
r = 1.9
K = 10
b = 2
R = r + 1
 
def i(B):
    return  B

def ricker (B): #Endringen er avtakene
    return B*np.exp(r*(1-B/K))

def logistisk (B): #den logistiske modellen har et nullpunkt, da endringen blir null (etterhvert negativ, men da bryter vi den)
    return B + r*B*(1-B/K)

def BH(B):
    return (R*B)/(1+((R-1)/K)*B)


B_verdier = np.linspace(0,20,100)

plt.plot(B_verdier,i(B_verdier),label = "Identitetsfunksjonen")
plt.plot(B_verdier,ricker(B_verdier),label = "Ricker")
plt.plot(B_verdier[:75],logistisk(B_verdier)[:75],label = "Logistisk") #begrenser den, da verdien på den deriverte blir negativ
plt.plot(B_verdier,BH(B_verdier),label = "Berverton-Holt")
plt.grid()
plt.xlabel("Biomasse B(t)")
plt.ylabel("B(t+1), som tilsvarer den deriverte ved B(t)")
plt.title("Endring i biomassene")
plt.legend()
plt.show()