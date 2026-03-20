#%%

import numpy as np
import matplotlib.pyplot as plt

#Definerer kovariansmatrisen
C_123 = np.array([[0.0025,7.5*10**(-4),-1*10**(-3)],[7.5*10**(-4),0.00255,-1.5*10**(-3)],[-1*10**(-3),-1.5*10**(-3),0.01]])
C_12 = np.array([[0.0025,7.5*10**(-4)],[7.5*10**(-4),0.00255]])#kovariasnmatrisen når markedet bare består av  to aksjer

#inverterer matrisen C
invers_123 = np.linalg.inv(C_123)
invers_12 = np.linalg.inv(C_12)

#lager en vektor med forventede avkasntninger
r_vektor = np.array([0.1,0.2,0.2])
r_vektor_2 = np.array([0.1,0.2])
one_3 = np.ones(3) #envektoren med tre elementer
one_2 = np.ones(2)

#beregner konstantene a, b og c
a = r_vektor.T@invers_123@r_vektor
b= one_3.T@invers_123@r_vektor
c = one_3.T@invers_123@one_3

print(f"a = {a:.4f} b = {b:.4f} c = {c:.4f}")
a_2 = r_vektor_2.T@invers_12@r_vektor_2
b_2= one_2.T@invers_12@r_vektor_2
c_2 = one_2.T@invers_12@one_2


def w(r_f):
    
    l = (a-r_f*b)/(a*c-b**2) #løser med hensyn på mu og lambda
    mu = (c*r_f - b)/(a*c-b**2)

    return invers_123@(mu*r_vektor + l*one_3)

def w_2(r_f):
    l = (a_2-r_f*b_2)/(a_2*c_2-b_2**2) #løser med hensyn på mu og lambda
    mu = (c_2*r_f - b_2)/(a_2*c_2-b_2**2)

    return invers_12@(mu*r_vektor_2 + l*one_2)


for r in [0.15,0.2,0.25]:
    w_f = w(r)
    print(f"Ved ønsket avkasnting på {r*100} % bør man investere følgene andeler av portefølgen i de ulike akjene")
    print(f"Aksje 1: {(w_f[0]*100):.2f} %")
    print(f"Aksje 2: {(w_f[1]*100):.2f} %")
    print(f"Aksje 3: {(w_f[2]*100):.2f} %")
    print("-")


def sigma_3(r):
    w_f = w(r) #lager en optimal portefølge for hver ønskede avkastning
    return np.sqrt(w_f@C_123@w_f.T) #beregner risikoen ved hver enkelt portefølge, som må kvadreres

def sigma_2(r):
    w_f = w_2(r) #lager en optimal portefølge for hver ønskede avkastning
    return np.sqrt(w_f@C_12@w_f.T) #beregner risikoen ved hver enkelt portefølge, som må kvadreres


r_verdier = np.linspace(-0.1,0.4,100) #løper gjennom avkasntinger fra -10% til 40%
v_verdier = np.array([sigma_3(r) for r in r_verdier])
t_verdier = np.array([sigma_2(r) for r in r_verdier])
plt.plot(t_verdier,r_verdier,label = "To aksjer")
plt.plot(v_verdier,r_verdier,color = "hotpink",label = "Tre aksjer")
plt.plot(0.05,0.1,"x",label = "Aksje 1", color = "yellow")
plt.plot(0.15,0.2,"x",label = "Aksje 2",color = "green")
plt.plot(0.1,0.2,"x",label = "Aksje 3",color = "black",)
plt.xlabel("Risiko")
plt.ylabel("Avkastning")
plt.grid()
plt.legend()
plt.title("Effesient portefølgefront")
plt.show()

