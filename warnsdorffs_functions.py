# Finds all possible moves on an nxm board
def edge_list(n, m):
    edges = []
    for i in range(n):
        for j in range(m):
            if (i + 1 < n) & (j + 2 < m):
                edges.append(((i, j), (i + 1, j + 2)))
            if (i + 2 < n) & (j + 1 < m):
                edges.append(((i, j), (i + 2, j + 1)))
            if (i + 2 < n) & (j - 1 >= 0):
                edges.append(((i, j), (i + 2, j - 1)))
            if (i - 2 >= 0) & (j + 1 < m):
                edges.append(((i, j), (i - 2, j + 1)))
            if (i - 2 >= 0) & (j - 1 >= 0):
                edges.append(((i, j), (i - 2, j - 1)))
            if (i + 1 < n) & (j - 2 >= 0):
                edges.append(((i, j), (i + 1, j - 2)))
            if (i - 1 >= 0) & (j + 2 < m):
                edges.append(((i, j), (i - 1, j + 2)))
            if (i - 1 >= 0) & (j - 2 >= 0):
                edges.append(((i, j), (i - 1, j - 2)))
    return edges


# Finds the next possible square to visit from a square
def find_next_squares(square, edges):
    available = []
    for edge in edges:
        if edge[0] == square:
            available.append(edge[1])
    return available


# Finds the number of available moves from a square
def find_deg(square, edges):
    deg = 0
    for edge in edges:
        if square == edge[0]:
            deg += 1
    return deg


# Chooses the square amongst the available squares with the lowest
# degree to be the next square visited
def choose_next(available, edges, n, m):
    low_deg = 63
    next_square = False
    for possible in available:
        if find_deg(possible, edges) < low_deg:
            low_deg = find_deg(possible, edges)
            next_square = possible
        elif find_deg(possible, edges) == low_deg:
            curr_dist = min(next_square[0] + 1, n - 1 - next_square[0]) + \
                        min(next_square[1] + 1, m - 1 - next_square[1])
            new_dist = min(possible[0] + 1, n - 1 - possible[0]) + \
                       min(possible[1] + 1, m - 1 - possible[1])
            if curr_dist > new_dist:
                next_square = possible
    return next_square


# Removes all moves involving a visited square from the list of
# available moves
def remove_edges(square, edges):
    keep_edges = []
    for edge in edges:
        if square not in [edge[0], edge[1]]:
            keep_edges.append(edge)
    return keep_edges
