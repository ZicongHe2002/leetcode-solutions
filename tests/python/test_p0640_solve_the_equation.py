import random
import unittest
from itertools import product

from python.p0640_solve_the_equation import Solution


def render(terms):
    text = ''
    for token, _, _ in terms:
        text += ('+' if text and not token.startswith('-') else '') + token
    return text


def model_answer(left_coefficient, left_constant, right_coefficient, right_constant):
    coefficient = left_coefficient - right_coefficient
    numerator = right_constant - left_constant
    if coefficient == 0:
        return 'Infinite solutions' if numerator == 0 else 'No solution'
    if numerator % coefficient:
        return None
    return f'x={numerator // coefficient}'


def constant_terms(value):
    sign = -1 if value < 0 else 1
    magnitude = abs(value)
    terms = [str(sign * 100)] * (magnitude // 100)
    if magnitude % 100 or not terms:
        terms.append(str(sign * (magnitude % 100)))
    return [(term, 0, int(term)) for term in terms]


class EquationTests(unittest.TestCase):
    def check(self, equation, expected):
        self.assertGreaterEqual(len(equation), 3)
        self.assertLessEqual(len(equation), 1000)
        actual = Solution().solveEquation(equation)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, expected, equation)

    def test_small_term_combinations_against_known_symbolic_coefficients(self):
        kinds = [('x', 1, 0), ('-x', -1, 0), ('0x', 0, 0), ('0', 0, 0),
                 ('1', 0, 1), ('-1', 0, -1), ('2x', 2, 0), ('-2x', -2, 0),
                 ('100', 0, 100), ('-100', 0, -100)]
        sides = [(render(terms), sum(term[1] for term in terms), sum(term[2] for term in terms))
                 for size in (1, 2) for terms in product(kinds, repeat=size)]
        checked = 0
        for left, right in product(sides, repeat=2):
            expected = model_answer(left[1], left[2], right[1], right[2])
            if expected is not None:
                self.check(left[0] + '=' + right[0], expected)
                checked += 1
        self.assertGreater(checked, 7000)

    def test_seeded_integer_roots_and_maximum_length(self):
        rng = random.Random(640)
        for _ in range(1000):
            left, right = rng.sample(range(-10, 11), 2)
            root, constant = rng.randint(-10, 10), rng.randint(-10, 10)
            other = (left - right) * root + constant
            lhs = [(f'{left}x', left, 0)] + constant_terms(constant)
            rhs = [(f'{right}x', right, 0)] + constant_terms(other)
            self.check(render(lhs) + '=' + render(rhs), f'x={root}')
        long_equation = ('x+' * 249 + 'x') + '=' + ('x+' * 249 + '10')
        self.assertEqual(len(long_equation), 1000)
        self.check(long_equation, 'x=10')
        for equation, expected in [('0x=0', 'Infinite solutions'), ('0x=1', 'No solution'),
                                   ('-x=1', 'x=-1'), ('-x=-100', 'x=100'),
                                   ('100x=-100', 'x=-1'), ('x+5-3+x=6+x-2', 'x=2')]:
            self.check(equation, expected)


if __name__ == '__main__':
    unittest.main()
