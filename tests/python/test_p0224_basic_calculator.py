import ast
from functools import lru_cache
import unittest

from python.p0224_basic_calculator import Solution


def ast_integer_oracle(text):
    def visit(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.UnaryOp):
            return -visit(node.operand)
        left, right = visit(node.left), visit(node.right)
        return left + right if isinstance(node.op, ast.Add) else left - right
    return visit(ast.parse(text.strip(), mode='eval').body)


@lru_cache(None)
def expression_trees(leaves):
    if leaves == 1:
        return ('0', '1', '2')
    result = []
    for first_leaves in range(1, leaves):
        for first in expression_trees(first_leaves):
            for second in expression_trees(leaves - first_leaves):
                for operator in '+-':
                    result.append(f'({first}{operator}{second})')
    return tuple(result)


class CalculatorContextTests(unittest.TestCase):
    def test_all_small_parenthesis_trees_and_outer_negation_against_ast(self):
        cases = 0
        for leaves in range(1, 5):
            for core in expression_trees(leaves):
                for text in ('  ' + core + '  ', ' - (' + core + ') '):
                    actual = Solution().calculate(text)
                    self.assertIs(type(actual), int)
                    self.assertEqual(actual, ast_integer_oracle(text))
                    cases += 1
        self.assertEqual(cases, 6954)

    def test_unary_signs_deep_contexts_int32_and_long_chain(self):
        for text, expected in [('1-(-2)', 3), ('-(2+3)', -5), (' 2 - (5-6) ', 3), ('0-2147483647-1', -2147483648), ('2147483647-(2147483646)', 1)]:
            self.assertEqual(Solution().calculate(text), expected)
        depth = 5001
        self.assertEqual(Solution().calculate('-(' * depth + '1' + ')' * depth), -1)
        text = '1+' * 100000 + '1'
        self.assertEqual(len(text), 200001)
        self.assertEqual(Solution().calculate(text), 100001)


if __name__ == '__main__':
    unittest.main()
