def dfs_path_length(graph, start_node, end_node, visited=None, path=None):
    if start_node not in graph:
        raise ValueError(f"Начальная вершина {start_node} не найдена в графе.")
    if end_node not in graph:
        raise ValueError(f"Конечная вершина {end_node} не найдена в графе.")


    if visited is None:
        visited = set()
    if path is None:
        path = [start_node]

    visited.add(start_node)

    if start_node == end_node:
        return len(path) -1  
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            new_path = path + [neighbor]
            result = dfs_path_length(graph, neighbor, end_node, visited, new_path)
            if result is not None:
                return result

    return None  

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

    start_node = 2
    end_node = 5  
    try:
        path_length = dfs_path_length(graph, start_node, end_node)
        print(f"Длина пути от вершины {start_node} до вершины {end_node}: {path_length}")
    except ValueError as e:
        print(f"Ошибка: {e}")