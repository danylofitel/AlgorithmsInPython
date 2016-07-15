__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-the-element-that-odd-number-of-times-in-olog-n-time/
# Find the odd appearing element in O(Log n) time
# Given an array where all elements appear even number of times except one.
# All repeating occurrences of elements appear in pairs and these pairs are not adjacent
# (there cannot be more than two consecutive occurrences of any element).
# Find the element that appears odd number of times.


def find_odd_appearing_element_pair(arr):
    if arr is None:
        raise Exception("Array is None.")

    n = len(arr)

    left = 0
    right = n - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] == arr[mid + 1]:
            starting_mid = mid
        elif arr[mid - 1] == arr[mid]:
            starting_mid = mid - 1
        else:
            return mid

        if starting_mid % 2 == 0:
            left = mid + 1
        else:
            right = mid - 1

    return left


arrays = [
    [1, 1, 2, 2, 1, 1, 2, 2, 13, 1, 1, 40, 40, 13, 13],
    [1, 1, 2, 2, 3, 3, 4, 4, 3, 600, 600, 4, 4]
]

for arr in arrays:
    odd_index = find_odd_appearing_element_pair(arr)
    print(arr)
    print("{0} at position {1}".format(arr[odd_index], odd_index))
