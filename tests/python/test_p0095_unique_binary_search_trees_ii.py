from itertools import permutations
import unittest

from python.p0095_unique_binary_search_trees_ii import Solution, TreeNode


def insertion_order_tree(order):
    if not order:
        return None
    root = order[0]
    left = tuple(value for value in order[1:] if value < root)
    right = tuple(value for value in order[1:] if value > root)
    return root, insertion_order_tree(left), insertion_order_tree(right)


class GeneratedBSTInsertionOracleTests(unittest.TestCase):
    def signature(self, root, seen):
        if root is None:
            return None
        self.assertIs(type(root), TreeNode)
        self.assertNotIn(id(root), seen, 'cycle or shared mutable node')
        seen.add(id(root))
        return root.val, self.signature(root.left, seen), self.signature(root.right, seen)

    def test_all_supported_sizes_against_all_insertion_orders(self):
        orders = trees = nodes = 0
        for size in range(1, 9):
            expected = set()
            for order in permutations(range(1, size + 1)):
                expected.add(insertion_order_tree(order))
                orders += 1
            result = Solution().generateTrees(size)
            self.assertIs(type(result), list)
            seen = set()
            actual = [self.signature(root, seen) for root in result]
            self.assertEqual(len(actual), len(set(actual)))
            self.assertEqual(set(actual), expected)
            self.assertEqual(len(seen), size * len(result))
            trees += len(result)
            nodes += len(seen)
        self.assertEqual((orders, trees, nodes), (46233, 2055, 15521))

    def test_mutating_one_result_does_not_affect_other_trees_or_calls(self):
        solution = Solution()
        first = solution.generateTrees(3)
        before_others = [self.signature(root, set()) for root in first[1:]]
        first[0].right.val = 100
        self.assertEqual([self.signature(root, set()) for root in first[1:]], before_others)
        second = solution.generateTrees(3)
        old_ids = set()
        for root in first:
            self.signature(root, old_ids)
        new_ids = set()
        actual = [self.signature(root, new_ids) for root in second]
        self.assertTrue(old_ids.isdisjoint(new_ids))
        self.assertEqual(set(actual), {insertion_order_tree(order) for order in permutations((1, 2, 3))})


if __name__ == '__main__':
    unittest.main()
