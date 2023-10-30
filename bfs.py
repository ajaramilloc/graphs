def bfs(graph, init_vertex):
    visited = []
    queue = [init_vertex]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            neighbors = graph[vertex]

            for neighbor in neighbors:
                queue.append(neighbor)

    return visited    


def bfs_shortest_path(graph, start, goal):
    
    visited = []
    queue = [[start]]
    
    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        if vertex not in visited:
            neighbors = graph[vertex]
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    return new_path
                
            visited.append(vertex)
            
    return "Path does not exist"

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

print(bfs(graph, 0))
print(bfs_shortest_path(graph, 0, 7))
