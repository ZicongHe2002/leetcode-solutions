from functools import lru_cache
from itertools import product
import unittest

from python.p0572_subtree_of_another_tree import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for k in range(size)
                 for left in shapes(k) for right in shapes(size - 1 - k))


def materialize(shape, values):
    if shape is None:
        return None
    node = TreeNode(next(values))
    node.left = materialize(shape[0], values)
    node.right = materialize(shape[1], values)
    return node


def equal_trees(left, right):
    if left is None or right is None:
        return left is right
    return (left.val == right.val and equal_trees(left.left, right.left)
            and equal_trees(left.right, right.right))


def candidate_node_oracle(root, target):
    if target is None:
        return True
    if root is None:
        return False
    return (equal_trees(root, target) or candidate_node_oracle(root.left, target)
            or candidate_node_oracle(root.right, target))


def snapshot(root):
    pending = [] if root is None else [root]
    result = {}
    while pending:
        node = pending.pop()
        result[node] = (node.val, node.left, node.right)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return result


def chain(size, bottom_value=1):
    root = TreeNode(bottom_value)
    for _ in range(size - 1):
        root = TreeNode(1, root)
    return root


class SubtreeTests(unittest.TestCase):
    def check(self, root, target, expected):
        before = (snapshot(root), snapshot(target))
        result = Solution().isSubtree(root, target)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual((snapshot(root), snapshot(target)), before)

    def test_all_small_labeled_tree_pairs_against_structural_comparison(self):
        trees = [materialize(shape, iter(values)) for size in range(4) for shape in shapes(size)
                 for values in product((-1, 1, 11), repeat=size)]
        self.assertEqual(len(trees), 157)
        checks = 0
        for root in trees:
            for target in trees:
                self.check(root, target, candidate_node_oracle(root, target))
                checks += 1
        self.assertEqual(checks, 24649)

    def test_deep_repeated_prefix_structure_and_value_boundaries(self):
        root = chain(2000)
        self.check(root, chain(1000), True)
        self.check(root, chain(1000, 2), False)
        whole = chain(1000)
        self.check(whole, whole, True)
        self.check(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)), False)
        self.check(TreeNode(12), TreeNode(2), False)
        self.check(TreeNode(-10000, TreeNode(10000)), TreeNode(10000), True)
        self.check(TreeNode(1, TreeNode(2)), TreeNode(1), False)


if __name__ == '__main__':
    unittest.main()
