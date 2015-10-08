import heapq


__author__ = 'Danylo'


# http://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/
# Minimum steps to reach a destination
# Given a number line from -infinity to +infinity.
# You start at 0 and can go either to the left or to the right.
# The condition is that in ith move, you take i steps.
# a) Find if you can reach a given number x
# b) Find the most optimal way to reach a given number x, if we can indeed reach it.
# For example, 3 can be reached om 2 steps, (0, 1) (1, 3)
# and 4 can be reached in 3 steps (0, -1), (-1, 1) (1, 4).


def min_steps_to_reach_destination(start, finish, max_feasible_steps):
    if start == finish:
        return []

    queue = []
    heapq.heappush(queue, (1, start - 1, [-1]))
    heapq.heappush(queue, (1, start + 1, [+1]))

    while not len(queue) == 0:
        position = heapq.heappop(queue)

        if position[1] == finish:
            assert sum(position[2]) == finish - start
            optimal_paths = [position[2]]
            while not len(queue) == 0:
                candidate = heapq.heappop(queue)

                if candidate[0] > position[0]:
                    break
                elif candidate[1] != finish:
                    continue

                assert sum(candidate[2]) == finish - start
                optimal_paths.append(candidate[2])

            return optimal_paths
        elif position[0] > max_feasible_steps:
            return None

        steps = position[0] + 1
        heapq.heappush(queue, (steps, position[1] - steps, position[2] + [-steps]))
        heapq.heappush(queue, (steps, position[1] + steps, position[2] + [+steps]))

    return None


for path in min_steps_to_reach_destination(0, 50, 20):
    print path
