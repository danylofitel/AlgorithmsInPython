__author__ = 'Danylo'


# http://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/
# Convert array into Zig-Zag fashion
# Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time.
# The converted array should be in form a < b > c < d > e < f ...


def zig_zag_array_by_sorting(array):
    if array is None:
        return None

    array.sort()

    for i in range(1, len(array) / 2):
        tmp = array[2 * i - 1]
        array[2 * i - 1] = array[2 * i]
        array[2 * i] = tmp

    return array


def zig_zag_array(array):
    if array is None:
        return None

    increasing = True
    for i in range(0, len(array) - 1):
        if (increasing and array[i] > array[i + 1]) or (not increasing and array[i] < array[i + 1]):
            tmp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = tmp
        increasing = not increasing

    return array


def visualize(array):
    for x in array:
        print ['*' for i in range(0, x)]


arr = [4, 3, 7, 8, 6, 2, 1]

print zig_zag_array_by_sorting(arr)
visualize(zig_zag_array_by_sorting(arr))

print zig_zag_array(arr)
visualize(zig_zag_array(arr))
