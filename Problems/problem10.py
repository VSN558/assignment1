# Problem 3: Implement a breadth-first search algorithm

from collections import deque

def bfs(graph, start, end):
    """
    Finds the shortest path between two nodes in an unweighted graph using breadth-first search.

    Args:
    - graph (dict): a dictionary representing the graph
    - start (str): the starting node
    - end (str): the ending node

    Returns:
    - path (list): a list of nodes representing the shortest path between the start and end nodes
    """
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


path = bfs(graph, 'A', 'F')

if path:
    print(f"The shortest path from A to F is: {' -> '.join(path)}")
else:
    print("There is no path from A to F.")
