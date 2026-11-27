from itertools import product
import unittest

from python.p0473_matchsticks_to_square import Solution


def four_container_oracle(sticks):
    if len(sticks) < 4 or sum(sticks) % 4:
        return False
    target = sum(sticks) // 4
    sides = [0] * 4

    def assign(index):
        if index == len(sticks):
            return all(length == target for length in sides)
        tried = set()
        for side in range(4):
            if sides[side] in tried or sides[side] + sticks[index] > target:
                continue
            tried.add(sides[side])
            sides[side] += sticks[index]
            if assign(index + 1):
                return True
            sides[side] -= sticks[index]
        return False

    return assign(0)


class MatchstickSubsetRemainderTests(unittest.TestCase):
    def check(self, sticks, expected=None):
        before = sticks[:]
        actual = Solution().makesquare(sticks)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, four_container_oracle(sticks) if expected is None else expected)
        self.assertEqual(sticks, before)

    def test_all_small_stick_arrays_against_explicit_four_side_assignments(self):
        arrays = 0
        for size in range(9):
            for sticks in product((1, 2, 3), repeat=size):
                self.check(list(sticks))
                arrays += 1
        self.assertEqual(arrays, 9841)

    def test_maximum_sticks_lengths_and_necessary_conditions_not_sufficient(self):
        self.check([1] * 12 + [4] * 3, True)
        self.check([10**8] * 15, False)
        self.check([10**8] * 4, True)
        self.check([10**8] * 12 + [2, 2, 4], False)
        self.check([3, 3, 3, 3, 4], False)
        self.check([1, 1, 2, 2, 2], True)
        self.check([10, 1, 1, 4], False)
        self.check([1, 1, 1], False)


if __name__ == '__main__':
    unittest.main()
