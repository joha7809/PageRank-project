#Fra opgave 9
from opgave9 import surf_step
#Fra opgave 4
from opgave4 import W1,W2

from opgave10 import random_surf

import numpy as np
import random as rd




def random_surf_damp(web, n, d):

    # Input: Et netværk som dictionary og antallet af skridt i random surf simuleringen
    # Output: PageRank-værdier for hver side som en dictionary

    ranking=dict()
    
    # INDSÆT KODE HER


    ranking = {key:0 for key in web.keys()}
    
    current_page = np.random.choice(list(web.keys()), 1)[0]

    for i in range(n):
        random_val = rd.random()
        if random_val<=d:
            prob = surf_step(web,current_page)
            next = [key for key, value in prob.items() if value != 0]

            current_page = np.random.choice(next, 1)[0] if len(next) else np.random.choice(list(web.keys()), 1)[0]

        else:
            current_page = np.random.choice(list(web.keys()), 1)[0]

        ranking[current_page] += 1/n


        
        

        

    return ranking

if __name__ == "__main__":
    print(random_surf_damp(W1,10000, 0.85))
    print(random_surf(W1, 10000))