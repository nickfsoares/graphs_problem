import sys, os, time
import networkx as nx
import random


def number_of_non_visited_neighbors(g, node, visited):
    if node in visited:
        return -float('inf')
    score = 0
    neighbor_score = 0
    for neighbor in nx.neighbors(g, node):
        if neighbor not in visited:
            score += 1
        for neighbor_neighbor in nx.neighbors(g, neighbor):
            if neighbor_neighbor not in visited:
                neighbor_score += 1
        
    final_score = score - 0.005 * neighbor_score
    final_score += 0.0125 * final_score * (random.random() - 0.5)
    return final_score

def dominate():
    ans = nx.Graph()
    visited = set()
    nodes = [n for n in g]

    while nodes:
        nodes.sort(key=lambda n: number_of_non_visited_neighbors(g, n, visited))
        if len(nodes) >= 3:
            node = random.choice(nodes[-3:])
            nodes.remove(node)
        else:
            node = nodes.pop()
        if node not in visited:
            ans.add_node(node)
            visited.add(node)
            for neighbor in nx.neighbors(g, node):
                visited.add(neighbor)
    return ans

def dominant(g):
    """
        A Faire:         
        - Ecrire une fonction qui retourne le dominant du graphe non dirigé g passé en parametre.
        - cette fonction doit retourner la liste des noeuds d'un petit dominant de g

        :param g: le graphe est donné dans le format networkx : https://networkx.github.io/documentation/stable/reference/classes/graph.html

    """
    cache = dict()
    for node in g:
        cache[node] = sum(1 for _ in nx.neighbors(g, node))

    best = None
    best_len = float('inf')
    for _ in range(75):
        dominated = dominate()
        len_dominated = len([n for n in dominated])
        if len_dominated < best_len:
            best_len = len_dominated
            best = dominated
    return best

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

    # input_dir = os.path.abspath("test")
    # output_dir = os.path.abspath("output")



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
