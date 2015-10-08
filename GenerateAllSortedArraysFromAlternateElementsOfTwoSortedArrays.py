__author__ = 'Danylo'


# http://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/
# Generate all possible sorted arrays from alternate elements of two given sorted arrays
# Given two sorted arrays A and B, generate all possible arrays such that
# first element is taken from A then from B then from A and so on in increasing order till the arrays exhausted.
# The generated arrays should end with an element from B.


def gsa(arr1, arr2, i, j, from_first, current):
    m = len(arr1)
    n = len(arr2)

    if from_first:
        if i >= m or (j > 0 and arr1[-1] < arr2[j - 1]):
            return [current]
    elif not from_first and i > 0:
        if j >= n or (i > 0 and arr2[-1] < arr1[i - 1]):
            return [current]

    results = []
    if from_first:
        for k in range(i, m):
            if j == 0 or arr1[k] >= arr2[j - 1]:
                for array in (gsa(arr1, arr2, k + 1, j, False, current + [arr1[k]])):
                    results.append(array)
    else:
        for k in range(j, n):
            if i == 0 or arr1[i - 1] <= arr2[k]:
                for array in gsa(arr1, arr2, i, k + 1, True, current + [arr2[k]]):
                    results.append(array)

    return results


def generate_sorted_arrays(arr1, arr2):
    if arr1 is None or arr2 is None:
        return None

    return gsa(arr1, arr2, 0, 0, True, [])


test_arrays = [
    [10, 15, 25],
    [1, 5, 20, 30],
    [1, 3, 4, 6, 7, 9, 10, 12, 15, 16, 17, 18, 20],
    [3, 4, 5, 6, 8, 10, 11, 13, 14, 16, 18, 19]
]

for array in generate_sorted_arrays(test_arrays[0], test_arrays[1]):
    print array
