

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
A= 324.196
B= -134.196

x_1 =( 1+np.sqrt(17))/8
x_2 = (1-np.sqrt(17))/8
def syk(n):
    if n == 0:
        return A*x_1**n + B*x_2**n
    
    if n == 1: 
        return A*x_1**n + B*x_2**n
    
    else:
        return 0.23*syk(n-1) + 0.25*syk(n-2)
    
print(syk(10))

def ja(n):
    return A*x_1**n + B*(x_2**n)

print(ja(10))