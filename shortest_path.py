import networkx as nx
import matplotlib.pyplot as plt

# g = nx.Graph()
# g.add_edge(131, 673, weight=673)
# g.add_edge(131, 201, weight=201)
# g.add_edge(673, 96, weight=96)
# g.add_edge(201, 96, weight=96)
# nx.draw(g, with_labels=True)#, with_weight=True)
# print(nx.shortest_path(g,source=131,target=96, weight='weight'))

DG = nx.DiGraph()
DG.add_weighted_edges_from([((0,1), 673, 673), ((0,1), 201, 201), (673, 96, 96), (201, 96, 96)])
# DG.add_edge((0,1), 96, weight = 96)

print(nx.shortest_path(DG,source=(0,1),target=96, weight='weight'))
print(nx.shortest_path_length(DG,source=(0,1),target=96, weight='weight'))

plt.show()
