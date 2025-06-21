# Parte 1: Librerías
import networkx as nx
import matplotlib.pyplot as plt

# Parte 2: Lista de nodos y aristas del grafo
vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 1),
    ('C', 'D', 4),
    ('C', 'E', 5),
    ('D', 'E', 1)
]

# Parte 3: Estructura Union-Find
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

# Parte 4: Algoritmo de Kruskal
def kruskal(graph_edges, vertices, reverse=False):
    uf = UnionFind(vertices)
    mst = []
    sorted_edges = sorted(graph_edges, key=lambda x: x[2], reverse=reverse)
    for u, v, w in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, w))
        if len(mst) == len(vertices) - 1:
            break
    return mst

# Parte 5: Ejecución de Kruskal para mínimo y máximo costo
mst_min = kruskal(edges, vertices, reverse=False)
mst_max = kruskal(edges, vertices, reverse=True)

# Parte 6: Función para graficar
def draw_kruskal_mst(vertices, edges, mst_edges, title):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in mst_edges],
                           width=4, edge_color='red')
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Parte 7: Mostrar gráficas
draw_kruskal_mst(vertices, edges, mst_min, "Árbol de Expansión Mínimo con Kruskal")
draw_kruskal_mst(vertices, edges, mst_max, "Árbol de Expansión Máximo con Kruskal")
