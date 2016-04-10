__author__ = 'Danylo'


# http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
# Count number of binary strings without consecutive 1s
# Given a positive integer N, count all possible distinct binary strings of length N
# such that there are no consecutive 1s


# The cached results for strings that end in 0 and 1 resp.
ending_in_0 = [0, 1]
ending_in_1 = [0, 1]


# This is actually Fibonacci series, thus current implementation is not the optimal one.
def binary_strings_with_no_consecutive_ones(length):
    current = len(ending_in_0)
    if length < current:
        return ending_in_0[length] + ending_in_1[length]

    # Recursively compute values for shorter strings
    binary_strings_with_no_consecutive_ones(length - 1)

    # 0 or 1 can be appended to all shorter strings ending in 0
    ending_in_0.append(ending_in_0[length - 1] + ending_in_1[length - 1])

    # Only 1 can be appended to all shorter strings ending in 0
    ending_in_1.append(ending_in_0[length - 1])

    return ending_in_0[length] + ending_in_1[length]

for i in range(0, 100):
    print binary_strings_with_no_consecutive_ones(i)
