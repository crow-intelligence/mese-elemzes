import networkx as nx
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.neighbors import kneighbors_graph

from src.utils.svd_algebra import SVDAlgebra

a = SVDAlgebra("data/lm/")

A = kneighbors_graph(a.U, 5, mode="connectivity", include_self=False)
m = A.toarray()

G = nx.Graph()
edges = {}

for i in range(len(a.U)):
    wd_embedding = a.U[i]
    lst = list(m[i])
    indices = [j for j in range(len(lst)) if lst[j] > 0]
    weights = [1-float(cosine(wd_embedding, a.U[k])) for k in indices]
    connected_wds = [a.vocabulary[j] for j in indices]
    G.add_node(i, label=a.vocabulary[i])

    keys = list(zip([i] * len(indices), indices))
    keys = [tuple(sorted(k)) for k in keys]
    d = dict(zip(keys, weights))
    for k, v in d.items():
        if k in edges:
            edges[k] = (edges[k] + v) / 2.0
        else:
            edges[k] = v

for k, v in edges.items():
    if v > 0.3:
        G.add_edge(k[0], k[1], weight=float(v))

nx.write_graphml(G, "data/graphs/full_graph.graphml")
