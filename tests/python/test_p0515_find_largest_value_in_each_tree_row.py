from functools import lru_cache
from itertools import product
import unittest

from python.p0515_find_largest_value_in_each_tree_row import Solution


class Node:
    def __init__(self, value, left=None, right=None):
        self.val, self.left, self.right = value, left, right


@lru_cache(None)
def binary_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for count in range(size) for left in binary_shapes(count)
                 for right in binary_shapes(size - count - 1))


def fill_preorder(shape, values):
    if shape is None:
        return None
    value = next(values)
    return Node(value, fill_preorder(shape[0], values), fill_preorder(shape[1], values))


def depth_groups_and_snapshot(root):
    groups, snapshot = {}, {}
    pending = [(root, 0)] if root is not None else []
    while pending:
        node, depth = pending.pop()
        if id(node) in snapshot:
            raise AssertionError('the input must remain a proper tree')
        snapshot[id(node)] = (node.val, id(node.left) if node.left is not None else None,
                              id(node.right) if node.right is not None else None)
        groups.setdefault(depth, []).append(node.val)
        pending.extend((child, depth + 1) for child in (node.left, node.right) if child is not None)
    return groups, snapshot


class TreeLevelMaximumTests(unittest.TestCase):
    def check(self, root, expected=None):
        groups, before = depth_groups_and_snapshot(root)
        actual = Solution().largestValues(root)
        self.assertIs(type(actual), list)
        self.assertTrue(all(type(value) is int for value in actual))
        reference = [max(groups[depth]) for depth in sorted(groups)]
        self.assertEqual(actual, reference if expected is None else expected)
        self.assertEqual(depth_groups_and_snapshot(root)[1], before)

    def test_all_small_shapes_and_signed_values_against_dfs_depth_groups(self):
        trees = 0
        for size in range(6):
            for values in product((-1, 0, 1), repeat=size):
                for shape in binary_shapes(size):
                    self.check(fill_preorder(shape, iter(values)))
                    trees += 1
        self.assertEqual(trees, 11497)

    def test_maximum_depth_broad_negative_tree_and_signed_integer_limits(self):
        root = None
        for value in range(9999, -1, -1):
            root = Node(value, right=root)
        self.check(root, list(range(10000)))
        nodes = [Node(-index - 1) for index in range(8191)]
        for index in range(4095):
            nodes[index].left, nodes[index].right = nodes[2 * index + 1], nodes[2 * index + 2]
        self.check(nodes[0], [-(1 << depth) for depth in range(13)])
        self.check(Node(-(1 << 31), Node(-1), Node((1 << 31) - 1)), [-(1 << 31), (1 << 31) - 1])
        self.check(None, [])


if __name__ == '__main__':
    unittest.main()
