import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from opgave5 import make_web


def visualize_graph(web, node_size=700, font_size=10, arrowsize=20):
    
    # Input: netværk som dictionary
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

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=node_size, font_size=font_size, font_weight='bold', arrowsize=arrowsize)
    #nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold', arrowsize=20)

    plt.title("Netværk visualiseret som graf")
    plt.axis('off')
    # Output: Netværk visualiseret som graf
    plt.show()

    

if __name__ == "__main__":
    # Test med et eksempel
    # Opret et web med 10 noder og maksimalt 4 links pr. node
    # og minimum 0 links pr. node
    W = make_web(10, 4)
    visualize_graph(W)

