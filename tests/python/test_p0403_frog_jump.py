from itertools import combinations
import unittest

from python.p0403_frog_jump import Solution


def enumerate_next_stone(stones):
    def visit(index, previous):
        if index == len(stones) - 1:
            return True
        for following in range(index + 1, len(stones)):
            step = stones[following] - stones[index]
            if step in (previous - 1, previous, previous + 1) and visit(following, step):
                return True
        return False
    return bool(stones) and visit(0, 0)


class FrogArrivalLengthTests(unittest.TestCase):
    def check(self, stones, expected=None):
        before = stones[:]
        actual = Solution().canCross(stones)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, enumerate_next_stone(stones) if expected is None else expected)
        self.assertEqual(stones, before)

    def test_all_small_stone_subsets_against_direct_next_landing_search(self):
        inputs = 0
        for size in range(13):
            for positions in combinations(range(1, 13), size):
                self.check([0, *positions])
                inputs += 1
        self.assertEqual(inputs, 4096)
        self.check([], False)

    def test_maximum_stones_large_coordinates_and_distinct_jump_histories(self):
        self.check([0, 1, 3, 5, 6, 8, 12, 17], True)
        self.check([0, 1, 2, 3, 4, 8, 9, 11], False)
        self.check([0, 2], False)
        self.check(list(range(2000)), True)
        self.check([index * (index + 1) // 2 for index in range(2000)], True)
        self.check(list(range(1999)) + [2**31 - 1], False)


if __name__ == '__main__':
    unittest.main()
