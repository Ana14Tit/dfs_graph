def dfs_path_length(graph, start_node, end_node, visited=None, path=None):
    """
    Реализация обхода графа в глубину и поиск длины пути от start_node до end_node.
    Обрабатывает исключения для некорректных входных данных.

    Сложность по времени: O(V + E), где V - количество вершин, E - количество ребер.
    Сложность по памяти: O(V), где V - количество вершин (для стека рекурсии и множества visited).

    Args:
        graph: Словарь, представляющий граф. Ключи - вершины, значения - список смежных вершин.
        start_node: Начальная вершина.
        end_node: Конечная вершина.
        visited: Множество посещенных вершин (для предотвращения циклов).
        path: Текущий путь (используется для рекурсивного отслеживания пути).

    Returns:
        Длина пути от start_node до end_node (или None, если путь не найден).

    Raises:
        ValueError: Если start_node или end_node не найдены в графе.
    """
    # Проверяем, существуют ли начальная и конечная вершины в графе.
    if start_node not in graph:
        raise ValueError(f"Начальная вершина {start_node} не найдена в графе.")
    if end_node not in graph:
        raise ValueError(f"Конечная вершина {end_node} не найдена в графе.")

    # Инициализируем множество посещенных вершин и текущий путь, если они не были переданы.
    if visited is None:
        visited = set()
    if path is None:
        path = [start_node]

    # Добавляем текущую вершину в множество посещенных.
    visited.add(start_node)

    # Если текущая вершина является конечной, возвращаем длину пути (минус 1, чтобы не учитывать начальную вершину).
    if start_node == end_node:
        return len(path) - 1

    # Перебираем всех соседей текущей вершины.
    for neighbor in graph[start_node]:
        # Если сосед не был посещен, рекурсивно вызываем dfs_path_length для соседа.
        if neighbor not in visited:
            # Создаем новый путь, добавляя соседа к текущему пути.
            new_path = path + [neighbor]
            # Рекурсивно ищем путь от соседа до конечной вершины.
            result = dfs_path_length(graph, neighbor, end_node, visited, new_path)
            # Если путь найден, возвращаем его длину.
            if result is not None:
                return result

    # Если путь не найден, возвращаем None.
    return None

if __name__ == '__main__':
    # Пример использования
    edges = [(4, 2), (1, 3), (2, 4)]  # Список ребер графа
    graph = {}  # Словарь для представления графа
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Граф неориентированный

    start_node = 2
    end_node = 5  # Некорректная вершина (нет в графе)
    try:
        path_length = dfs_path_length(graph, start_node, end_node)
        print(f"Длина пути от вершины {start_node} до вершины {end_node}: {path_length}")
    except ValueError as e:
        # Обрабатываем исключение, если начальная или конечная вершина не найдена.
        print(f"Ошибка: {e}")