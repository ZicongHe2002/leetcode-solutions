from functools import lru_cache
from itertools import product
import unittest

from python.p0563_binary_tree_tilt import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in shapes(left_size) for right in shapes(size - 1 - left_size))


def materialize(shape, values):
    if shape is None:
        return None
    node = TreeNode(next(values))
    node.left = materialize(shape[0], values)
    node.right = materialize(shape[1], values)
    return node


def subtree_sum(root):
    return 0 if root is None else root.val + subtree_sum(root.left) + subtree_sum(root.right)


def repeated_sum_oracle(root):
    if root is None:
        return 0
    return (abs(subtree_sum(root.left) - subtree_sum(root.right))
            + repeated_sum_oracle(root.left) + repeated_sum_oracle(root.right))


def snapshot(root):
    pending = [root] if root is not None else []
    result = {}
    while pending:
        node = pending.pop()
        result[node] = (node.val, node.left, node.right)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return result


class BinaryTiltTests(unittest.TestCase):
    def check(self, root, expected):
        before = snapshot(root)
        result = Solution().findTilt(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(snapshot(root), before)

    def test_all_small_shapes_and_signed_labels_against_repeated_sums(self):
        checks = 0
        for size in range(6):
            for shape in shapes(size):
                for labels in product((-1, 0, 2), repeat=size):
                    root = materialize(shape, iter(labels))
                    self.check(root, repeated_sum_oracle(root))
                    checks += 1
        self.assertEqual(checks, 11497)

    def test_ten_thousand_depth_signed_overflow_and_examples(self):
        for value in (-1000, 1000):
            root = None
            for _ in range(10000):
                root = TreeNode(value, root)
            self.check(root, 1000 * 10000 * 9999 // 2)
        self.check(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)),
                            TreeNode(9, None, TreeNode(7))), 15)
        self.check(TreeNode(10, TreeNode(-3, TreeNode(3)), TreeNode(0)), 3)


if __name__ == '__main__':
    unittest.main()
