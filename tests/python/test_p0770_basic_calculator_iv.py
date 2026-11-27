import random
import unittest
from itertools import product

from python.p0770_basic_calculator_iv import Solution


def render(node):
    if isinstance(node, (int, str)):
        return str(node)
    operator, left, right = node
    return '(' + render(left) + ' ' + operator + ' ' + render(right) + ')'


def evaluate(node, values):
    if type(node) is int:
        return node
    if isinstance(node, str):
        return values[node]
    operator, left, right = node
    a, b = evaluate(left, values), evaluate(right, values)
    return a + b if operator == '+' else a - b if operator == '-' else a * b


def degree_bound(node):
    if type(node) is int:
        return 0
    if isinstance(node, str):
        return 1
    operator, left, right = node
    a, b = degree_bound(left), degree_bound(right)
    return a + b if operator == '*' else max(a, b)


def output_terms(texts):
    return [(int(parts[0]), tuple(parts[1:])) for parts in (text.split('*') for text in texts)]


class CalculatorFourTests(unittest.TestCase):
    def test_seeded_asts_partial_substitution_and_complete_degree_bounded_value_grids(self):
        rng = random.Random(770)

        def tree(depth):
            if not depth or rng.randrange(4) == 0:
                return rng.choice(('a', 'b', 0, 1, 3))
            return (rng.choice(('+','-','*')), tree(depth - 1), tree(depth - 1))

        checked = 0
        for _ in range(100):
            node = tree(3)
            expression, bound = render(node), degree_bound(node)
            self.assertLessEqual(len(expression), 250)
            for bindings in ({}, {'a':-2}, {'a':-2,'b':3}):
                names, integers = list(bindings), list(bindings.values())
                result = Solution().basicCalculatorIV(expression, names, integers)
                self.assertIs(type(result), list)
                terms = output_terms(result)
                monomials = [term for _, term in terms]
                remaining = sorted(set(('a','b')) - bindings.keys())
                self.assertEqual(monomials, sorted(monomials, key=lambda term: (-len(term), term)))
                self.assertEqual(len(monomials), len(set(monomials)))
                for text, (coefficient, term) in zip(result, terms):
                    self.assertNotEqual(coefficient, 0)
                    self.assertEqual(text, str(coefficient) + ''.join('*' + variable for variable in term))
                    self.assertEqual(tuple(sorted(term)), term)
                    self.assertTrue(set(term) <= set(remaining))
                    self.assertLessEqual(len(term), bound)
                for point in product(range(bound + 1), repeat=len(remaining)):
                    values = {**bindings, **dict(zip(remaining, point))}
                    total = 0
                    for coefficient, term in terms:
                        value = coefficient
                        for variable in term:
                            value *= values[variable]
                        total += value
                    self.assertEqual(total, evaluate(node, values), (expression, bindings, result, point))
                self.assertEqual((names, integers), (list(bindings), list(bindings.values())))
                checked += 1
        self.assertEqual(checked, 300)

    def test_official_examples_cancellation_multiletter_variables_and_deep_legal_parentheses(self):
        solver = Solution()
        self.assertEqual(solver.basicCalculatorIV('e + 8 - a + 5', ['e'], [1]), ['-1*a','14'])
        self.assertEqual(solver.basicCalculatorIV('e - 8 + temperature - pressure', ['e','temperature'], [1,12]), ['-1*pressure','5'])
        self.assertEqual(solver.basicCalculatorIV('(e + 8) * (e - 8)', [], []), ['1*e*e','-64'])
        self.assertEqual(solver.basicCalculatorIV('7 - 7', [], []), [])
        self.assertEqual(solver.basicCalculatorIV('a * b * c + b * a * c * 4', [], []), ['5*a*b*c'])
        self.assertEqual(solver.basicCalculatorIV('alpha * beta - beta * alpha', [], []), [])
        self.assertEqual(solver.basicCalculatorIV('a * a - a', ['a'], [-2]), ['6'])
        self.assertEqual(solver.basicCalculatorIV('(' * 124 + 'a' + ')' * 124, [], []), ['1*a'])


if __name__ == '__main__':
    unittest.main()
