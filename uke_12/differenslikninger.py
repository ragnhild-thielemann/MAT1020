

#%%

def x_verdier(n):
    if n == 0:
        return 2
    if n == 1:
        return -3 + 2
    
    else:
        return -x_verdier(n-1) + 6 *x_verdier(n-2)
    
print(x_verdier(10))

#%%

def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(4))

#%%
import numpy as np
import matplotlib.pyplot as plt
A_a= 200
B_a= -10

x_1_a = 5/4
x_2_a = -1

A_c = 230
B_c = -40
x_1_c = 1
x_2_c= -3/4

def syk(n,A,B,x_1,x_2,smitte):
    if n == 0:
        return A*x_1**n + B*x_2**n
    
    if n == 1: 
        return A*x_1**n + B*x_2**n
    
    else:
        return 0.25*syk(n-1,A,B,x_1,x_2,smitte) + smitte *syk(n-2,A,B,x_1,x_2,smitte)
    


n_verdier = []
a_verdier = []
b_verdier = []
for n in range(5):
    n_verdier.append(n)
    a_verdier.append(syk(n,A_a,B_a,x_1_a,x_2_a,5/4))
    b_verdier.append(syk(n,A_c,B_c,x_1_c,x_2_c,3/4))

plt.ylabel("Antall syke")
plt.xlabel("Uker")
plt.plot(n_verdier,b_verdier,label = "Oppgave c",color = "hotpink")

plt.plot(n_verdier,a_verdier,label = "Oppgave b")
plt.title("Sykdomsutvikling")
plt.grid()
plt.legend()
plt.show()