import sys, os, time
import networkx as nx
from networkx.algorithms.shortest_paths import weighted
import dominant as dm 
import matplotlib.pyplot as plt 
import numpy as np

#G=nx.Graph()
# i=1
# G.add_node(range(1,10))
# G.add_edge(1,2,weight=0.5)
# G.add_edge(1,3,weight=9.8)
# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G,pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
# plt.show()

# a = np.reshape(np.random.random_integers(0,1,size=25),(5,5)) # random 5,5 numpy-array
# np.fill_diagonal(a,0)   # remove self-loops                                     
# print("np-array: \n" + str(a))

# PLOTTING GRAPHS
# D = nx.Graph(a)      # create undirectional graph from numpy array
# weighted_edges = dict(zip(D.edges(),np.random.randint(1,10,size=len(D.edges())))) # assign random weights to each edge
# edge_tuple_list =  [(key[0],key[1],value) for key,value in zip(weighted_edges.keys(),weighted_edges.values())] 
# D.add_weighted_edges_from(edge_tuple_list) #convert to list of edge tuples and add to the graph
# #plotting graph
# pos = nx.spring_layout(D) # <---this line is new.  the pos here replaces nx.spring_layout below.
# nx.draw(D, pos=pos, with_labels=True, node_size=700) #draw the graph
# nx.draw_networkx_edge_labels(D, pos=pos, edge_labels=nx.get_edge_attributes(D,'weight')) #add edge labels
# plt.show()

# FROM DOMINANT.PY
input_dir = os.path.abspath(sys.argv[1])
graph_filename = sorted(os.listdir(input_dir)).loc[0]
# importer le graphe
g = dm.load_graph(os.path.join(input_dir, graph_filename))
pos = nx.spring_layout(g) # <---this line is new.  the pos here replaces nx.spring_layout below.
nx.draw(g, pos=pos, with_labels=True, node_size=700) #draw the graph
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=nx.get_edge_attributes(g,'weight')) #add edge labels
plt.show()
def dominant_test(g):
    return g.nodes


# # creating an empty Graph 
# G = nx.Graph()
# #adding random nodes
# G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])
# print(G)
# pos = nx.kamada_kawai_layout(G)
# nx.draw(G, pos, with_labels = True)
# plt.show()
