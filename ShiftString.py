__author__ = 'Danylo'


# Given a string like abcdef, rotate or shift the string n
# characters where n < the length of the string without allocating a newt
# string. Do it in-place. Hint: use multiple swapping


def shift_string(string, shift):
    if string is None:
        raise Exception("None string")

    n = len(string)
    if shift < 0 or shift >= n:
        raise Exception("Shift out of range")

    array = list(string)
    next_index = shift
    current_elem = array[0]
    for i in range(0, n):
        tmp = array[next_index]
        array[next_index] = current_elem
        current_elem = tmp

        next_index = (next_index + shift) % n

    return ''.join(array)

test_strings = [
    "",
    "a",
    "ab",
    "abc",
    "abcd",
    "abcde",
    "abcdef",
    "xyz"
]

for string in test_strings:
    for i in range(0, len(string)):
        print shift_string(string, i)
    print ""
