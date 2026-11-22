import re
import unittest
from itertools import product

from python.p0008_string_to_integer_atoi import Solution


def regex_prefix_integer(text):
    match = re.match(r'^ *([+-]?[0-9]+)', text)
    value = int(match.group(1)) if match else 0
    return min(2**31 - 1, max(-2**31, value))


class AtoiTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = regex_prefix_integer(text)
        result = Solution().myAtoi(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_strings_against_regular_expression_prefix(self):
        checks = 0
        for size in range(6):
            for characters in product(' +-019x.', repeat=size):
                self.check(''.join(characters))
                checks += 1
        self.assertEqual(checks, 37449)

    def test_maximum_length_signs_spaces_decimal_stop_and_integer_clamping(self):
        self.check(' ' * 200, 0)
        self.check('-' + '9' * 199, -2**31)
        self.check('+' + '9' * 199, 2**31 - 1)
        self.check('0' * 199 + '7', 7)
        for text, expected in (('2147483647', 2147483647), ('2147483648', 2147483647),
                               ('-2147483648', -2147483648), ('-2147483649', -2147483648),
                               ('  -00042words', -42), ('3.14159', 3), ('+ 1', 0),
                               ('--2', 0), ('0 123', 0), ('-', 0), ('', 0)):
            self.check(text, expected)


if __name__ == '__main__':
    unittest.main()
