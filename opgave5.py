import numpy as np
import random

def make_web(n,k,kmin=0):

    # Input: n og k er ikke-negative heltal
    # Output: web er en dictionary med n nøgler.
    # Værdien af hver nøgle er en liste, der er en delmængde af nøglerne.
    
    assert(k < n), "k skal være mindre end n (da man ikke kan linke til sig selv)"
    assert(kmin <= k), "kmin skal være mindre end eller lig med k"
    keys = [n for n in range(0, n)]
    web = dict()
    
    for j in keys:
        numlinks = random.randint(kmin, k)
        keys2 = keys[:]
        keys2.remove(j)
        web[j] = set(np.random.choice(keys2, numlinks, replace=False))
        print(web[j])

make_web(10,5)