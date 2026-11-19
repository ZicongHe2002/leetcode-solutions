from dataclasses import dataclass
from functools import cache
import unittest

from python.p0094_binary_tree_inorder_traversal import Solution


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


def recursive_inorder(root):
    if root is None:
        return []
    return recursive_inorder(root.left) + [root.val] + recursive_inorder(root.right)


class InorderTraversalTests(unittest.TestCase):
    def check_tree(self, root, nodes, expected):
        before = [(node.val, node.left, node.right) for node in nodes]
        self.assertEqual(Solution().inorderTraversal(root), expected)
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)
        for node in nodes:
            node.val = -node.val
        mapped_before = [(node.val, node.left, node.right) for node in nodes]
        try:
            self.assertEqual(Solution().inorderTraversal(root), [-value for value in expected])
            self.assertEqual([(node.val, node.left, node.right) for node in nodes], mapped_before)
        finally:
            for node, (value, _, _) in zip(nodes, before):
                node.val = value
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)

    def test_all_small_shapes_with_repeated_values_and_topology(self):
        cases = 0
        for count in range(7):
            for shape in shapes(count):
                nodes = []
                root = build(shape, nodes)
                self.check_tree(root, nodes, recursive_inorder(root))
                cases += 1
        self.assertEqual(cases, 197)

    def test_left_and_right_chains_at_upper_node_boundary(self):
        for side in ("left", "right"):
            nodes = [TreeNode(value) for value in range(100)]
            for parent, child in zip(nodes, nodes[1:]):
                setattr(parent, side, child)
            expected = list(range(100))
            if side == "left":
                expected.reverse()
            self.check_tree(nodes[0], nodes, expected)


if __name__ == "__main__":
    unittest.main()
