from dataclasses import dataclass
from functools import cache
from itertools import product
import unittest

from python.p0101_symmetric_tree import Solution


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


def serialized(node, mirrored=False):
    if node is None:
        return None
    first, second = (node.right, node.left) if mirrored else (node.left, node.right)
    return node.val, serialized(first, mirrored), serialized(second, mirrored)


class SymmetricTreeTests(unittest.TestCase):
    def check(self, root, nodes, expected):
        before = [(node.val, node.left, node.right) for node in nodes]
        self.assertEqual(Solution().isSymmetric(root), expected)
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)
        try:
            for node, (_, left, right) in zip(nodes, before):
                node.left, node.right = right, left
            mirrored = [(node.val, node.left, node.right) for node in nodes]
            self.assertEqual(Solution().isSymmetric(root), expected)
            self.assertEqual([(node.val, node.left, node.right) for node in nodes], mirrored)
        finally:
            for node, (value, left, right) in zip(nodes, before):
                node.val, node.left, node.right = value, left, right
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)

    def test_all_small_shapes_and_binary_values_against_structural_oracle(self):
        checked = 0
        for count in range(7):
            for shape in shapes(count):
                for values in product((-1, 1), repeat=count):
                    nodes = []
                    root = build(shape, iter(values), nodes)
                    self.check(root, nodes, serialized(root) == serialized(root, True))
                    checked += 1
        self.assertEqual(checked, 10067)

    def test_deep_mirrors_value_mismatch_and_one_sided_upper_boundary(self):
        root = TreeNode(0)
        nodes = [root]
        left = right = root
        for _ in range(499):
            left.left = TreeNode(1)
            right.right = TreeNode(1)
            left, right = left.left, right.right
            nodes.extend((left, right))
        self.check(root, nodes, True)
        right.val = -1
        self.check(root, nodes, False)
        nodes = [TreeNode(1) for _ in range(1000)]
        for first, second in zip(nodes, nodes[1:]):
            first.left = second
        self.check(nodes[0], nodes, False)


if __name__ == '__main__':
    unittest.main()
