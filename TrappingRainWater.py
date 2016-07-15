__author__ = 'Danylo'


# http://www.geeksforgeeks.org/trapping-rain-water/
# Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.


def trapping_rain_water(arr):
    if arr is None or len(arr) == 0:
        return 0

    n = len(arr)
    max_so_far = 0
    max_left = [max_so_far]
    for i in range(1, n):
        max_so_far = max(arr[i - 1], max_so_far)
        max_left.append(max_so_far)

    max_so_far = 0
    max_right = [max_so_far]
    for i in range(n - 2, -1, -1):
        max_so_far = max(arr[i + 1], max_so_far)
        max_right = [max_so_far] + max_right

    water_sum = 0
    for i in range(1, n - 1):
        water_sum += max(min(max_left[i], max_right[i]) - arr[i], 0)

    return water_sum


def visualize(array):
    for x in array:
        print(['*' for i in range(0, x)])

arrays = [
    [2, 0, 2],
    [3, 0, 0, 2, 0, 4],
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
]

for arr in arrays:
    visualize(arr)
    print(trapping_rain_water(arr))
    print()
