def surf_step(web, page):
    
    # Input: Et netværk som dictionary og en start side
    # Output: Sandsynlighedsfordeling som dictionary for næste hjemmeside
    
    distribution=dict()

    # INDSÆT KODE HER
   
    #ex ['p1', 'p2' ... 'p5']
    nodes = web.keys()

    #ex 'p1' = {'p3', 'p5'}
    edges = web.get(page)

    # 1/N
    chance = 1/len(edges) if len(edges) != 0 else 0

    #ex dict = {'p1': {'p2'} ... 'p5': {'p4'}}
    for key in nodes:
        if key in edges:
            distribution[key] = chance
        else:
            distribution[key] = 0
        
    return distribution


#Fra opgave 4
from opgave4 import W1,W2


#print(surf_step(W1,'p1'))