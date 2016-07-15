__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-maximum-average-subarray-of-k-length/
# Find maximum average subarray of k length
# Given an array with positive and negative numbers, find the maximum average subarray of given length.


def max_average_subarray_extra_space(arr, k):
    if arr is None or k < 0 or k > len(arr):
        raise Exception("Arguments out of range")

    n = len(arr)
    if len(arr) == 0 or k == 0:
        return 0

    cumulative = [arr[0]]

    for i in range(1, n):
        cumulative.append(cumulative[i - 1] + arr[i])

    max_sum = cumulative[k - 1]
    for i in range(1, n - k + 1):
        max_sum = max(max_sum, cumulative[i + k - 1] - cumulative[i - 1])

    return max_sum


def max_average_subarray(arr, k):
    if arr is None or k < 0 or k > len(arr):
        raise Exception("Arguments out of range")

    n = len(arr)
    if len(arr) == 0 or k == 0:
        return 0

    curr_sum = sum(arr[:4])
    max_sum = curr_sum

    for i in range(k, n):
        curr_sum -= arr[i - k]
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)

    return max_sum


array = [1, 12, -5, -6, 50, 3]

print(max_average_subarray_extra_space(array, 4))
print(max_average_subarray(array, 4))
