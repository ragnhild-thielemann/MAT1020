#%%

import numpy as np
import matplotlib.pyplot as plt

#Definerer kovariansmatrisen
C = np.array([[0.0025,7.5*10**(-4)],[7.5*10**(-4),0.00255]])

print(C)

#inverterer matrisen C
invers = np.linalg.inv(C)
#lager en vektor med forventede avkasntninger
r_vektor = np.array([0.1,0.2])
one = np.ones(2) #envektoren med tre elementer


#beregner konstantene a, b og c
a = r_vektor.T@invers@r_vektor
b = one.T@invers@r_vektor
c = one.T@invers@one



def w(r_f):
    
    l = (a-r_f*b)/(a*c-b**2) #løser med hensyn på mu og lambda
    mu = (c*r_f - b)/(a*c-b**2)

    return invers@(mu*r_vektor + l*one)


for r in [0.15,0.2,0.25]:
    w_f = w(r)
    print(f"Ved ønsket avkasnting på {r*100} % bør man investere følgene andeler av portefølgen i de ulike akjene")
    print(f"Aksje 1: {(w_f[0]*100):.2f} %")
    print(f"Aksje 2: {(w_f[1]*100):.2f} %")
    print("-")


def sigma(r):
    w_f = w(r) #lager en optimal portefølge for hver ønskede avkastning
    return np.sqrt(w_f@C@w_f.T) #beregner risikoen ved hver enkelt portefølge, som må kvadreres

r_verdier = np.linspace(-0.1,0.4,100) #løper gjennom avkasntinger fra -10% til 40%
v_verdier = np.array([sigma(r) for r in r_verdier])

plt.plot(v_verdier,r_verdier,color = "hotpink",label = "Effesient portefølge")
plt.plot(0.05,0.1,"x",label = "Aksje 1")
plt.plot(0.15,0.2,"x",label = "Aksje 2")
plt.plot(0.1,0.2,"x",label = "Aksje 3")
plt.xlabel("Risiko")
plt.ylabel("Avkastning")
plt.grid()
plt.legend()
plt.title("Effesient portefølgefront")
plt.show()

