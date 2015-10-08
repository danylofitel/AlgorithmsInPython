__author__ = 'Vlad'

comparison_counter = 0


def second_max(arr):
    def is_greater(x, y):
        global comparison_counter
        comparison_counter += 1
        return x > y

    def build_pair_order():
        orders = {}
        i = 0
        while i < len(arr):
            first_i = i + 1
            second_i = i
            if is_greater(arr[i], arr[i + 1]):
                first_i = i
                second_i = i + 1
            orders[arr[first_i]] = arr[second_i]
            i += 2
        return orders

    def build_first_order(firsts):
        def flat(t):
            res = []
            for i in range(len(t)):
                if hasattr(t[i], '__iter__'):
                    for j in t[i]:
                        res.append(j)
                else:
                    res.append(t[i])
            return res

        new_firsts = {}
        while len(firsts) > 1:
            first_k = firsts.keys()[0]
            second_k = firsts.keys()[1]
            if not is_greater(first_k, second_k):
                first_k = second_k
                second_k = firsts.keys()[0]
            new_firsts[first_k] = flat((firsts[first_k], second_k))
            del firsts[first_k]
            del firsts[second_k]
            if len(firsts) == 0:
                firsts = new_firsts
                new_firsts = {}
        return firsts

    def build_second_order(first_order):
        def find_max(arr):
            max_val = 0
            i = 0
            if hasattr(arr, '__iter__'):
                while i < len(arr):
                    if i == 0:
                        max_val = arr[i]
                    elif is_greater(arr[i], max_val):
                        max_val = arr[i]
                    i += 1
            else:
                max_val = arr
            return max_val

        return (first_order.keys()[0], find_max(first_order.values()[0]))

    pair_order = build_pair_order()
    print 'Pair order:', pair_order
    import copy

    first_order = build_first_order(copy.deepcopy(pair_order))
    print 'First order:', first_order
    second_order = build_second_order(first_order)
    return second_order


test_arrays = [
    [1, 2],
    [2, 6, 3, 1],
    [1, 21, 3, 9, 5, 6, 7, 8],
    [1, 21, 3, 9, 5, 6, 7, 8, 24, 13, 25, 23, 21, 31, 34, 22],
    [1, 21, 3, 9, 5, 6, 7, 8, 24, 13, 25, 23, 21, 31, 34, 22, 14, 2, 10, 18, 4, 12, 11, 30, 32, 0, 15, 23, 19, 29, 28, 36]
]

for i in range(len(test_arrays)):
    test_arr = test_arrays[i]
    print i
    print test_arr
    print second_max(test_arr)
    print 'Number of comparisons =', comparison_counter
    print ''
    comparison_counter = 0
