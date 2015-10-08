__author__ = 'Danylo'


# http://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/
# How to print maximum number of A's using given four keys
# This is a famous interview question asked in Google, Paytm and many other company interviews.
# Below is the problem statement.

# Imagine you have a special keyboard with the following keys:
# Key 1:  Prints 'A' on screen
# Key 2: (Ctrl-A): Select screen
# Key 3: (Ctrl-C): Copy selection to buffer
# Key 4: (Ctrl-V): Print buffer on screen appending it
# after what has already been printed.

# If you can only press the keyboard for N times (with the above four
# keys), write a program to produce maximum numbers of A's. That is to
# say, the input parameter is N (No. of keys that you can press), the
# output is M (No. of As that you can produce).


def max_number_of_as(n):
    if n < 1:
        raise n + " is out of range, has to be a positive integer."

    cache = [1, 2, 3, 4, 5, 6]

    # expand cache
    for i in range(0, n - len(cache), 1):
        cache.append(0)

    for m in range(7, n + 1, 1):
        for b in range(n - 3, 0, -1):
            current = (m - b - 1) * cache[b - 1]
            if current > cache[m - 1]:
                cache[m - 1] = current

    return cache[n - 1]

print max_number_of_as(10)
