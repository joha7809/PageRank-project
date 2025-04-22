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
    for i in range(N):
        if(pagelist)


modified_link_matrix(W1, list(W1.keys()))


