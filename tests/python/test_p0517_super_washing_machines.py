from collections import deque
from functools import lru_cache
from itertools import product
import unittest

from python.p0517_super_washing_machines import Solution


@lru_cache(None)
def compositions(total, count):
    if count == 1:
        return ((total,),)
    return tuple((first,) + tail for first in range(total + 1)
                 for tail in compositions(total - first, count - 1))


@lru_cache(None)
def reverse_state_distances(count, total):
    states = compositions(total, count)
    reverse = {state: set() for state in states}
    for state in states:
        choices = []
        for index, load in enumerate(state):
            directions = [0]
            if load:
                if index:
                    directions.append(-1)
                if index + 1 < count:
                    directions.append(1)
            choices.append(directions)
        for directions in product(*choices):
            following = list(state)
            for index, direction in enumerate(directions):
                if direction:
                    following[index] -= 1
                    following[index + direction] += 1
            following = tuple(following)
            if following != state:
                reverse[following].add(state)
    target = (total // count,) * count
    distances, queue = {target: 0}, deque([target])
    while queue:
        state = queue.popleft()
        for predecessor in reverse[state]:
            if predecessor not in distances:
                distances[predecessor] = distances[state] + 1
                queue.append(predecessor)
    return distances


def simultaneous_move_oracle(machines):
    if not machines:
        return 0
    total, count = sum(machines), len(machines)
    if total % count:
        return -1
    return reverse_state_distances(count, total)[tuple(machines)]


class WashingCutFlowTests(unittest.TestCase):
    def check(self, machines, expected=None):
        before = machines[:]
        actual = Solution().findMinMoves(machines)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, simultaneous_move_oracle(machines) if expected is None else expected)
        self.assertEqual(machines, before)

    def test_all_small_distributions_against_legal_simultaneous_state_graphs(self):
        arrays = 0
        for size in range(5):
            for machines in product(range(4), repeat=size):
                self.check(list(machines))
                arrays += 1
        self.assertEqual(arrays, 341)
        self.check([0, 4, 0, 0])

    def test_maximum_count_load_nonintegral_and_two_sided_receive_send(self):
        self.check([100000] * 10000, 0)
        self.check([100000] + [0] * 9999, 99990)
        self.check([0, 100000] * 5000, 50000)
        self.check([0] * 9999 + [1], -1)
        self.check([3, 0, 3], 1)
        self.check([0, 3, 0], 2)
        self.check([1, 0, 5], 3)
        self.check([0, 2, 0], -1)


if __name__ == '__main__':
    unittest.main()
