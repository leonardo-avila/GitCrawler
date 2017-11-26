import csv
import networkx as nx

G = nx.read_edgelist('crawlerGetRepos', delimiter=',', nodetype=int)
#print(G.edges())
with open('degrees.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')
    for node in G.nodes():
        writeit.writerow([str(node)] + [G.degree(node)])
