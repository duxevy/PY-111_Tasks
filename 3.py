"""
Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
"""

import networkx as nx

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
G.add_edges_from([(1, 2), (2, 3), (1, 3), (1, 4), (5, 6), (5, 7), (5, 8)])

list_of_comp = list(nx.connected_components(G))
print(list_of_comp)
print(len(list_of_comp))

print(G.number_of_nodes())
print(G.number_of_edges())
