__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
# Find minimum number of coins that make a given value
# Given a value V, if we want to make change for V cents,
# and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins,
# what is the minimum number of coins to make the change?


def min_number_of_coins_help(coins, value, cache):
    if value in cache:
        return cache[value]

    if value == 0 or value in coins:
        cache[value] = 1
        return 1
    elif value < 0:
        return None

    min_so_far = None
    for c in coins:
        if c <= value:
            c_coins = min_number_of_coins_help(coins, value - c, cache)
            if min_so_far is None or c_coins < min_so_far:
                min_so_far = c_coins

    if min_so_far is None:
        return None

    cache[value] = 1 + min_so_far
    return 1 + min_so_far


def min_number_of_coins(coins, value):
    return min_number_of_coins_help(coins, value, {})


# Returns a given sum represented as coins for a limited amount of each coin type.
class CoinMachine:

    def __init__(self):
        pass

    available_coins = {}
    coin_values = []
    count = 0

    def to_coins_help(self, value, index, coin_selection):
        if value == 0:
            return coin_selection
        elif index > self.count:
            return None

        current_coin_value = self.coin_values[index]
        max_current = min(value // current_coin_value, self.available_coins[current_coin_value])

        for i in range(max_current, -1, -1):
            coin_selection.append(i)
            res = self.to_coins_help(value - i * current_coin_value, index + 1, coin_selection)
            if res is not None:
                return res
            coin_selection.pop(-1)

        return None

    def to_coins(self, available_coins, value):
        if available_coins is None or value is None or value < 0:
            return None

        for c in available_coins:
            if c is None or c < 0 or available_coins[c] is None or available_coins[c] < 0:
                return None

        coin_values = list(available_coins.keys())
        coin_values.sort(reverse=True)

        self.available_coins = available_coins
        self.coin_values = coin_values
        self.count = len(coin_values)

        selection = self.to_coins_help(value, 0, [])
        if selection is None:
            return None

        result = {}
        for i in range(len(selection)):
            count = selection[i]
            if count > 0:
                result[coin_values[i]] = selection[i]

        return result

coins = [25, 10, 5]
print(min_number_of_coins(coins, 2995))

coins = {
    5: 2,
    2: 7,
    1: 3,
    10: 4,
    25: 1,
    50: 2
}

machine = CoinMachine()

for i in range(101):
    print("{0} : {1}".format(i, machine.to_coins(coins, i)))
