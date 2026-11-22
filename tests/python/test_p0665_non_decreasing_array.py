from itertools import product
import unittest

from python.p0665_non_decreasing_array import Solution


def explicit_one_replacement(values):
    def ordered(candidate):
        return all(left <= right for left, right in zip(candidate, candidate[1:]))
    if ordered(values):
        return True
    for index in range(len(values)):
        for replacement in range(-2, 3):
            candidate = values[:]
            candidate[index] = replacement
            if ordered(candidate):
                return True
    return False


class OneEditMonotonicityTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = explicit_one_replacement(values)
        result = Solution().checkPossibility(values)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_actual_replacements(self):
        checks = 0
        for size in range(1, 9):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_one_or_two_repairs_and_value_limits(self):
        self.check(list(range(10000)), True)
        values = list(range(10000))
        values[5000] = -100000
        self.check(values, True)
        values = list(range(10000))
        values[3000] = values[7000] = -100000
        self.check(values, False)
        self.check([100000] + [-100000] * 9999, True)
        self.check([100000, 100000] + [-100000] * 9998, False)
        self.check([3, 4, 2, 3], False)


if __name__ == '__main__':
    unittest.main()
