import unittest
from itertools import permutations

from python.p0268_missing_number import Solution


class MissingNumberTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        expected = (set(range(len(values) + 1)) - set(values)).pop()
        self.assertEqual(Solution().missingNumber(values), expected)
        self.assertEqual(values, before)

    def test_all_small_missing_values_and_input_orders_against_set_difference(self):
        checks = 0
        for n in range(1, 8):
            for missing in range(n + 1):
                values = [value for value in range(n + 1) if value != missing]
                for order in permutations(values):
                    self.check(list(order))
                    checks += 1
        self.assertEqual(checks, 46232)

    def test_maximum_length_missing_extremes_middle_and_empty_extension(self):
        for missing in [0, 5000, 10000]:
            self.check([value for value in range(10000, -1, -1) if value != missing])
        self.check([])


if __name__ == '__main__':
    unittest.main()
