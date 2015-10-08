__author__ = 'Danylo'


# Count the number of palindromic substrings in a string.


def is_palindrome(s):
    for i in range(len(s) / 2):
        if s[i] <> s[len(s) - i - 1]:
            return False
    return True


def count_palindromes_n_3(s):
    count = 0
    for i in range(len(s)):
        for j in xrange(1, len(s) - i + 1, 1):
            if is_palindrome(s[i:i + j]):
                count += 1
    return count


def count_palindromes_n_2(s):
    count = 0
    n = len(s)
    for mid in range(0, n):
        count += 1
        radius = 0
        while mid - radius >= 0 and mid + radius + 1 < n and s[mid - radius] == s[mid + radius + 1]:
            count += 1
            radius += 1
        radius = 1
        while mid - radius >= 0 and mid + radius < n and s[mid - radius] == s[mid + radius]:
            count += 1
            radius += 1
    return count


def count_palindromes_n_log_n(s):
    count = 0
    return count


def count_palindromes_n(s):
    count = 0
    return count


test_strings = ['', 'a', 'aa', 'ab', 'aaa', 'aba', 'abc', 'aaaa', 'abab', 'aaaaa', 'ababa', 'abcdcbabc']
for string in test_strings:
    n3 = count_palindromes_n_3(string)
    n2 = count_palindromes_n_2(string)
    print '{0} : {1}, {2}'.format(n3, n2, n3 == n2)
