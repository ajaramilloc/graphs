def dfs(graph, init_vertex):
    visited = []
    stack = [init_vertex]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.append(vertex)
            neighbors = graph[vertex]

            for neighbor in neighbors:
                stack.append(neighbor)

    return visited   


graph = {
    0: [1, 2],
    1: [0, 2, 3, 4],
    2: [0, 1],
    3: [1, 5],
    4: [1],
    5: [3, 6, 7, 8],
    6: [5],
    7: [5, 8],
    8: [5, 7, 9],
    9: [8]
}

print(dfs(graph, 0))
