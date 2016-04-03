__author__ = 'Danylo'


# Find equilibrium index in array.
# It is the index i where sum till i from 0th index = sum from ith index to last index


def equilibrium_index(array):
    if array is None:
        raise Exception("Array is None")

    n = len(array)
    left_sums = [x for x in array]
    right_sums = [x for x in array]

    for i in range(1, n):
        left_sums[i] += left_sums[i - 1]
        right_sums[n - i - 1] += right_sums[n - i]

    for i in range(0, n):
        if left_sums[i] == right_sums[i]:
            yield i


test_arrays = [
    [1, 2, 3, 4, 2, 3, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [1, 2, 1, 2, 1, 2, 0, 9]
]

for test_array in test_arrays:
    print list(equilibrium_index(test_array))
