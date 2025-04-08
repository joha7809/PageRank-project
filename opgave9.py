def surf_step(web, page):
    
    # Input: Et netværk som dictionary og en start side
    # Output: Sandsynlighedsfordeling som dictionary for næste hjemmeside
    
    distribution=dict()

    # INDSÆT KODE HER
    
    
    next = []
    x = [0.0 for i in range(len(W1))]
    x[page-1] = 1.0

    chance = [0.0 for i in range(len(W1))]
    

    for i in range(len(x)):
        if(x[i] != 0):
            next.append(i)

    keys = [key for key in web]
   
    val = []

    for i in range(len(next)):
        val = list(list(web.values())[i])
        for i in range(len(val)):
            chance[list(web).index(val[i])] = 1 / len(val)
    
    print(x)
    print(chance)
    
    return distribution


#Fra opgave 4
W1 = {'p1': {'p3', 'p5'}, 'p2': {'p4', 'p5'}, 'p3': {'p1'}, 'p4': {'p1', 'p2', 'p5'}, 'p5': {}}
W2 = {'P1': {'P2'}, 'P2': {'P2'}, 'P3': {'P1'}, 'P4': {'P5'}, 'P5': {'P6'}, 'P6': {'P4'}}


print(surf_step(W2,1))