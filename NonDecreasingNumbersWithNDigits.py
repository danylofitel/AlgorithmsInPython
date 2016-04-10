__author__ = 'Danylo'


# http://www.geeksforgeeks.org/total-number-of-non-decreasing-numbers-with-n-digits/
# Total number of non-decreasing numbers with n digits
# A number is non-decreasing if every digit (except the first one) is greater than or equal to previous digit.
# For example, 223, 4455567, 899, are non-decreasing numbers.
# So, given the number of digits n, you are required to find the count of total non-decreasing numbers with n digits.


def non_decreasing_numbers_dynamic(length):
    # cache[i][j] contains total count of non decreasing numbers ending with digit i and of length j
    cache = [[0 for x in range(0, length + 1)] for x in range(0, 10)]

    for i in range(0, 10):
        # Non-decreasing numbers of length 1
        cache[i][1] = 1

    for n in range(2, length + 1):
        for digit in range(0, 10):
            for x in range(0, digit + 1):
                cache[digit][n] += cache[x][n - 1]

    count = 0
    for i in range(0, 10):
        count += cache[i][length]
    return count

print non_decreasing_numbers_dynamic(10)
