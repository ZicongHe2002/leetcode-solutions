import unittest

from python.p0066_plus_one import Solution


class PlusOneTests(unittest.TestCase):
    def check(self, digits):
        before = digits[:]
        value = int(''.join(map(str, before)))
        expected = list(map(int, str(value + 1)))
        result = Solution().plusOne(digits)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, expected)
        self.assertEqual(digits, before)
        self.assertIsNot(result, digits)

    def test_all_small_integers_against_integer_addition(self):
        for value in range(10000):
            self.check(list(map(int, str(value))))

    def test_maximum_digits_and_carry_chain_boundaries(self):
        self.check([9] * 100)
        self.check([1] + [0] * 99)
        self.check([1] + [9] * 99)
        self.check([9] * 99 + [8])
        self.check([0])
        self.check([1, 2, 9])


if __name__ == '__main__':
    unittest.main()
