__author__ = 'Danylo'


# A unimodal array is an array in which the elements first follow ascending order,
# then after the max element - descending order.
# Find maximum element in O(log(n)).


def umm(array, left, right):
    if left < right:
        mid = (left + right) / 2
        if array[mid] < array[mid + 1]:
            return umm(array, mid + 1, right)
        elif array[mid - 1] > array[mid]:
            return umm(array, left, mid - 1)
        else:
            return array[mid]
    else:
        return array[left]


def unimodal_maximum(array):
    if len(array) == 0:
        return None
    return umm(array, 0, len(array) - 1)


test_array = [-1, 1, 3, 5, 7, 9, 11, 13, 12, 10, 8, 6, 4, 2, 0, -2, -4]

print unimodal_maximum(test_array)