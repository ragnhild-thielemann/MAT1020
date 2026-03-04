#%%

import numpy as np
import matplotlib.pyplot as plt
S_1 = np.array([1,1.1,1.1,1.2])
S_2 = np.array([1.6,0.8,1.2,1.2])

R_1 = S_1 - 1
R_2 = S_2 - 1

snitt_1 = sum(R_1)/len(S_1)
snitt_2 = sum(R_2)/len(S_2)

r1 = (snitt_1)/1 ;  r2 = (snitt_2)/1

r_vektor = np.array([r1,r2])
print(r_vektor)
#regner varians og kovarians
var_1 = sum([n**2 for n in R_1])/4-snitt_1**2
var_2 = sum([n**2 for n in R_2])/4-snitt_2**2


cov_1_2 = sum([((a-snitt_1)*(b-snitt_2))/4 for a,b in zip(R_1,R_2)]) #regner ut kovariansen

#vi ser at det er en negativ korrlelasjon
C = np.array([[var_1,cov_1_2],[cov_1_2,var_2]])
print(C)
print(f"Standardaviket til den første akjesen er {(np.sqrt(var_1)):.4f}")
print(f"Standardaviket til den første akjesen er {(np.sqrt(var_2)):.4f}")
print(f"Vi ser av dette at den første aksjen har et mindre standaravik enn den andre")

#Bruker matrisemultiplikajson til å regne de to portefølgene

w_1 = np.array([1/4,3/4])
w_2 = np.array([3/4,1/4])

avkastning = w_1.T@r_vektor
varians = w_1.T@C@w_1
stanardavik = np.sqrt(varians)

print(f"For w_1 = [1/4,3/4]^T har vi forventet avkastning {(avkastning*100):.2f} %, med et standardavik på {(stanardavik*100):.2f}%")

avkastning = w_2.T@r_vektor
varians = w_2.T@C@w_2
stanardavik = np.sqrt(varians)

print(f"For w_2 = [3/4,1/4]^T har vi forventet avkastning {(avkastning*100):.2f} %, med et standardavik på {(stanardavik*100):.2f}%")

###

C_inv = np.linalg.inv(C)


en_vektoren = np.ones(2)
print(en_vektoren)


a = r_vektor.T@C_inv@r_vektor
b = en_vektoren.T@C_inv@r_vektor
c = en_vektoren.T@C_inv@en_vektoren
print(a,b,c)


def varians(r):
    return np.sqrt(c*((r-(a/c))**2)/(b*c-a**2) + 1/c)


r_verdier = np.linspace(-1,1)
print(np.sqrt(var_2))
plt.plot(np.sqrt(var_1),snitt_1,"x",label = "aksje 1")
plt.plot(np.sqrt(var_2),snitt_2,"x",label = "aksje 2")
plt.plot(varians(r_verdier),r_verdier,label = "portefølgefront")
plt.xlabel("standardavvik")
plt.ylabel("forventet avkastning")
plt.title("Effesient portefølgefront")
plt.legend()
plt.show()


