"""N-Queens problem solver using Depth-First Search (DFS) algorithm."""
def dfs_n_queens(n: int):
    """Function to solve the N-Queens problem using DFS."""
    if n < 1:
        return []

    solutions = []
    placement = []  # placement[row] = col

    def dfs(row, cols, diag1, diag2):
        # row: next row to place a queen
        if row == n:
            solutions.append(placement.copy())
            return

        for col in range(n):
            d1 = row - col      # main diagonal id
            d2 = row + col      # anti-diagonal id

            if col in cols or d1 in diag1 or d2 in diag2:
                continue

            placement.append(col)
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)

            dfs(row + 1, cols, diag1, diag2)

            placement.pop()
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)

    dfs(0, set(), set(), set())
    return solutions

print(dfs_n_queens(1))
print(dfs_n_queens(2))
print(dfs_n_queens(3))
print(dfs_n_queens(4))
print(dfs_n_queens(5))
print(len(dfs_n_queens(5)))
print(len(dfs_n_queens(8)))
