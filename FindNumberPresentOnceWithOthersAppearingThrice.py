__author__ = 'Danylo'


# Numbers in array are repeated thrice except one number which is present just once.
# Find this number


def find_number_appearing_once(array):
    if array is None:
        raise Exception("Array is none")

    digits = 32

    binaries = (to_binary(x, digits) for x in array)
    bitsum = bitwise_add(binaries, digits)

    odd_appearing = list((x % 3 for x in bitsum))

    return to_number(odd_appearing)


def to_binary(number, digits):
    binary = []
    while number != 0:
        bit = number % 2
        binary.append(bit)
        number //= 2

    if len(binary) > digits:
        raise Exception("Number out of range")

    padding = digits - len(binary)
    for i in range(0, padding):
        binary.append(0)

    binary.reverse()
    return binary


def to_number(binary_array):
    result = 0
    current = 1

    for i in range(len(binary_array) - 1, -1, -1):
        if binary_array[i] > 0:
            result += current
        current *= 2

    return result


def bitwise_add(numbers, digits):
    result = [0 for i in range(0, digits)]

    for number in numbers:
        for digit in range(0, digits):
            result[digit] += number[digit]

    return result


test_arrays = [
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5],
    [1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
]

for test_array in test_arrays:
    print(find_number_appearing_once(test_array))
