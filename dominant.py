import sys, os, time
import networkx as nx
import numpy as np 

def treating_node(g,node_label): 
  new_node = g.nodes()[node_label]
  new_node['label'] = node_label
  new_node['neighbors'] = [neighbors for neighbors in g.neighbors(node_label)]
  return new_node


def dominant(g):
    """
        A Faire:         
        - Ecrire une fonction qui retourne le dominant du graphe non dirigé g passé en parametre.
        - cette fonction doit retourner la liste des noeuds d'un petit dominant de g

        :param g: le graphe est donné dans le format networkx : https://networkx.github.io/documentation/stable/reference/classes/graph.html

    """
    #removing self-loops
    g.remove_edges_from(nx.selfloop_edges(g))

    #selecting a random node 
    node_label = np.random.choice(g.nodes)
    label_dominant_nodes = set()
    neighbors_plus_nodes = set()
    while (set(g.nodes)!= neighbors_plus_nodes):
        new_node = treating_node(g,node_label)            #first we select a node randomly
        label_dominant_nodes.update([new_node['label']])  #we update the dominant
        neighbors_plus_nodes.update([new_node['label']])
        neighbors_plus_nodes.update(new_node['neighbors'])
        ######################checking neighbors########################
        maxScore = 0
        for n in new_node['neighbors']:
            neighbors = treating_node(g,n)
            neighbors['score'] = round(len(neighbors['neighbors'])/neighbors['weight'])
            if neighbors['score']>maxScore:
                maxScore = neighbors['score']
                #checking neighbors' neighbors 
            for nn in neighbors['neighbors']:
                neighbors_neighbors = treating_node(g,nn)
                neighbors_neighbors['score'] = round(len(neighbors_neighbors['neighbors'])/neighbors_neighbors['weight'],4)
                if neighbors_neighbors['score']>maxScore:
                    maxScore = neighbors_neighbors['score']
                    new_node = neighbors_neighbors          # chosing the best neighbor
            ################################################################

        if new_node['label'] in label_dominant_nodes:
            try:
                node_label = np.random.choice(list(g.nodes - neighbors_plus_nodes))
            except: pass
        else:                     # if node is not in the dominant 
            label_dominant_nodes.update([new_node['label']])  #we update the dominant
            neighbors_plus_nodes.update([new_node['label']])
            neighbors_plus_nodes.update(new_node['neighbors'])
            
    return list(label_dominant_nodes)  # pas terrible :) mais c'est un dominant


#########################################
#### Ne pas modifier le code suivant ####
#########################################


def load_graph(name):
    with open(name, "r") as f:
        state = 0
        G = None
        for l in f:
            if state == 0:  # Header nb of nodes
                state = 1
            elif state == 1:  # Nb of nodes
                nodes = int(l)
                state = 2
            elif state == 2:  # Header position
                i = 0
                state = 3
            elif state == 3:  # Position
                i += 1
                if i >= nodes:
                    state = 4
            elif state == 4:  # Header node weight
                i = 0
                state = 5
                G = nx.Graph()
            elif state == 5:  # Node weight
                G.add_node(i, weight=int(l))
                i += 1
                if i >= nodes:
                    state = 6
            elif state == 6:  # Header edge
                i = 0
                state = 7
            elif state == 7:
                if i > nodes:
                    pass
                else:
                    edges = l.strip().split(" ")
                    for j, w in enumerate(edges):
                        w = int(w)
                        if w == 1 and (not i == j):
                            G.add_edge(i, j)
                    i += 1

        return G

#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__ == "__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])

    # un repertoire des graphes en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
        print(input_dir, "doesn't exist")
        exit()

    # un repertoire pour enregistrer les dominants doit être passé en parametre 2
    if not os.path.isdir(output_dir):
        print(input_dir, "doesn't exist")
        exit()

        # fichier des reponses depose dans le output_dir et annote par date/heure
    output_filename = 'answers_{}.txt'.format(time.strftime("%d%b%Y_%H%M%S", time.localtime()))
    output_file = open(os.path.join(output_dir, output_filename), 'w')

    for graph_filename in sorted(os.listdir(input_dir)):
        # importer le graphe
        g = load_graph(os.path.join(input_dir, graph_filename))

        # calcul du dominant
        D = sorted(dominant(g), key=lambda x: int(x))

        # ajout au rapport
        output_file.write(graph_filename)
        for node in D:
            output_file.write(' {}'.format(node))
        output_file.write('\n')

    output_file.close()
