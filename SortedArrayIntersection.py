__author__ = 'Danylo'


# http://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/
# Union and Intersection of two sorted arrays
# Given two sorted arrays, find their union and intersection.

# For example, if the input arrays are:
# arr1[] = {1, 3, 4, 5, 7}
# arr2[] = {2, 3, 5, 6}
# Then your program should print Union as {1, 2, 3, 4, 5, 6, 7} and Intersection as {3, 5}.


def intersection(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0
    res = []
    while i < m and j < n:
        elem1 = arr1[i]
        elem2 = arr2[j]
        if elem1 == elem2:
            res.append(elem1)
            i += 1
            j += 1
        elif elem1 < elem2:
            i += 1
        else:
            j += 1

    return res


def union(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0
    res = []
    while i < m and j < n:
        elem1 = arr1[i]
        elem2 = arr2[j]
        if elem1 <= elem2:
            res.append(elem1)
            i += 1
        else:
            res.append(elem2)
            j += 1

    while i < m:
        res.append(arr1[i])
        i += 1

    while j < n:
        res.append(arr2[j])
        j += 1

    assert len(res) == m + n

    return res


test_arrays = [
    [1, 3, 4, 6, 7, 9, 10, 12, 15, 16, 17, 18, 20],
    [3, 4, 5, 6, 8, 10, 11, 13, 14, 16, 18, 19]
]


print(intersection(test_arrays[0], test_arrays[1]))
print(union(test_arrays[0], test_arrays[1]))
