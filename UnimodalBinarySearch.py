__author__ = 'Danylo'


# A unimodal array is an array in which the elements first follow ascending order,
# then after the max element - descending order.
# Implement binary search in a unimodal array.


def ubs(array, left, right, elem):
    if left < right:
        current = (left + right) / 2

        if array[current] == elem:
            return current

        elem_bigger = array[current] < elem
        ascending = array[current] < array[current + 1]

        if elem_bigger:
            if ascending:
                # Only smaller elements to the left, larger elements exist to the right
                return ubs(array, current + 1, right, elem)
            else:
                if array[current - 1] < array[current]:
                    # Current is the maximum
                    return -1
                else:
                    # Larger elements exist to the right
                    return ubs(array, left, current - 1, elem)
        else:
            # Check the left side
            ls = ubs(array, left, current - 1, elem)
            if ls >= 0:
                # Element found on the left side
                return ls
            else:
                # Check the right side
                return ubs(array, current + 1, right, elem)

    elif left == right and array[left] == elem:
        return left
    else:
        return -1


def unimodal_binary_search(array, elem):
    if len(array) == 0:
        return None
    return ubs(array, 0, len(array) - 1, elem)


test_array = [-1, 1, 3, 5, 7, 9, 11, 13, 12, 10, 8, 6, 4, 2, 0, -2]

for i in test_array:
    print unimodal_binary_search(test_array, i)