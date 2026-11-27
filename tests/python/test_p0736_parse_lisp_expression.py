import random
import unittest
from itertools import product

from python.p0736_parse_lisp_expression import Solution


def checked(value):
    if not -2**31 <= value <= 2**31 - 1:
        raise OverflowError
    return value


def interpret_tree(tree, environment):
    if isinstance(tree, int):
        return checked(tree)
    if isinstance(tree, str):
        return environment[tree]
    operation = tree[0]
    if operation == 'let':
        local = dict(environment)
        for name, value in tree[1]:
            local[name] = interpret_tree(value, local)
        return interpret_tree(tree[2], local)
    left, right = interpret_tree(tree[1], environment), interpret_tree(tree[2], environment)
    return checked(left + right if operation == 'add' else left * right)


def render_tree(tree):
    if isinstance(tree, (int, str)):
        return str(tree)
    if tree[0] == 'let':
        bindings = ' '.join(name + ' ' + render_tree(value) for name, value in tree[1])
        return '(let ' + bindings + ' ' + render_tree(tree[2]) + ')'
    return '(' + tree[0] + ' ' + render_tree(tree[1]) + ' ' + render_tree(tree[2]) + ')'


def generate_tree(rng, depth, environment):
    if not depth or rng.random() < 0.3:
        return rng.choice(list(range(-3, 4)) + list(environment))
    operation = rng.choice(('add', 'mult', 'let'))
    if operation != 'let':
        return (operation, generate_tree(rng, depth - 1, environment), generate_tree(rng, depth - 1, environment))
    local, bindings = dict(environment), []
    for _ in range(rng.randrange(1, 4)):
        name = rng.choice(('x', 'y', 'a1'))
        value = generate_tree(rng, depth - 1, local)
        local[name] = interpret_tree(value, local)
        bindings.append((name, value))
    return ('let', bindings, generate_tree(rng, depth - 1, local))


class ParseLispTests(unittest.TestCase):
    def check_text(self, expression, expected):
        self.assertTrue(1 <= len(expression) <= 2000)
        result = Solution().evaluate(expression)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, expression[:100])

    def check_tree(self, tree):
        self.check_text(render_tree(tree), interpret_tree(tree, {}))

    def test_constructed_arithmetic_shadowing_and_seeded_legal_trees_against_environment_copies(self):
        checked_cases = 0
        for operation in ('add', 'mult'):
            for left, right in product(range(-2, 3), repeat=2):
                self.check_tree((operation, left, right))
                checked_cases += 1
        for outer, first, increment in product(range(-2, 3), repeat=3):
            inner = ('let', [('x', first), ('x', ('add', 'x', increment))], 'x')
            self.check_tree(('let', [('x', outer)], ('add', inner, 'x')))
            checked_cases += 1
        self.assertEqual(checked_cases, 175)
        rng, accepted = random.Random(736), 0
        while accepted < 1000:
            try:
                tree = generate_tree(rng, rng.randrange(5), {})
                expected = interpret_tree(tree, {})
            except OverflowError:
                continue
            expression = render_tree(tree)
            if len(expression) <= 2000:
                self.check_text(expression, expected)
                accepted += 1
        self.assertEqual(accepted, 1000)

    def test_official_scope_examples_integer_boundaries_and_deep_legal_expressions(self):
        for expression, expected in (
                ('(let x 2 (mult x (let x 3 y 4 (add x y))))', 14),
                ('(let x 3 x 2 x)', 2), ('(let x 1 y 2 x (add x y) (add x y))', 5),
                ('(let x 2 (add (let x 3 x) x))', 5), ('(let x 5 (let x (add x 1) x))', 6),
                ('(let a1 3 b2 4 (add a1 b2))', 7), ('(let x 7 y x y)', 7),
                ('(let x 1 -2)', -2), ('(let x 1 0)', 0),
                ('-2147483648', -2147483648), ('(add 2147483647 0)', 2147483647),
                ('(mult -2147483648 1)', -2147483648)):
            self.check_text(expression, expected)
        expression = '0'
        for _ in range(249):
            expression = '(add 1 ' + expression + ')'
        self.assertEqual(len(expression), 1993)
        self.check_text(expression, 249)
        expression = 'x'
        for value in range(190):
            expression = '(let x ' + str(value % 10) + ' ' + expression + ')'
        self.assertEqual(len(expression), 1901)
        self.check_text(expression, 0)
        self.check_text('(let x 0 ' + 'x (add x 1) ' * 150 + 'x)', 150)


if __name__ == '__main__':
    unittest.main()
