import heapq

def dijkstra(graph, source):
    shortest_path = {node: float('inf') for node in graph}
    shortest_path[source] = 0

    priority_queue = [(source, 0)]

    while priority_queue:
        current_vertex, current_weight = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_weight + weight

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(priority_queue, (neighbor, distance))

    return shortest_path

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))
