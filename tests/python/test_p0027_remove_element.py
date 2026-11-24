import unittest
from itertools import product

from python.p0027_remove_element import Solution


class RemoveElementTests(unittest.TestCase):
    def check(self, values, target):
        before = values[:]
        expected = [value for value in before if value != target]
        result = Solution().removeElement(values, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, len(expected))
        self.assertEqual(values[:result], expected)
        self.assertEqual(len(values), len(before))

    def test_all_small_arrays_against_stable_filter(self):
        for size in range(8):
            for values in product((0, 1, 50), repeat=size):
                for target in (0, 1, 2, 50, 100):
                    self.check(list(values), target)

    def test_empty_maximum_length_and_extreme_targets(self):
        self.check([], 0)
        self.check([50] * 100, 50)
        self.check([0] * 100, 100)
        self.check([50, 0] * 50, 50)
        self.check([0, 50] * 50, 0)
        self.check([1], 1)


if __name__ == '__main__':
    unittest.main()
