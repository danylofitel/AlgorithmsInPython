__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/
# Find a Fixed Point in a given array
# Given an array of n distinct integers sorted in ascending order,
# write a function that returns a Fixed Point in the array,
# if there is any Fixed Point present in array, else returns -1.
# Fixed Point in an array is an index i such that arr[i] is equal to i.
# Note that integers in array can be negative.


def bs(array, left, right):
    if left < right:
        mid = (left + right) / 2
        if array[mid] == mid:
            return mid
        elif array[left] > mid:
            return None
        elif array[mid] > mid:
            return bs(array, left, mid)
        else:
            ls = bs(array, left, mid - 1)
            if ls is not None:
                return ls
            else:
                return bs(array, mid + 1, right)
    else:
        if array[left] == left:
            return left
        else:
            return None


def identity_binary_search_iterative(array):
    if len(array) == 0:
        return None
    return bs(array, 0, len(array) - 1)


def ibs(array, left, right):
    if left > right:
        return None

    middle_index = (left + right) / 2
    middle_item = array[middle_index]

    if middle_index == middle_item:
        return middle_index
    elif middle_index > middle_item:
        return ibs(array, middle_index + 1, right)
    else:
        return ibs(array, left, middle_index - 1)


def identity_binary_search_recursive(array):
    if len(array) == 0:
        return None
    return ibs(array, 0, len(array) - 1)


test_array_true = [-1, 0, 2, 3, 5, 6, 9]
test_array_false = [-1, 0, 1, 2, 3, 8, 9]

print identity_binary_search_recursive(test_array_true)
print identity_binary_search_iterative(test_array_true)

print identity_binary_search_recursive(test_array_false)
print identity_binary_search_iterative(test_array_false)
