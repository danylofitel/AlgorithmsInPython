__author__ = 'Danylo'


# Find all pairs in the array that sum up to zero.


def two_sum_by_hashing(array):
    result = []
    elements = {}
    for i in range(len(array)):
        elements[array[i]] = False
    for i in array:
        if -i in elements and not elements[-i]:
            elements[i] = True
            elements[-i] = True
            result.append((i, -i))
    return result


def two_sum_by_sorting(array):
    result = []
    sorted_array = sorted(array)
    start = 0
    end = len(sorted_array) - 1
    while start < end:
        a = sorted_array[start]
        b = sorted_array[end]
        if a + b == 0:
            result.append((a, b))
            while start + 1 < end and sorted_array[start + 1] == a:
                start += 1
            while start < end - 1 and sorted_array[end - 1] == b:
                end -= 1
            else:
                start += 1
                end -= 1
        elif a + b > 0:
            end -= 1
        else:
            start += 1
    return result


test_array = [1, 3, -2, 9, 6, 3, 5, -1, -8, -3, -5, 1]

print two_sum_by_hashing(test_array)
print two_sum_by_sorting(test_array)
