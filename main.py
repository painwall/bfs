# 2. Реализовать поиск кратчайшего пути между парой заданных вершин на неориентированном связном графе.
# 3. Ответить на вопросы:
# Что является входом для алгоритма поиска кратчайшего пути на неориентированном связном графе, что – результатом работы?
# Какова его вычислительная сложность?
# Переносится ли поиск кратчайшего пути (и поиск в ширину) на ориентированные графы?



from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

# Пример графа в виде словаря, где ключи - вершины, а значения - их соседи
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Начинаем обход с вершины 'A'
print("Результат обхода в ширину:")
bfs(graph, 'A')


from collections import deque

def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()
        for neighbor in graph[vertex] - set(path):
            if neighbor == end:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None

# Пример графа в виде словаря
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Начальная и конечная вершины для поиска кратчайшего пути
start_vertex = 'A'
end_vertex = 'F'

shortest_path = bfs_shortest_path(graph, start_vertex, end_vertex)

if shortest_path:
    print(f"Кратчайший путь от {start_vertex} до {end_vertex}: {shortest_path}")
else:
    print(f"Пути от {start_vertex} до {end_vertex} не существует.")