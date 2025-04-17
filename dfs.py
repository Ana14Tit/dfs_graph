def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    path = [start_node]

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            path.extend(dfs(graph, neighbor, visited))
            break 
    return path


if __name__ == '__main__':
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  
    print(f"Graph representation: {graph}")
    start_node = 1
    path = dfs(graph, start_node)
    print(f"DFS обход из вершины {start_node}: {path}")