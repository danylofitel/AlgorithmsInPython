__author__ = 'Danylo'


# http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# Longest Increasing Subsequence
# Given an array of random numbers. Find longest increasing subsequence (LIS) in the array


# Dynamic programming implementation of LIS problem in O(n^2)
def longest_increasing_subsequence_dp(arr):
    n = len(arr)

    # Declare the list for LIS and initialize LIS values for all indexes
    lis_ending_here = [1] * n

    # Compute optimized LIS values in bottom-up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_ending_here[i] < lis_ending_here[j] + 1:
                lis_ending_here[i] = lis_ending_here[j] + 1

    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis_ending_here[i])

    return maximum


# Binary search (note boundaries in the caller)
# A is ceilIndex in the caller
def ceil_index(arr, l, r, key):
    while r - l > 1:
        m = l + (r - l) / 2
        if arr[m] >= key:
            r = m
        else:
            l = m

    return r


def longest_increasing_subsequence(arr):
    size = len(arr)
    length = 1
    tail_table = [0] * size
    tail_table[0] = arr[0]

    for i in range(1, size):
        if arr[i] < tail_table[0]:
            # new smallest value
            tail_table[0] = arr[i]

        elif arr[i] > tail_table[length - 1]:
            # A[i] wants to extend largest subsequence
            tail_table[length] = arr[i]
            length += 1
        else:
            # A[i] wants to be current end candidate of an existing
            # subsequence. It will replace ceil value in tail_table
            tail_table[ceil_index(tail_table, -1, length - 1, arr[i])] = arr[i]

    return length


test_arrays = [
    [10, 22, 9, 33, 21, 50, 41, 60],
    [2, 5, 3, 7, 11, 8, 10, 13, 6]
]

for array in test_arrays:
    lis_dp = longest_increasing_subsequence_dp(array)
    lis = longest_increasing_subsequence(array)
    assert lis == lis_dp
    print "Length of LIS is ", lis
