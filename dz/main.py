from collections import deque


def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])  # Очередь с парами (элемент, расстояние до него)

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance

        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append((neighbor, distance + 1))

    return None


# Пример графа в виде словаря смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A', 'F'))
print(bfs(graph, 'A', 'D'))
print(bfs(graph, 'A', 'G'))