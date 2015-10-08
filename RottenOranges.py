__author__ = 'Danylo'


# http://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
# Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2
# which has the following meaning:
# 0: Empty cell
# 1: Cells have fresh oranges
# 2: Cells have rotten oranges

# So we have to determine what is the minimum time required so that all the oranges become rotten.
# A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1]
# (up, down, left and right). If it is impossible to rot every orange then simply return -1.


def time_to_rotten_oranges(matrix):
    empty = 0
    fresh = 1
    rotten = 2

    if matrix is None:
        return None

    m = len(matrix)
    if m == 0:
        return -1

    n = len(matrix[0])
    if n == 0:
        return -1

    # Initialize the queue with all rotten tomatoes.
    queue = []
    for i in range(0, m):
        for j in range(0, n):
            cell = matrix[i][j]
            if cell == rotten:
                queue.append((i, j, 0))

    time = 0
    while len(queue) != 0:
        rotten = queue.pop(0)

        i = rotten[0]
        j = rotten[1]
        t = rotten[2]

        matrix[i][j] = rotten
        time = max(time, t)

        if i > 0 and matrix[i - 1][j] == fresh:
            matrix[i - 1][j] = rotten
            queue.append((i - 1, j, t + 1))

        if i < m - 1 and matrix[i + 1][j] == fresh:
            matrix[i + 1][j] = rotten
            queue.append((i + 1, j, t + 1))

        if j > 0 and matrix[i][j - 1] == fresh:
            matrix[i][j - 1] = rotten
            queue.append((i, j - 1, t + 1))

        if j < n - 1 and matrix[i][j + 1] == fresh:
            matrix[i][j + 1] = rotten
            queue.append((i, j + 1, t + 1))

    all_rotten = True
    for line in matrix:
        if all_rotten:
            for cell in line:
                if cell == fresh:
                    all_rotten = False
                    break

    if all_rotten:
        return time
    else:
        return -1


matrices = [
    [
        [2, 1, 0, 2, 1],
        [1, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ],
    [
        [2, 1, 0, 2, 1],
        [0, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ]
]

for mat in matrices:
    print time_to_rotten_oranges(mat)
