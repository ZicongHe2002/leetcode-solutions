from functools import lru_cache
from itertools import count
import unittest

from python.p0545_boundary_of_binary_tree import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def immutable_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in immutable_shapes(left_size)
                 for right in immutable_shapes(size - left_size - 1))


def materialize(shape, labels):
    if shape is None:
        return None
    left, right = shape
    return TreeNode(next(labels), materialize(left, labels), materialize(right, labels))


def full_leaf_paths_oracle(root):
    paths = []

    def collect(node, path):
        path = path + (node,)
        if node.left is None and node.right is None:
            paths.append(path)
        else:
            if node.left is not None:
                collect(node.left, path)
            if node.right is not None:
                collect(node.right, path)

    collect(root, ())
    if len(paths) == 1 and len(paths[0]) == 1:
        return [root.val]
    left = paths[0][1:-1] if root.left is not None else ()
    right = paths[-1][1:-1] if root.right is not None else ()
    boundary = [root] + list(left) + [path[-1] for path in paths] + list(reversed(right))
    return [node.val for node in boundary]


def snapshot(root):
    pending, records = [root], {}
    while pending:
        node = pending.pop()
        if id(node) in records:
            raise AssertionError('Repeated node or cycle in a tree')
        records[id(node)] = (node.val, id(node.left), id(node.right))
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return records


class AnticlockwiseBoundaryTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = snapshot(root)
        actual = Solution().boundaryOfBinaryTree(root)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, full_leaf_paths_oracle(root) if expected is None else expected)
        self.assertEqual(snapshot(root), before)

    def test_all_small_binary_shapes_against_complete_leaf_paths(self):
        trees = 0
        for size in range(1, 9):
            for shape in immutable_shapes(size):
                self.check(materialize(shape, count()))
                trees += 1
        self.assertEqual(trees, 2055)

    def test_maximum_depth_both_sides_repeated_values_and_missing_left_subtree(self):
        root = TreeNode(0)
        node = root
        for index in range(1, 10000):
            node.left = TreeNode(index % 1001)
            node = node.left
        self.assertEqual(len(snapshot(root)), 10000)
        self.check(root, [index % 1001 for index in range(10000)])
        root = TreeNode(0)
        node = root
        for index in range(1, 10000):
            node.right = TreeNode(index % 1001)
            node = node.right
        self.assertEqual(len(snapshot(root)), 10000)
        self.check(root, [0] + [index % 1001 for index in range(9999, 0, -1)])
        self.check(TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)),
                            TreeNode(0, TreeNode(0), TreeNode(0))), [0] * 7)
        self.check(TreeNode(-1000), [-1000])
        self.check(TreeNode(1, right=TreeNode(2, TreeNode(3), TreeNode(4))), [1, 3, 4, 2])


if __name__ == '__main__':
    unittest.main()
