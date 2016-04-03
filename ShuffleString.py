__author__ = 'Danylo'


# Shuffle the string so that no two equal characters are together
# e.g. ABBAABC => ABABABC


def shuffle_string(string):
    if string is None:
        raise Exception("None string")

    lst = list(string)
    n = len(string)

    lst.sort()

    shuffled = map(lambda index: lst[index] + lst[n / 2 + index], range(0, n / 2))
    if n % 2 == 1:
        shuffled.append(lst[n - 1])

    return ''.join(shuffled)


print shuffle_string("BBCCDDEA")
