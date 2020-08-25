# Finds which squares it is possible to visit next
def next_square(square, n, m):
    i = square[0]
    j = square[1]
    squares = []
    if (i + 1 < n) & (j + 2 < m):
        squares.append((i + 1, j + 2))
    if (i + 2 < n) & (j + 1 < m):
        squares.append((i + 2, j + 1))
    if (i + 2 < n) & (j - 1 >= 0):
        squares.append((i + 2, j - 1))
    if (i - 2 >= 0) & (j + 1 < m):
        squares.append((i - 2, j + 1))
    if (i - 2 >= 0) & (j - 1 >= 0):
        squares.append((i - 2, j - 1))
    if (i + 1 < n) & (j - 2 >= 0):
        squares.append((i + 1, j - 2))
    if (i - 1 >= 0) & (j + 2 < m):
        squares.append((i - 1, j + 2))
    if (i - 1 >= 0) & (j - 2 >= 0):
        squares.append((i - 1, j - 2))
    return squares


# Recursively searches for a complete tour from a given square
def find_route(square, visited, n, m):
    if len(visited) == n * m:
        return True
    for next in next_square(square, n, m):
        if next not in visited:
            if find_route(next, visited + [next], n, m):
                return True
    return False


# Checks if a tour is possible from any square of an nxm board
def is_tour(n, m):
    for i in range(n):
        for j in range(m):
            square = (i, j)
            visited = [square]
            if find_route(square, visited, n, m):
                return True
    return False
