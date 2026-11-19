from dataclasses import dataclass
from functools import cache
import unittest

from python.p0226_invert_binary_tree import Solution


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


def inorder_values(node):
    if node is None:
        return []
    return inorder_values(node.left) + [node.val] + inorder_values(node.right)


class InvertTreeTests(unittest.TestCase):
    def check_tree(self, root, nodes):
        before = [(node.val, node.left, node.right) for node in nodes]
        original_inorder = inorder_values(root)
        self.assertIs(Solution().invertTree(root), root)
        for node, (value, left, right) in zip(nodes, before):
            self.assertEqual(node.val, value)
            self.assertIs(node.left, right)
            self.assertIs(node.right, left)
        self.assertEqual(inorder_values(root), original_inorder[::-1])
        self.assertIs(Solution().invertTree(root), root)
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)
        self.assertEqual(inorder_values(root), original_inorder)

    def test_all_small_shapes_preserve_node_identity_and_restore_exact_edges(self):
        cases = 0
        for count in range(7):
            for shape in shapes(count):
                nodes = []
                root = build(shape, nodes)
                self.check_tree(root, nodes)
                cases += 1
        self.assertEqual(cases, 197)

    def test_left_and_right_chains_at_upper_node_boundary(self):
        for side in ("left", "right"):
            nodes = [TreeNode(value) for value in range(100)]
            for parent, child in zip(nodes, nodes[1:]):
                setattr(parent, side, child)
            self.check_tree(nodes[0], nodes)


if __name__ == "__main__":
    unittest.main()
