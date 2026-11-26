from collections import Counter
from itertools import product
import unittest

from python.p0442_find_all_duplicates_in_an_array import Solution


class InPlaceDuplicateSignTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        counts = Counter(before)
        self.assertTrue(all(count <= 2 for count in counts.values()))
        expected = {value for value, count in counts.items() if count == 2}
        actual = Solution().findDuplicates(values)
        self.assertIs(type(actual), list)
        self.assertTrue(all(type(value) is int and value > 0 for value in actual))
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(set(actual), expected)
        self.assertEqual(list(map(abs, values)), before)

    def test_every_small_array_satisfying_value_and_multiplicity_promises(self):
        checked = 0
        for size in range(1, 7):
            for values in product(range(1, size + 1), repeat=size):
                if max(Counter(values).values()) <= 2:
                    self.check(list(values))
                    checked += 1
        self.assertGreater(checked, 30000)

    def test_future_marked_positions_and_maximum_array_length(self):
        self.check([2, 3, 2, 1, 5, 3])
        self.check([1])
        self.check([1, 1])
        self.check(list(range(1, 100001)))
        self.check(list(range(1, 50001)) * 2)
        self.check(list(range(1, 99999)) + [100000, 100000])


if __name__ == '__main__':
    unittest.main()
