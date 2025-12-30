"""Depth First Search (DFS) algorithm implementation."""
def dfs(matrix, start_node):
    """Function to perform Depth First Search on a graph"""
    # Number of nodes
    n = len(matrix)
    visited = [False] * n
    result = []

    def explore(node):
        visited[node] = True
        result.append(node)

        for neighbor in range(n - 1, -1, -1):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                explore(neighbor)

    explore(start_node)
    return result