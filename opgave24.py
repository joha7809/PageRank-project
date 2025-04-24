from opgave4 import W1
from opgave4 import W2
from opgave17 import modified_link_matrix
import numpy as np
from scipy.linalg import null_space

def eigenvector_PageRank(web,d=0.85):
    # Input: web er en ordbog over websider og links.
    # d er dæmpningen
    # Output: En ordbog med de samme nøgler som web og værdierne er PageRank for nøglerne

    ranking = dict()

    # INDSÆT KODE HER
    
    # variabel oprettes, der opbevarer vores modified link matrix
    md = modified_link_matrix(web, list(web),d=d)

    # identitetsmatricen trækkes fra og kernen findes for at finde egenvektoren til egenværdien 1
    md = md-np.identity(len(web))
    eigenvector = null_space(md)

    # vektoreren normaliseres så summen af elementerne er 1.
    eigenvector /= sum(eigenvector)
    
    #Vi laver et dictionary, der keys er hjemmesider og values er pageranking
    ranking = {page : rank[0] for page, rank in zip(web, eigenvector)}
    return ranking
print(eigenvector_PageRank(W1))