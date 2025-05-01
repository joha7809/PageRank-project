import numpy as np
import random

def make_web(n,k,kmin=0, seed=2039293273):

    # Input: n og k er ikke-negative heltal
    # Output: web er en dictionary med n nøgler.
    # Værdien af hver nøgle er en liste, der er en delmængde af nøglerne.
    
    assert(k < n), "k skal være mindre end n (da man ikke kan linke til sig selv)"
    assert(kmin <= k), "kmin skal være mindre end eller lig med k"
    keys = [n for n in range(0, n)]
    web = dict()
    random.seed(seed)
    np.random.seed(seed)
    for j in keys:
        numlinks = random.randint(kmin, k)
        keys_excluded_j = keys[:] # Makes a deep copy of the keys list
        keys_excluded_j.remove(j)
        web[j] = set(int(link) for link in np.random.choice(keys_excluded_j, numlinks, replace=False))

    return web