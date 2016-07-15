from math import pow, log, floor
from random import shuffle


__author__ = 'Danylo'


# Find the second largest element in the array in no more than n + log(n, 2) - 2 comparisons.


def is_power_of_2(num):
    if num <= 0:
        return False
    return pow(2, floor(log(num, 2))) == num


class SecondLargest:
    comparisons = 0

    def __init__(self):
        return

    def less(self, a, b):
        self.comparisons += 1
        return a[0] < b[0]

    def second_largest(self, array):
        if not is_power_of_2(len(array)):
            raise Exception("Array size is not the power of 2.")
        self.comparisons = 0
        comparison_array = self.prepare_comparison_array(array)
        while len(comparison_array) > 1:
            comparison_array = self.pairwise_largest(comparison_array)
        return max(comparison_array[0][1])

    def prepare_comparison_array(self, original_array):
        array = []
        for x in original_array:
            array.append((x, []))
        return array

    def pairwise_largest(self, array):
        new_array = []
        for index in range(0, len(array) - 1, 2):
            min_elem = array[index]
            max_elem = array[index + 1]
            if self.less(max_elem, min_elem):
                tmp = min_elem
                min_elem = max_elem
                max_elem = tmp
            max_elem[1].append(min_elem[0])
            new_array.append(max_elem)
        return new_array


sl = SecondLargest()
for p in range(1, 10, 1):
    n = 2 ** p
    test_array = [i for i in range(n)]
    shuffle(test_array)

    print(sl.second_largest(test_array))
    print(sl.comparisons <= n + log(n, 2) - 2)
