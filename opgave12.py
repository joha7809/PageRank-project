from opgave4 import W1,W2
from opgave9 import surf_step

import numpy as np
import random as rd

def random_surf_damp(web, n, d=0.85, stop_value=0):

    # Input: Et netværk som dictionary og antallet af skridt i random surf simuleringen
    # Output: PageRank-værdier for hver side som en dictionary

    # visits er hvor mange gange en hjemmeside er blevet besøgt
    visits = {key:0 for key in web.keys()}
    # ranking er hvor mange gange en hjemmeside er blevet besøgt ud af mængden af totale besøg
    ranking = {key:0 for key in web.keys()}
    # forrige ranking så vi kan sammenligne ændringen
    prev_ranking = {key:0 for key in web.keys()}

    current_page = np.random.choice(list(web.keys()), 1)[0]

    for i in range(1, n+1):
        random_val = rd.random()
        # tjekker om der skal gås til en tilfældig side
        if random_val<=d:
            prob = surf_step(web,current_page)
            # next indeholder de sider current page linker til
            next = [key for key, value in prob.items() if value != 0]
            # der vælges en tilfældig side fra next
            current_page = np.random.choice(next, 1)[0] if len(next) else np.random.choice(list(web.keys()), 1)[0]

        else:
            current_page = np.random.choice(list(web.keys()), 1)[0]

        visits[current_page] += 1
        
        # ranking opdaters ud fra visits og mængden af totale besøg
        for page in visits:
            ranking[page] = visits[page]/(i)

        # den største ændring findes og hvis den er mindre end stop_value stopper loopet
        max_increment = max(abs(ranking[k] - prev_ranking[k]) for k in ranking)
        if max_increment < stop_value: break

        # prev_ranking opdateres
        for page in ranking:
            prev_ranking[page] = ranking[page]

    return ranking, i