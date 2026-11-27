from itertools import permutations
from math import comb
import unittest

from python.p0096_unique_binary_search_trees import Solution


def insertion_order_shape(order):
    if not order:
        return None
    root = order[0]
    left = tuple(value for value in order[1:] if value < root)
    right = tuple(value for value in order[1:] if value > root)
    return insertion_order_shape(left), insertion_order_shape(right)


class UniqueBSTInsertionOracleTests(unittest.TestCase):
    def test_small_sizes_against_all_insertion_order_shapes(self):
        checked_orders = 0
        for nodes in range(1, 8):
            shapes = set()
            for order in permutations(range(1, nodes + 1)):
                shapes.add(insertion_order_shape(order))
                checked_orders += 1
            result = Solution().numTrees(nodes)
            self.assertIs(type(result), int)
            self.assertEqual(result, len(shapes))
        self.assertEqual(checked_orders, 5913)

    def test_every_supported_size_against_closed_form_and_repeated_calls(self):
        solution = Solution()
        for nodes in range(1, 20):
            result = solution.numTrees(nodes)
            self.assertIs(type(result), int)
            self.assertEqual(result, comb(2 * nodes, nodes) // (nodes + 1))
        self.assertEqual(solution.numTrees(19), 1767263190)
        self.assertEqual(solution.numTrees(1), 1)
        self.assertEqual(solution.numTrees(3), 5)


if __name__ == '__main__':
    unittest.main()
