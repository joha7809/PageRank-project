import numpy as np
from opgave4 import W1, W2

def modified_link_matrix(web, pagelist, d=0.85):

    # Input: web (dictionary), pagelist (liste over nøgler), d (dæmpningsfaktor)
    # Output: d*A^T + (1-d)*E/N
    
    # A: NxN numpy array, hvor række j har ikke-nul elementer i søjler, som side j linker til.
    # Hvis side j ikke linker til nogen, får alle elementer i række j værdien 1/N.
    # E: np.ones([N,N])
    
    # INDSÆT KODE HER

    N = len(web.keys())
    A = np.zeros([N, N])
    for page, i in zip(pagelist, range(N)):
        links = web[page]
        links_len = len(links)

        if not links:
            #Handles sinks
            A[i] = [1/N for _ in range(N)]
            continue

        for k in links:
            idx = pagelist.index(k)
            A[i,idx] = 1/links_len

    E = np.ones([N,N])
    
    return d*A.transpose()+(1-d)*E/N



modified_link_matrix(W1, list(W1.keys()))


