# Importamos las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Creamos el grafo como diccionario de adyacencias con pesos
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

# Algoritmo de Dijkstra para calcular distancias más cortas desde un nodo
def dijkstra(graph, start):
    # Inicializamos distancias a infinito
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Distancia del nodo origen a sí mismo es 0
    priority_queue = [(0, start)]  # Cola de prioridad para visitar nodos

    # Diccionario para guardar caminos anteriores (para reconstruir la ruta)
    previous_nodes = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Función para reconstruir la ruta desde el nodo origen hasta uno de destino
def get_path(previous_nodes, target):
    path = []
    while target is not None:
        path.insert(0, target)  # Insertamos al inicio
        target = previous_nodes[target]
    return path

# Visualización del grafo
def draw_graph(graph, shortest_paths, start):
    G = nx.Graph()

    # Agregar nodos y aristas al grafo
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)  # Posiciones de los nodos para el dibujo

    # Dibujamos el grafo básico con pesos
    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Coloreamos el camino más corto desde el nodo de inicio hacia todos los demás
    for target in graph:
        if target == start:
            continue
        path = get_path(shortest_paths[1], target)
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, width=4, edge_color='red')

    plt.title(f"Camino más corto desde '{start}' a todos los nodos")
    plt.axis('off')
    plt.show()

# Nodo de inicio
start_node = 'A'

# Ejecutamos el algoritmo de Dijkstra
distances, previous_nodes = dijkstra(graph, start_node)

# Mostramos en consola las distancias
print(f"Distancias más cortas desde el nodo {start_node}:")
for node in distances:
    print(f"Distancia a {node}: {distances[node]}")

# Dibujamos el grafo con las rutas más cortas
draw_graph(graph, (distances, previous_nodes), start_node)
