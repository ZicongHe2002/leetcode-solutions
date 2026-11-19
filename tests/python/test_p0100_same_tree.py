from dataclasses import dataclass
from functools import cache
from itertools import product
import unittest

from python.p0100_same_tree import Solution


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
        return None, None
    value = next(values)
    left, left_encoding = build(shape[0], values, nodes)
    right, right_encoding = build(shape[1], values, nodes)
    node = TreeNode(value, left, right)
    nodes.append(node)
    return node, (value, left_encoding, right_encoding)


class SameTreeTests(unittest.TestCase):
    def check(self, first, second, nodes, expected):
        # The ordered-pair enumeration also passes the same tree twice.
        nodes = list({id(node): node for node in nodes}.values())
        before = [(node.val, node.left, node.right) for node in nodes]
        self.assertEqual(Solution().isSameTree(first, second), expected)
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)
        try:
            for node, (value, _, _) in zip(nodes, before):
                node.val = -value
            mapped = [(node.val, node.left, node.right) for node in nodes]
            self.assertEqual(Solution().isSameTree(first, second), expected)
            self.assertEqual([(node.val, node.left, node.right) for node in nodes], mapped)
        finally:
            for node, (value, left, right) in zip(nodes, before):
                node.val, node.left, node.right = value, left, right
        self.assertEqual([(node.val, node.left, node.right) for node in nodes], before)

    def test_all_small_ordered_tree_pairs_against_tuple_encodings(self):
        trees = []
        for count in range(4):
            for shape in shapes(count):
                for values in product((-1, 1), repeat=count):
                    nodes = []
                    root, encoding = build(shape, iter(values), nodes)
                    trees.append((root, encoding, nodes))
        self.assertEqual(len(trees), 51)
        for first, first_encoding, first_nodes in trees:
            for second, second_encoding, second_nodes in trees:
                self.check(first, second, first_nodes + second_nodes,
                           first_encoding == second_encoding)

    def test_missing_child_orientation_value_limits_and_long_chain(self):
        first_child, second_child = TreeNode(2), TreeNode(2)
        first, second = TreeNode(1, first_child), TreeNode(1, None, second_child)
        self.check(first, second, [first, second, first_child, second_child], False)
        first_nodes = [TreeNode(-10000) for _ in range(100)]
        second_nodes = [TreeNode(-10000) for _ in range(100)]
        for nodes in (first_nodes, second_nodes):
            for parent, child in zip(nodes, nodes[1:]):
                parent.right = child
        self.check(first_nodes[0], second_nodes[0], first_nodes + second_nodes, True)
        second_nodes[-1].val = 10000
        self.check(first_nodes[0], second_nodes[0], first_nodes + second_nodes, False)
        self.check(None, first_nodes[0], first_nodes, False)


if __name__ == '__main__':
    unittest.main()
