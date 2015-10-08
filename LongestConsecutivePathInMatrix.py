__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-length-of-the-longest-consecutive-path-in-a-character-matrix/
# Find length of the longest consecutive path from a given starting character
# Given a matrix of characters. Find length of the longest path from a given character,
# such that all characters in the path are consecutive to each other,
# i.e., every character in path is next to previous in alphabetical order.
# It is allowed to move in all 8 directions from a cell.


def search(cache, mat, m, n, i, j):
    if (i, j) in cache:
        return cache[(i, j)]

    current_value = mat[i][j]
    next_value = current_value + 1

    paths = []
    if i > 0:
        if j > 0 and mat[i - 1][j - 1] == next_value:
            paths.append(search(cache, mat, m, n, i - 1, j - 1))

        if mat[i - 1][j] == next_value:
            paths.append(search(cache, mat, m, n, i - 1, j))

        if j < n - 1 and mat[i - 1][j + 1] == next_value:
            paths.append(search(cache, mat, m, n, i - 1, j + 1))

    if j > 0 and mat[i][j - 1] == next_value:
        paths.append(search(cache, mat, m, n, i, j - 1))

    if j < n - 1 and mat[i][j + 1] == next_value:
        paths.append(search(cache, mat, m, n, i, j + 1))

    if i < m - 1:
        if j > 0 and mat[i + 1][j - 1] == next_value:
            paths.append(search(cache, mat, m, n, i + 1, j - 1))

        if mat[i + 1][j] == next_value:
            paths.append(search(cache, mat, m, n, i + 1, j))

        if j < n - 1 and mat[i + 1][j + 1] == next_value:
            paths.append(search(cache, mat, m, n, i + 1, j + 1))

    max_len = 0
    max_path = []

    for p in paths:
        if len(p) > max_len:
            max_path = p
            max_len = len(p)

    total_path = [current_value] + max_path
    cache[(i, j)] = total_path
    return total_path


def longest_consecutive_path(mat):
    if mat is None or len(mat) == 0 or len(mat[0]) == 0:
        return None

    cache = {}
    m = len(mat)
    n = len(mat[0])

    max_path = []
    max_len = 0
    for i in range(m):
        for j in range(n):
            path = search(cache, mat, m, n, i, j)
            length = len(path)
            if length > max_len:
                max_path = path
                max_len = length

    return max_path

matrix = [
    [6, 5, 3, 1, 2, 7],
    [9, 4, 2, 7, 8, 0],
    [5, 6, 7, 8, 9, 8]
]

print longest_consecutive_path(matrix)
