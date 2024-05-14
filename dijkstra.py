import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (станцій)
stations = ['Майдан Незалежності', 'Хрещатик', 'Арсенальна', 'Університет', 'Вокзальна', 'Політехнічний інститут',
            'Шулявська', 'Театральна', 'Золоті ворота', 'Палац спорту', 'Льва Толстого', 'Олімпійська',
            'Площа Льва Толстого', 'Палац Україна', 'Либідська']
G.add_nodes_from(stations)

# Додавання ребер з вагами (доріг або маршрутів між станціями)
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
G.add_weighted_edges_from(routes)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиціонування вузлів
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа Києва з вагами")
plt.show()

# Функція для знаходження найкоротшого шляху за допомогою алгоритму Дейкстри
def dijkstra_all_pairs_shortest_paths(graph):
    return dict(nx.all_pairs_dijkstra_path(graph))

# Знаходження найкоротших шляхів між усіма вершинами
shortest_paths = dijkstra_all_pairs_shortest_paths(G)

# Виведення найкоротших шляхів
print("Найкоротші шляхи між усіма вершинами:")
for start_node, paths in shortest_paths.items():
    for end_node, path in paths.items():
        print(f"{start_node} -> {end_node}: {path}")