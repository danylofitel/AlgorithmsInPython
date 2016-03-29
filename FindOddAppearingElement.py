__author__ = 'Danylo'


# Find the odd appearing element in O(n) time
# Given an array where all elements appear even number of times except one.
# Find the element that appears odd number of times.


def find_odd_appearing_element(arr):
    if arr is None:
        raise Exception("Array is None.")

    n = len(arr)
    if n % 2 == 0:
        raise Exception("Array contains even numer of elements.")

    xor = 0

    for elem in arr:
        xor = xor ^ elem

    return xor


arrays = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 6, 600, 600, 4, 4]
]

for arr in arrays:
    print arr
    print find_odd_appearing_element(arr)
