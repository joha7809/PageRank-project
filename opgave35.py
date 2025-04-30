import numpy as np
from opgave17 import modified_link_matrix
from opgave4 import W1, W2


def matrix_PageRank(web, power, d=0.85, stop_value=0):

    # Input: web er et dictionary med websider og links.
    # d er en positiv float, dæmpningskonstanten.
    # Output: Et dictionary med de samme nøgler som web, og værdierne er PageRank for hver nøgle.

    md = modified_link_matrix(web, list(web), d=d)
    # original md som vi ganger med i loopet
    original_md = md.copy()
    # forrige md så vi kan sammenligne ændringen
    previous_md = md.copy()
    i = 0
    for i in range(1, power):
        md = md @ original_md
        # finder den største forskel mellem md og previous_md
        if max(map(abs, md[:,0]-previous_md[:, 0])) < stop_value: break

        previous_md = md.copy()

    ranking = {page : rank for page, rank in zip(web, md[:,0])}

    return ranking, i+1