import unittest
from fractions import Fraction

from python.p0150_evaluate_rpn import Solution


class RpnTests(unittest.TestCase):
    def check(self, tokens, expected):
        before = list(tokens)
        self.assertEqual(Solution().evalRPN(tokens), expected)
        self.assertEqual(tokens, before)

    def test_all_small_expression_trees_against_tree_values(self):
        trees = {1: [((str(value),), value) for value in range(-2, 3)]}
        for leaves in range(2, 4):
            trees[leaves] = []
            for left_size in range(1, leaves):
                for left_tokens, left in trees[left_size]:
                    for right_tokens, right in trees[leaves - left_size]:
                        for operation in '+-*/':
                            if operation == '/' and right == 0:
                                continue
                            if operation == '+':
                                expected = left + right
                            elif operation == '-':
                                expected = left - right
                            elif operation == '*':
                                expected = left * right
                            else:
                                expected = int(Fraction(left, right))
                            trees[leaves].append((left_tokens + right_tokens + (operation,), expected))
        checked = 0
        for expressions in trees.values():
            for tokens, expected in expressions:
                self.check(list(tokens), expected)
                checked += 1
        self.assertGreater(checked, 3000)

    def test_sign_operand_order_and_maximum_legal_length(self):
        for tokens, expected in [(['2', '1', '+', '3', '*'], 9), (['4', '13', '5', '/', '+'], 6),
                                 (['-7', '3', '/'], -2), (['7', '-3', '/'], -2),
                                 (['-7', '-3', '/'], 2), (['10', '3', '-'], 7),
                                 (['3', '10', '-'], -7), (['-200', '200', '*'], -40000),
                                 (['200', '200', '*', '200', '*', '200', '*', '200', '+'], 1600000200),
                                 (['-200'], -200)]:
            self.check(tokens, expected)
        wide = ['200'] * 5000 + ['+'] * 4999
        chain = ['0'] + ['200', '-'] * 4999
        self.assertEqual((len(wide), len(chain)), (9999, 9999))
        self.check(wide, 1000000)
        self.check(chain, -999800)


if __name__ == '__main__':
    unittest.main()
