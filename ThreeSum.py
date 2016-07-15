__author__ = 'Danylo'


# Find all triplets in the array that sum up to zero.


def three_sum_by_hashing(array):
    sorted_array = sorted(array)
    result = []
    elements = {}
    for i in range(len(sorted_array)):
        elements[sorted_array[i]] = i
    for i in range(len(sorted_array)):
        if i > 0 and sorted_array[i - 1] == sorted_array[i]:
            continue
        for j in range(i + 1, len(sorted_array)):
            if j > 0 and sorted_array[j - 1] == sorted_array[j]:
                continue
            third = - sorted_array[i] - sorted_array[j]
            if third in elements and elements[third] > j:
                result.append((sorted_array[i], sorted_array[j], third))
    return result


def three_sum_by_sorting(array):
    result = []
    sorted_array = sorted(array)
    for i in range(len(sorted_array) - 3):
        a = sorted_array[i]
        start = i + 1
        end = len(sorted_array) - 1
        while start < end:
            b = sorted_array[start]
            c = sorted_array[end]
            curr_sum = a + b + c
            if curr_sum == 0:
                result.append((a, b, c))
                while start + 1 < end and sorted_array[start + 1] == b:
                    start += 1
                while start < end - 1 and sorted_array[end - 1] == c:
                    end -= 1
                else:
                    start += 1
                    end -= 1
            elif curr_sum > 0:
                end -= 1
            else:
                start += 1
    return result


test_array = [1, 3, -2, 9, 6, 3, 5, -1, -8]

print(three_sum_by_hashing(test_array))
print(three_sum_by_sorting(test_array))
