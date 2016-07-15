__author__ = 'Danylo'


# http://www.geeksforgeeks.org/longest-consecutive-subsequence/
# Longest Consecutive Subsequence
# Given an array of integers, find the length of the longest sub-sequence
# such that elements in the subsequence are consecutive integers,
# the consecutive numbers can be in any order.


def longest_consecutive_subsequence_sorting(arr):
    if arr is None:
        return None

    if len(arr) == 0:
        return []

    arr.sort()

    longest = []
    current = []
    for x in arr:
        if len(current) == 0 or x == current[-1] + 1:
            current.append(x)
        else:
            if len(current) > len(longest):
                longest = current
                current = []

    return longest


def longest_consecutive_subsequence_hashing(arr):
    if arr is None:
        return None

    if len(arr) == 0:
        return []

    lookup = {}
    for x in arr:
        lookup[x] = x

    longest = []
    for x in arr:
        if not (x - 1) in lookup:
            current = [x]
            while (x + 1) in lookup:
                x += 1
                current.append(x)
            if len(current) > len(longest):
                longest = current

    return longest


arrays = [
    [1, 9, 3, 10, 4, 20, 2],
    [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
]

for arr in arrays:
    print(longest_consecutive_subsequence_sorting(arr))
    print(longest_consecutive_subsequence_hashing(arr))
