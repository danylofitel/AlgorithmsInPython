__author__ = 'Danylo'


# http://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/
# Given a number, find the next smallest palindrome
# Given a number, find the next smallest palindrome larger than this number.
# For example, if the input number is 23545, the output should be 23632.
# And if the input number is 999, the output should be 1001.
# The input is assumed to be an array.
# Every entry in array represents a digit in input number.
# Let the array be num[] and size of array be n


def is_palindrome(number):
    string = str(number)
    for i in range(len(string) / 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def next_palindrome(num):
    if num < 0:
        raise 'Negative number.'

    number = num
    if is_palindrome(number):
        number += 1
    original = str(number)
    length = len(original)

    mirror = list(str(number))
    for i in range(length):
        mirror[length - i - 1] = mirror[i]

    if int(''.join(mirror)) <= num:
        right = length / 2
        left = right - (length + 1) % 2

        while left >= 0:
            if int(mirror[right]) < int(original[right]):
                mirror[left] = original[right]
                mirror[right] = original[right]
                break
            elif mirror[right] == original[right] and original[right] != '9':
                mirror[left] = str(int(original[right]) + 1)
                mirror[right] = str(int(original[right]) + 1)
                break
            else:
                mirror[left] = '0'
                mirror[right] = '0'
            left -= 1
            right += 1

    result = int(''.join(mirror))
    assert result > num
    return result


test_numbers = [0, 1, 12, 32, 123, 999, 1221, 10000, 90909090, 1234543234565454321]
for n in test_numbers:
    print '{0} -> {1}'.format(n, next_palindrome(n))
