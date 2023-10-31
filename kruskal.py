def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)

    return parent[node]

def union(node1, node2, parent):
    root1 = find(node1, parent)
    root2 = find(node2, parent)

    if root1 != root2:
        parent[root2] = root1

def kruskal(edges, num_v):
    parent = {node: node for node in range(num_v)}
    mst_cost = 0
    mst = []
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        u, v, w = edge

        if find(u, parent) != find(v, parent):
            mst_cost += w
            mst.append(edge)
            union(u, v, parent)

    return mst_cost, mst

edges = [(0, 1, 1), (1, 2, 2), (2, 3, 1),(3, 4, 3), (4, 0, 1), (5, 6, 5)]

print(kruskal(edges, 7))