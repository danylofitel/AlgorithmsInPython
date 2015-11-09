__author__ = 'Danylo'

# http://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
# Reverse an array without affecting special characters
# Given a string, that contains special character together with alphabets
# (a to z and A to Z), reverse the string in a way that special characters are not affected.

# Examples:
# Input:   str = "a,b$c"
# Output:  str = "c,b$a"


def reverse_ignoring_special_characters(array, special_characters):
    if special_characters is None:
        special_characters = {}

    count = len(array)
    left = 0
    right = count - 1

    while left < right:
        if array[left] in special_characters:
            left += 1
        elif array[right] in special_characters:
            right -= 1
        else:
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp
            left += 1
            right -= 1

    return array

print reverse_ignoring_special_characters(list("a,b$c"), list(",$"))
print reverse_ignoring_special_characters(list("Ab,c,de!$"), list(",!$"))
