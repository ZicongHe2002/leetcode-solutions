import unittest

from python.p0202_happy_number import Solution


def happy_by_visited_strings(value):
    visited = set()
    while value != 1 and value not in visited:
        visited.add(value)
        value = sum(int(character) ** 2 for character in str(value))
    return value == 1


class HappyNumberTests(unittest.TestCase):
    def check(self, value):
        result = Solution().isHappy(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, happy_by_visited_strings(value))

    def test_every_small_input_against_visited_string_digit_sums(self):
        for value in range(1, 10001):
            self.check(value)

    def test_maximum_integer_many_nines_powers_of_ten_and_cycle_entries(self):
        for value in (2**31 - 1, 2**31 - 2, 1999999999, 1000000000, 1, 7, 19, 2, 4):
            self.check(value)
        for exponent in range(10):
            self.assertTrue(Solution().isHappy(10**exponent))


if __name__ == '__main__':
    unittest.main()
