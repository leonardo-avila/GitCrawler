import csv
import networkx as nx

G = nx.read_edgelist('crawlerGetRepos', delimiter=',', nodetype=str)
#print(G.edges())
with open('crawlerConections.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',',lineterminator='\n')
    for node in G.nodes():
        writeit.writerow([str(node)] + [G.degree(node)])
with open('graphEdges.csv', 'w') as e:
    writeit = csv.writer(e, delimiter=',',lineterminator='\n')
    for edge in G.edges():
        writeit.writerow(edge)
with open('graphNodes.csv', 'w') as n:
    writeit = csv.writer(n, delimiter=',',lineterminator='\n')
    for node in G.nodes():
        writeit.writerow([node])

print("Média do grau dos nodos do grafo: " + str(nx.average_degree_connectivity(G)))
print("Média de Clustering do Grafo: " + str(nx.average_clustering(G)))
print("Distância média dos nodos: " + str(nx.average_shortest_path_length(G)))
print("Betweeness das arestas: " + str(nx.edge_betweenness(G)))
print("Betweeness dos nodos:" + str(nx.betweenness_centrality((G))))
