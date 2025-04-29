import matplotlib.pyplot as plt
import numpy as np
from opgave4 import W1,W2
import networkx as nx
from opgave24 import eigenvector_PageRank




def plot_ranking(web, ranking, d=0.85, node_size = 2500, arrow_size = 30):

    
    page_rank = [rank * node_size for rank in list(ranking.values())]
    arrow_size = [rank * arrow_size for rank in list(ranking.values())]
    nodes = [key for key in web.keys()]
    edges = [(key, target) for key in web.keys() for target in web[key]]
    print("Nodes:", nodes)
    print("Edges:", edges)
    # Opret en graf
    G = nx.DiGraph() #Intialiserer en rettet graf
    # Tilføj noder og kanter til grafen
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # Tegn grafen
    subax1 = plt.subplot(111)
    pos = nx.kamada_kawai_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=page_rank, font_size=10, font_weight='bold', arrowsize = arrow_size)
    #nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold', arrowsize=20)

    plt.title("Netværk visualiseret som graf")
    plt.axis('off')
    # Output: Netværk visualiseret som graf
    plt.show()

plot_ranking(W1,eigenvector_PageRank(W1,0.85),0.85)