from itertools import product
import re
import unittest

from python.p0537_complex_number_multiplication import Solution


def builtin_complex_oracle(first, second):
    def parse(text):
        match = re.fullmatch(r'(-?\d+)\+(-?\d+)i', text)
        return complex(*map(int, match.groups()))

    value = parse(first) * parse(second)
    return f'{int(value.real)}+{int(value.imag)}i'


class IntegerComplexProductTests(unittest.TestCase):
    def check(self, coefficients):
        a, b, c, d = coefficients
        first, second = f'{a}+{b}i', f'{c}+{d}i'
        actual = Solution().complexNumberMultiply(first, second)
        self.assertIs(type(actual), str)
        self.assertRegex(actual, r'^-?\d+\+-?\d+i$')
        self.assertEqual(actual, builtin_complex_oracle(first, second))

    def test_every_small_coefficient_quadruple_against_builtin_complex(self):
        count = 0
        for coefficients in product(range(-3, 4), repeat=4):
            self.check(coefficients)
            count += 1
        self.assertEqual(count, 2401)

    def test_endpoint_combinations_and_every_legal_coefficient_in_each_position(self):
        count = 0
        for coefficients in product((-100, -99, 0, 99, 100), repeat=4):
            self.check(coefficients)
            count += 1
        for position in range(4):
            for coefficient in range(-100, 101):
                values = [1, -1, 1, -1]
                values[position] = coefficient
                self.check(values)
                count += 1
        self.assertEqual(count, 1429)
        self.assertEqual(Solution().complexNumberMultiply('1+-1i', '1+-1i'), '0+-2i')
        self.assertEqual(Solution().complexNumberMultiply('0+0i', '-100+-100i'), '0+0i')


if __name__ == '__main__':
    unittest.main()
