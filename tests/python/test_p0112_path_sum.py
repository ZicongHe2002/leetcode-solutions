from dataclasses import dataclass
from functools import cache
from itertools import product
import unittest

from python.p0112_path_sum import Solution


@dataclass(eq=False)
class TreeNode:
    val: int
    left: object = None
    right: object = None


@cache
def shapes(count):
    if count == 0:
        return (None,)
    return tuple((left, right) for size in range(count)
                 for left in shapes(size) for right in shapes(count - 1 - size))


def build(shape, values, nodes):
    if shape is None:
        return None
    node = TreeNode(next(values))
    nodes.append(node)
    node.left = build(shape[0], values, nodes)
    node.right = build(shape[1], values, nodes)
    return node


def leaf_sums(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    return [root.val + total for total in leaf_sums(root.left) + leaf_sums(root.right)]


class PathSumTests(unittest.TestCase):
    def check(self, root, nodes, target, expected):
        before = [(node.val, node.left, node.right) for node in nodes]
        self.assertEqual(Solution().hasPathSum(root, target), expected)
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)
        try:
            for node, (value, _, _) in zip(nodes, before):
                node.val = -value
            negated = [(node.val, node.left, node.right) for node in nodes]
            self.assertEqual(Solution().hasPathSum(root, -target), expected)
            self.assertEqual([(node.val, node.left, node.right) for node in nodes], negated)
        finally:
            for node, (value, left, right) in zip(nodes, before):
                node.val, node.left, node.right = value, left, right
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)

    def test_small_shapes_values_and_targets_against_all_leaf_sums(self):
        checked = 0
        for count in range(6):
            for shape in shapes(count):
                for values in product((-1, 0, 1), repeat=count):
                    nodes = []
                    root = build(shape, iter(values), nodes)
                    sums = leaf_sums(root)
                    for target in range(-3, 4):
                        self.check(root, nodes, target, target in sums)
                        checked += 1
        self.assertEqual(checked, 80479)

    def test_internal_match_negative_cancellation_and_maximum_depth(self):
        child = TreeNode(2)
        root = TreeNode(1, child)
        self.check(root, [root, child], 1, False)
        child.val = -2
        self.check(root, [root, child], -1, True)
        left, leaf = TreeNode(4), TreeNode(-3)
        right = TreeNode(-2, leaf)
        branching = TreeNode(5, left, right)
        self.check(branching, [branching, left, right, leaf], 0, True)
        self.check(branching, [branching, left, right, leaf], 5, False)
        self.check(None, [], 0, False)
        nodes = [TreeNode(0) for _ in range(5000)]
        for parent, child in zip(nodes, nodes[1:]):
            parent.right = child
        self.check(nodes[0], nodes, 0, True)
        self.check(nodes[0], nodes, 1, False)


if __name__ == '__main__':
    unittest.main()
