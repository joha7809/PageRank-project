import networkx as nx
import matplotlib.pyplot as plt
#from opgave5 import make_web

def visualize_graph(web):
    
    # Input: netværk som dictionary
    nodes = [key for key in web.keys()]
    edges = [(key, target) for key in web.keys() for target in web[key]]
    print("Nodes:", nodes)
    print("Edges:", edges)
    # Opret en graf
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Tegn grafen
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold', arrowsize=20)
    plt.title("Netværk visualiseret som graf")
    plt.axis('off')
    # Output: Netværk visualiseret som graf
    plt.show()

    


#Generate a random web with 10 nodes and 3 links per node
W = {'P1': {'P2', 'P3'}, 'P2': {'P3'}, 'P3': {'tis'}}

visualize_graph(W)