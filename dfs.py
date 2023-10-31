def dfs(graph, source):
    visited = [source]
    stack = [source]

    while stack:
        vertex = stack.pop()
        neighbors = graph[vertex]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs(graph, 'A'))