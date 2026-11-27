from itertools import combinations
import unittest

from python.p0530_minimum_absolute_difference_in_bst import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def all_bst_shapes(values):
    if not values:
        return [None]
    trees = []
    for index, value in enumerate(values):
        for left in all_bst_shapes(values[:index]):
            for right in all_bst_shapes(values[index + 1:]):
                trees.append(TreeNode(value, left, right))
    return trees


def node_snapshot(root):
    pending, records = [root], {}
    while pending:
        node = pending.pop()
        records[id(node)] = (node.val, id(node.left), id(node.right))
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return records


def every_node_pair_oracle(root):
    values = [record[0] for record in node_snapshot(root).values()]
    return min(abs(left - right) for left, right in combinations(values, 2))


class InorderMinimumGapTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = node_snapshot(root)
        actual = Solution().getMinimumDifference(root)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, every_node_pair_oracle(root) if expected is None else expected)
        self.assertEqual(node_snapshot(root), before)

    def test_all_small_bst_shapes_and_value_subsets_against_every_node_pair(self):
        count = 0
        values = (0, 2, 5, 9, 20, 99999, 100000)
        for size in range(2, 7):
            for chosen in combinations(values, size):
                for tree in all_bst_shapes(chosen):
                    self.check(tree)
                    count += 1
        self.assertEqual(count, 2513)

    def test_maximum_depth_both_directions_zero_predecessor_and_value_limits(self):
        root = TreeNode(0)
        current = root
        for value in range(10, 100000, 10):
            current.right = TreeNode(value)
            current = current.right
        self.assertEqual(len(node_snapshot(root)), 10000)
        self.check(root, 10)
        root = TreeNode(100000)
        current = root
        for value in range(99990, 0, -10):
            current.left = TreeNode(value)
            current = current.left
        self.assertEqual(len(node_snapshot(root)), 10000)
        self.check(root, 10)
        self.check(TreeNode(0, right=TreeNode(100000)), 100000)
        self.check(TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49))), 1)
        self.check(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)), 1)


if __name__ == '__main__':
    unittest.main()
