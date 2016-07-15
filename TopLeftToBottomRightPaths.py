__author__ = 'Danylo'


# http://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
# Count all possible paths from top left to bottom right of a mXn matrix
# The problem is to count all the possible paths from top left to bottom right of a mXn matrix
# with the constraints that from each cell you can either move only to right or down.


# http://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/
# Print all possible paths from top left to bottom right of a mXn matrix
# The problem is to print all the possible paths from top left to bottom right of a mXn matrix
# with the constraints that from each cell you can either move only to right or down.


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def paths_formula(m, n):
    return factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1))


def paths_dynamic(m, n):
    cache = [[0 for x in range(n)] for x in range(m)]

    for i in range(0, m):
        cache[i][0] = 1

    for i in range(0, n):
        cache[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    return cache[m - 1][n - 1]


def print_paths_help(m, n, i, j, path):
    if i == m - 1:
        print(path + ['R' for x in range(j, n - 1)])
        return
    elif j == n - 1:
        print(path + ['D' for x in range(i, m - 1)])
        return

    path.append('D')
    print_paths_help(m, n, i + 1, j, path)
    del path[-1]

    path.append('R')
    print_paths_help(m, n, i, j + 1, path)
    del path[-1]


def print_paths(m, n):
    return print_paths_help(m, n, 0, 0, [])


M = 5
N = 5
for i in range(M, M + 1):
    for j in range(N, N + 1):
        print(paths_formula(i, j))
        print(paths_dynamic(i, j))

print_paths(M, N)
