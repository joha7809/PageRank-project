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
    chance = 1/len(edges)

    #ex dict = {'p1': {'p2'} ... 'p5': {'p4'}}
    for key in nodes:
        if key in edges:
            distribution[key] = chance
        else:
            distribution[key] = 0
        
    return distribution


#Fra opgave 4
W1 = {'p1': {'p3', 'p5'}, 'p2': {'p4', 'p5'}, 'p3': {'p1'}, 'p4': {'p1', 'p2', 'p5'}, 'p5': {}}
W2 = {'P1': {'P2'}, 'P2': {'P2'}, 'P3': {'P1'}, 'P4': {'P5'}, 'P5': {'P6'}, 'P6': {'P4'}}


print(surf_step(W1,'p1'))