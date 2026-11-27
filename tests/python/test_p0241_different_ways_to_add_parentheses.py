from itertools import product
import unittest

from python.p0241_different_ways_to_add_parentheses import Solution


def reduction_order_oracle(numbers, operators):
    completed = {}

    def reduce_adjacent(nodes, signs):
        if not signs:
            value, tree = nodes[0]
            completed[tree] = value
            return
        for index, sign in enumerate(signs):
            left, left_tree = nodes[index]
            right, right_tree = nodes[index + 1]
            value = {'+': lambda: left + right, '-': lambda: left - right,
                     '*': lambda: left * right}[sign]()
            tree = f'({left_tree}{sign}{right_tree})'
            reduce_adjacent(nodes[:index] + [(value, tree)] + nodes[index + 2:], signs[:index] + signs[index + 1:])

    reduce_adjacent([(value, f'x{index}') for index, value in enumerate(numbers)], list(operators))
    return sorted(completed.values())


class ParenthesizationTreeTests(unittest.TestCase):
    def test_all_small_expressions_against_adjacent_reduction_trees(self):
        expressions = 0
        for size in range(1, 5):
            for numbers in product((0, 1, 2), repeat=size):
                for operators in product('+-*', repeat=size - 1):
                    text = ''.join(str(value) + (operators[index] if index < size - 1 else '') for index, value in enumerate(numbers))
                    actual = Solution().diffWaysToCompute(text)
                    self.assertTrue(all(type(value) is int for value in actual))
                    self.assertEqual(sorted(actual), reduction_order_oracle(numbers, operators))
                    expressions += 1
        self.assertEqual(expressions, 2460)

    def test_multiple_digits_duplicate_results_subtraction_and_call_isolation(self):
        solver = Solution()
        self.assertEqual(sorted(solver.diffWaysToCompute('2*3-4*5')), [-34, -14, -10, -10, 10])
        self.assertEqual(sorted(solver.diffWaysToCompute('2-1-1')), [0, 2])
        self.assertEqual(solver.diffWaysToCompute('11'), [11])
        self.assertEqual(solver.diffWaysToCompute('0'), [0])
        self.assertEqual(solver.diffWaysToCompute('99*99*99'), [970299, 970299])
        text = '99' + '+0' * 9
        self.assertEqual(len(text), 20)
        self.assertEqual(solver.diffWaysToCompute(text), [99] * 4862)


if __name__ == '__main__':
    unittest.main()
