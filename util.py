import numpy as np 

# Funkce pro výpočet kongruentní periody
def congruent_period(prime, root):
    prime = np.uint64(prime)
    root = np.uint64(root)
    x = 1
    result = None
    for i in range(prime):
        x = int(x*root % prime)
        if x == 1:
            result = i + 1 
            break

    return result

