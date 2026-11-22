import unittest
from itertools import permutations

from python.p0496_next_greater_element_i import Solution


def direct_right_scans(first, second):
    return [next((candidate for candidate in second[second.index(value) + 1:] if candidate > value), -1)
            for value in first]


class NextGreaterSubsetTests(unittest.TestCase):
    def check(self, first, second, expected=None):
        before_first, before_second = first[:], second[:]
        if expected is None:
            expected = direct_right_scans(first, second)
        result = Solution().nextGreaterElement(first, second)
        self.assertIs(type(result), list)
        self.assertEqual(result, expected)
        self.assertEqual((first, second), (before_first, before_second))

    def test_small_rank_permutations_and_reversed_subsets_against_right_scans(self):
        arrays = checks = 0
        for size in range(1, 7):
            for values in permutations(range(size)):
                arrays += 1
                for mask in range(1, 1 << size):
                    first = [values[index] for index in reversed(range(size)) if mask & (1 << index)]
                    self.check(first, list(values))
                    checks += 1
        self.assertEqual((arrays, checks), (873, 49489))

    def test_maximum_length_value_bounds_and_output_order(self):
        second = list(range(1, 1001))
        first = list(reversed(second))
        self.check(first, second, [-1] + list(range(1000, 1, -1)))
        second = list(range(10000, 9000, -1))
        self.check(list(reversed(second)), second, [-1] * 1000)
        self.check([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1])


if __name__ == '__main__':
    unittest.main()
