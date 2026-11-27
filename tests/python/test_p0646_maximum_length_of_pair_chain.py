from itertools import product
import unittest

from python.p0646_maximum_length_of_pair_chain import Solution


def all_feasible_chain_orders(pairs):
    def extend(used, previous_end):
        return max([0] + [1 + extend(used | (1 << index), right)
                          for index, (left, right) in enumerate(pairs)
                          if not used >> index & 1
                          and (previous_end is None or previous_end < left)])

    return extend(0, None)


class StrictPairChainTests(unittest.TestCase):
    def check(self, pairs, expected=None):
        before = [pair[:] for pair in pairs]
        if expected is None:
            expected = all_feasible_chain_orders(pairs)
        result = Solution().findLongestChain(pairs)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(pairs, before)

    def test_all_small_pair_arrays_against_every_feasible_selection_order(self):
        vocabulary = ((-3, -2), (-2, -1), (-1, 0), (0, 1), (1, 2), (-3, 2))
        checks = 0
        for size in range(1, 6):
            for pairs in product(vocabulary, repeat=size):
                self.check([list(pair) for pair in pairs])
                checks += 1
        self.assertEqual(checks, 9330)

    def test_maximum_length_strict_touching_nested_and_equal_endpoints(self):
        chain = [[start, start + 1] for start in range(-1000, 1000, 2)]
        self.check(chain[::-1], 1000)
        self.check([[0, 1] for _ in range(1000)], 1)
        self.check([[start, start + 1] for start in range(-500, 500)], 500)
        self.check([[start, 1000] for start in range(-1000, 0)], 1)
        self.check([[-1000, 1000], [-2, -1], [0, 1], [2, 3]], 3)
        self.check([[1, 2], [2, 3], [3, 4]], 2)


if __name__ == '__main__':
    unittest.main()
