__author__ = 'Danylo'


# http://www.geeksforgeeks.org/check-if-a-given-number-is-fancy/
# Check if a given number is Fancy
# A fancy number is one which when rotated 180 degrees is the same. Given a number, find whether it is fancy or not.
# 180 degree rotations of 6, 9, 1, 0 and 8 are 9, 6, 1, 0 and 8 respectively.


rotated_fancy_numbers = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}


def is_fancy(number):
    if number is None:
        return None

    count = len(number)
    for i in range(count / 2 + count % 2):
        if number[i] in rotated_fancy_numbers:
            if number[count - i - 1] != rotated_fancy_numbers[number[i]]:
                return False
        else:
            return False

    return True


test_fancy_numbers = [
    "",
    "0", "1", "8",
    "00", "11", "69", "88", "96",
    "000", "010", "818", "609", "916", "8698",
    "1001", "6969", "9696", "8008", "8888", "98886"
]

test_not_fancy_numbers = [
    "2", "3", "4", "5", "6", "7", "9",
    "01", "12", "34", "45", "56", "67", "78", "89", "90",
    "020", "007", "747", "666", "999", "6696",
    "1010", "6996", "9669", "0808", "1100", "98889"
]

for num in test_fancy_numbers:
    print num, " : ", is_fancy(num)

for num in test_not_fancy_numbers:
    print num, " : ", is_fancy(num)
