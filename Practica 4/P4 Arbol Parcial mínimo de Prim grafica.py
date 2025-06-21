# Importamos las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Definimos el grafo como un diccionario de adyacencias
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 5},
    'D': {'B': 1, 'C': 4, 'E': 1},
    'E': {'C': 5, 'D': 1}
}


# Algoritmo de Prim para encontrar el Árbol de Expansión Mínimo
def prim(graph, start):
    visited = set()  # Para saber qué nodos ya se visitaron
    mst = []  # Lista donde guardamos las aristas del MST
    edges = [(0, start, None)]  # Cola de prioridad: (peso, nodo_actual, nodo_anterior)

    print("Paso a paso del algoritmo de Prim:\n")
    while edges:
        weight, current, previous = heapq.heappop(edges)  # Tomamos la arista de menor peso
        if current in visited:
            continue
        visited.add(current)

        # Si no es el nodo de inicio, agregamos la arista al MST
        if previous is not None:
            mst.append((previous, current, weight))
            print(f"Agregado: {previous} --({weight})--> {current}")

        # Revisamos los vecinos y agregamos las aristas a la cola si no han sido visitados
        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(edges, (cost, neighbor, current))

    return mst


# Función para graficar el MST
def draw_prim_mst(graph, mst_result):
    G = nx.Graph()

    # Agregamos todas las aristas del grafo original
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    # Posiciones fijas para los nodos
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Dibujamos nodos, etiquetas y aristas
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Resaltamos las aristas del MST en rojo
    mst_edges = [(u, v) for u, v, w in mst_result]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=4, edge_color='red')

    plt.title("Árbol de Expansión Mínimo usando Prim")
    plt.axis('off')
    plt.tight_layout()
    plt.show()


# Ejecutamos el algoritmo y mostramos resultados
start_node = 'A'
mst_result = prim(graph, start_node)

print("\nResumen del Árbol de Expansión Mínimo:")
for u, v, w in mst_result:
    print(f"{u} -- {w} --> {v}")

# Mostramos la gráfica
draw_prim_mst(graph, mst_result)
