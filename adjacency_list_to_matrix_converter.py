"""Convert adjacency list to adjacency matrix."""
def adjacency_list_to_matrix(adj_list):
    """Function to convert an adjacency list to an adjacency matrix."""
    # Number of nodes
    n = len(adj_list)

    # Initialize n x n matrix with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the matrix based on adjacency list
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print each row
    for row in matrix:
        print(row)

    return matrix

adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
