__author__ = 'Danylo'


# Figure out the sequence.
# Each row depends only on the previous one.
# Hint: flip-flop circuit.


string_data = [
    "0000010100010011010010110111110110111",
    "0000010100010011011000001111111110111",
    "0000010100010011001001110111111010111",
    "0000010100010011000100111111111100111",
    "0000010100010011000011101111101110111",
    "0000010100010011010101100111110110111",
    "0000010100010011001110000111111110111",
    "0000010100010011010010110111111010111",
    "0000010100010011011000101111111100111",
    "0000010100010011001001110111101110111",
    "0000010100010011000100111111110110111",
    "0000010100010011000011001111111110111"
]


binary_data = map(lambda x: long(x, 2), string_data)


def print_diff(first, second):
    if first == '0':
        f = 0
    else:
        f = 1

    if second == '0':
        s = 0
    else:
        s = 1

    return s - f


def print_diffs():
    for string in range(1, len(string_data)):
        output = []
        for i in range(len(string_data[string])):
            if string_data[string - 1][i] != string_data[string][i]:
                output.append((i, print_diff(string_data[string - 1][i], string_data[string][i])))
        print output


def print_characters(string, character):
    result = []
    zeros = True
    current = 0

    for c in string + ' ':
        if c != character:
            if not zeros:
                result.append(current)
                current = 0
                zeros = True
        elif c == character:
            current += 1
            if zeros:
                zeros = False

    return result


def print_consecutive_characters():
    for string in string_data:
        print print_characters(string, '0')
        print print_characters(string, '1')
        print


def print_len():
    for string in string_data:
        print len(string)

print_consecutive_characters()
print_diffs()


for i in range(1, len(binary_data)):
    print bin(binary_data[i - 1] & binary_data[i])

