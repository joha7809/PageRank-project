from opgave4 import W1
from opgave4 import W2
from opgave17 import modified_link_matrix
import numpy as np

def eigenvector_PageRank(web,d=0.85):
    # Input: web er en ordbog over websider og links.
    # d er dæmpningen
    # Output: En ordbog med de samme nøgler som web og værdierne er PageRank for nøglerne

    ranking = dict()

    # INDSÆT KODE HER
    
    #variabel oprettes, der opbevarer vores modified link matrix
    md = modified_link_matrix(web, list(web),d=d)

    #vi udregner vores eigenværdier og eigenvektorer
    vals, vects = np.linalg.eig(md)

    #indeks, der for den eigenværdi, der er tættest på 1
    index = np.argmin(np.abs(vals - 1))

    #vi definerer og normaliserer vores eigenvektorer
    eigenvector = vects[:,index]
    eigenvector /= sum(eigenvector)

    #Vi laver et dictionary, der keys er hjemmesider og values er pageranking
    ranking = {page : rank for page, rank in zip(web, eigenvector)}
    return ranking

