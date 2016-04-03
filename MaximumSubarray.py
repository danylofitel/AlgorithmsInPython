__author__ = 'Danylo'


# http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# Largest Sum Contiguous Subarray
# Write an efficient C program to find the sum of contiguous subarray
# within a one-dimensional array of numbers which has the largest sum.

# Kadane's Algorithm:
# Initialize:
#    max_so_far = 0
#    max_ending_here = 0
# Loop for each element of the array
#  (a) max_ending_here = max_ending_here + a[i]
#  (b) if(max_ending_here < 0)
#            max_ending_here = 0
#  (c) if(max_so_far < max_ending_here)
#            max_so_far = max_ending_here
# return max_so_far


def max_subarray(a, b):
    if a[0] > b[0]:
        return a
    else:
        return b


def maximum_subarray(array):
    max_ending_here = (array[0], 0, 1)
    max_so_far = (array[0], 0, 1)

    for i in range(1, len(array)):
        max_ending_here = max_subarray((max_ending_here[0] + array[i], max_ending_here[1], i + 1), (array[i], i, i + 1))
        max_so_far = max_subarray(max_ending_here, max_so_far)

    return max_so_far


test_array = [-2, 0, 9, 2, 1, -5, 9, 3, -3, -1, 5]
print maximum_subarray(test_array)

test_array = [-4, 3, -2, 1, 0, 1, 2, -3]
print maximum_subarray(test_array)
