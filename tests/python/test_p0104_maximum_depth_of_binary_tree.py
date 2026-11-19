from dataclasses import dataclass
from functools import cache
import unittest

from python.p0104_maximum_depth_of_binary_tree import Solution


@dataclass(eq=False)
class TreeNode:
    val: int
    left: object = None
    right: object = None


@cache
def shapes(count):
    if count == 0:
        return (None,)
    return tuple(
        (left, right)
        for left_count in range(count)
        for left in shapes(left_count)
        for right in shapes(count - 1 - left_count)
    )


def build(shape, nodes):
    if shape is None:
        return None
    node = TreeNode(len(nodes) % 3 - 1)
    nodes.append(node)
    node.left = build(shape[0], nodes)
    node.right = build(shape[1], nodes)
    return node


def recursive_depth(root):
    return 0 if root is None else 1 + max(recursive_depth(root.left), recursive_depth(root.right))


class MaximumDepthTests(unittest.TestCase):
    def check_tree(self, root, nodes, expected):
        before = [(node.val, node.left, node.right) for node in nodes]
        self.assertEqual(Solution().maxDepth(root), expected)
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)
        for node in nodes:
            node.left, node.right = node.right, node.left
        mirrored_before = [(node.val, node.left, node.right) for node in nodes]
        try:
            self.assertEqual(Solution().maxDepth(root), expected)
            self.assertEqual([(node.val, node.left, node.right) for node in nodes], mirrored_before)
        finally:
            for node, (_, left, right) in zip(nodes, before):
                node.left, node.right = left, right
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)

    def test_small_shapes_match_recursive_oracle_without_mutation(self):
        cases = 0
        for count in range(7):
            for shape in shapes(count):
                nodes = []
                root = build(shape, nodes)
                self.check_tree(root, nodes, recursive_depth(root))
                cases += 1
        self.assertEqual(cases, 197)

    def test_long_chains_without_recursive_construction_or_oracle(self):
        for side in ("left", "right"):
            nodes = [TreeNode(value % 3) for value in range(10000)]
            for parent, child in zip(nodes, nodes[1:]):
                setattr(parent, side, child)
            self.check_tree(nodes[0], nodes, 10000)


if __name__ == "__main__":
    unittest.main()
