import unittest
from itertools import permutations

from python.p0634_find_the_derangement_of_an_array import Solution


MODULUS = 10**9 + 7


def inclusion_exclusion(n):
    quotient = 1
    result = 0
    for fixed_count in range(n, -1, -1):
        result = (result + (-quotient if fixed_count % 2 else quotient)) % MODULUS
        quotient = quotient * fixed_count % MODULUS
    return result


class DerangementTests(unittest.TestCase):
    def check(self, n, expected):
        actual = Solution().findDerangement(n)
        self.assertIs(type(actual), int)
        self.assertGreaterEqual(actual, 0)
        self.assertLess(actual, MODULUS)
        self.assertEqual(actual, expected, n)

    def test_all_small_permutations_by_fixed_position_exclusion(self):
        checked = 0
        for n in range(1, 10):
            expected = 0
            for values in permutations(range(n)):
                expected += all(value != index for index, value in enumerate(values))
                checked += 1
            self.check(n, expected)
        self.assertEqual(checked, 409113)

    def test_modular_inclusion_exclusion_through_maximum_n(self):
        for n in (10, 25, 100, 999, 100000, 999999, 1000000):
            self.check(n, inclusion_exclusion(n))


if __name__ == '__main__':
    unittest.main()
