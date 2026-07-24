# ml/tsp_solver.py
import networkx as nx
from geopy.distance import geodesic

def calcular_distancia(p1, p2):
    return geodesic(p1, p2).kilometers

def resolver_tsp(locations):
    G = nx.complete_graph(len(locations))
    for i in G.nodes:
        for j in G.nodes:
            if i != j:
                dist = calcular_distancia(locations[i], locations[j])
                G[i][j]['weight'] = dist
    return nx.approximation.traveling_salesman_problem(G, weight="weight", cycle=True)
