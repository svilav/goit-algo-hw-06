import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (станцій)
stations = ['Майдан Незалежності', 'Хрещатик', 'Арсенальна', 'Університет', 'Вокзальна', 'Політехнічний інститут',
            'Шулявська', 'Театральна', 'Золоті ворота', 'Палац спорту', 'Льва Толстого', 'Олімпійська',
            'Площа Льва Толстого', 'Палац Україна', 'Либідська']
G.add_nodes_from(stations)

# Додавання ребер (доріг або маршрутів між станціями)
routes = [
    ('Майдан Незалежності', 'Хрещатик'),
    ('Хрещатик', 'Арсенальна'),
    ('Майдан Незалежності', 'Театральна'),
    ('Театральна', 'Золоті ворота'),
    ('Золоті ворота', 'Університет'),
    ('Університет', 'Вокзальна'),
    ('Вокзальна', 'Політехнічний інститут'),
    ('Політехнічний інститут', 'Шулявська'),
    ('Театральна', 'Палац спорту'),
    ('Палац спорту', 'Льва Толстого'),
    ('Льва Толстого', 'Олімпійська'),
    ('Олімпійська', 'Палац Україна'),
    ('Палац Україна', 'Либідська')
]
G.add_edges_from(routes)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиціонування вузлів
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10,
        font_weight='bold')
plt.title("Транспортна мережа Києва")
plt.show()


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Знаходження шляхів за допомогою DFS
dfs_paths = list(dfs_path(G, 'Майдан Незалежності', 'Либідська'))
print("Шляхи за допомогою DFS:")
for path in dfs_paths:
    print(path)

# Знаходження шляхів за допомогою BFS
bfs_paths = list(bfs_path(G, 'Майдан Незалежності', 'Либідська'))
print("Шляхи за допомогою BFS:")
for path in bfs_paths:
    print(path)
