import numpy as np
from opgave17 import modified_link_matrix
from opgave4 import W1, W2


def matrix_PageRank(web,power,d=0.85):

    # Input: web er et dictionary med websider og links.
    # d er en positiv float, dæmpningskonstanten.
    # Output: Et dictionary med de samme nøgler som web, og værdierne er PageRank for hver nøgle.

    ranking = dict()

    md = modified_link_matrix(web, list(web), d=d)

    md = np.linalg.matrix_power(md, power)

    ranking = {page : rank for page, rank in zip(web, md[:,0])}
    
    return ranking

matrix_PageRank(W1,1)