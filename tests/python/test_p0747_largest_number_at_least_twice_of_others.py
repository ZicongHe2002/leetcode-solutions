import unittest
from itertools import product

from python.p0747_largest_number_at_least_twice_of_others import Solution


def try_every_candidate(values):
    candidates = [index for index, value in enumerate(values)
                  if all(value >= 2 * other for position, other in enumerate(values) if position != index)]
    return candidates[0] if candidates else -1


class DominantIndexTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        result = Solution().dominantIndex(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, try_every_candidate(values) if expected is None else expected, values)
        self.assertEqual(values, before)

    def test_every_small_unique_maximum_array_against_each_candidate(self):
        checked = 0
        for size in range(2, 8):
            for values in product(range(5), repeat=size):
                if values.count(max(values)) == 1:
                    self.check(list(values))
                    checked += 1
        self.assertEqual(checked, 44310)

    def test_examples_fifty_element_limits_and_exact_factor_boundary(self):
        self.check([3,6,1,0], 1)
        self.check([1,2,3,4], -1)
        self.check([0,1], 1)
        self.check([50] * 49 + [100], 49)
        self.check([51] * 49 + [100], -1)
        self.check([100] + [49] * 49, 0)
        self.check([0] * 49 + [100], 49)


if __name__ == '__main__':
    unittest.main()
