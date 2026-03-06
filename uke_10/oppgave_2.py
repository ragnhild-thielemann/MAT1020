#%%

import numpy as np
import matplotlib.pyplot as plt
#a
r = (np.array([[0.4],[0.3],[0.5]])) #vektoren med forventnngen til krafverkene
st_1 = 0.3 ; st_2 = 0.25 ; st_3 = 0.4
#finner kovariansen ved å multiplisere korrelasjonen med de to standardavikene
c_1_2 = 0.4*(st_1*st_2)
c_1_3 = -0.1*(st_1*st_3)
c_2_3 = -0.2*(st_2*st_3)
#Setter dette sammen til en kovariansmatrise

C = np.array([[st_1**2,c_1_2,c_1_3],[c_1_2,st_2**2,c_2_3],[c_1_3,c_2_3,st_3**2]])

r_r_T = (r@r.T)

#b)

b_vektor = C + r_r_T

b_inv = np.linalg.inv(b_vektor)
print(b_inv)
# c) 

mu_r = 200 #det energibehovet vi ønsker å dekke. Vi ønsker å minimere avviket. 

#har vist at følgene allokering gir minst murlig avvik, da det er løsningen av optimeringsproblemet med lagrange

w_optimal = mu_r * (b_inv@r)


print(w_optimal)

r_gjennomsnittlig = w_optimal.T@r

print(f"Gjennomsnittlig strømmengde produsert er {np.sum(r_gjennomsnittlig):.2f}")