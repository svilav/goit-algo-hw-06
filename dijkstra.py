import heapq

import matplotlib.pyplot as plt
import networkx as nx


def main():
    g = nx.Graph()

    stations = ['Майдан Незалежності', 'Хрещатик', 'Арсенальна', 'Університет', 'Вокзальна', 'Політехнічний інститут',
                'Шулявська', 'Театральна', 'Золоті ворота', 'Палац спорту', 'Льва Толстого', 'Олімпійська',
                'Площа Льва Толстого', 'Палац Україна', 'Либідська']

    g.add_nodes_from(stations)

    routes = [
        ('Майдан Незалежності', 'Хрещатик', 1),
        ('Хрещатик', 'Арсенальна', 2),
        ('Майдан Незалежності', 'Театральна', 1),
        ('Театральна', 'Золоті ворота', 1),
        ('Золоті ворота', 'Університет', 1),
        ('Університет', 'Вокзальна', 2),
        ('Вокзальна', 'Політехнічний інститут', 1),
        ('Політехнічний інститут', 'Шулявська', 1),
        ('Театральна', 'Палац спорту', 1),
        ('Палац спорту', 'Льва Толстого', 1),
        ('Льва Толстого', 'Олімпійська', 2),
        ('Олімпійська', 'Палац Україна', 1),
        ('Палац Україна', 'Либідська', 2)

    ]

    g.add_weighted_edges_from(routes)
    # Візуалізація графа
    pos = nx.spring_layout(g)  # Позиціонування вузлів
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw(g, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10,
            font_weight='bold')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    plt.title("Транспортна мережа Києва з вагами")
    plt.show()

    shortest_paths = dijkstra_all_pairs_shortest_paths(g)

    print("Найкоротші шляхи між усіма вершинами:")
    for start_node, paths in shortest_paths.items():
        for end_node, (distance, path) in paths.items():
            print(f"{start_node} -> {end_node}: {path} (відстань: {distance})")


def dijkstra(graph, start):
    shortest_paths = {node: (float('inf'), []) for node in graph.nodes}
    shortest_paths[start] = (0, [start])
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > shortest_paths[current_node][0]:
            continue
        for neighbor, attributes in graph[current_node].items():
            weight = attributes['weight']
            distance = current_distance + weight
            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, shortest_paths[current_node][1] + [neighbor])
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths


def dijkstra_all_pairs_shortest_paths(graph):
    all_shortest_paths = {}
    for node in graph.nodes:
        all_shortest_paths[node] = dijkstra(graph, node)

    return all_shortest_paths


if __name__ == '__main__':
    main()
