from warnsdorffs_functions import *


# Takes a square and if a tour is possible returns the visited squares in order,
# else returns False
def find_tour_from_square(square, n, m):
    edges = edge_list(n, m)
    square_list = [square]
    for i in range(n * m - 1):
        next_square = choose_next(find_next_squares(square, edges), edges, n, m)
        if next_square is False:
            return False
        else:
            edges = remove_edges(square, edges)
            square = next_square
        square_list.append(square)
    return square_list


# Prints the order the squares are visited in a tour in a board-like way
def print_tour(square_list, n, m):
    table = [['x'] * m for i in range(n)]
    for square in square_list:
        table[square[0]][square[1]] = square_list.index(square) + 1
    for row in table:
        print(row)
    return
