import numpy as np

def make_web(n,k,kmin=0):

    # Input: n og k er ikke-negative heltal
    # Output: web er en dictionary med n nøgler.
    # Værdien af hver nøgle er en liste, der er en delmængde af nøglerne.
    
    assert(k < n), "k skal være mindre end n (da man ikke kan linke til sig selv)"
    assert(kmin <= k), "kmin skal være mindre end eller lig med k"
    keys = # Fjern pass og INDSÆT KODE HER - definér n nøgler fra 0 til n-1 
    web = dict()
    
    for j in keys:
        numlinks = # INDSÆT KODE HER - generér et tilfældigt tal mellem kmin og k
        web[j] = set() # INDSÆT KODE HER - Vælg et antal links (numlinks) fra de andre sider, undgå at vælge den nuværende side (j) og sørg for, at der ikke er duplikatlinks