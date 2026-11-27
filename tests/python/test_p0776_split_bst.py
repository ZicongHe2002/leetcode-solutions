import unittest
from functools import cache

from python.p0776_split_bst import Solution


class TreeNode:
    def __init__(self, value):
        self.val, self.left, self.right = value, None, None


@cache
def all_shapes(size):
    if not size:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in all_shapes(left_size) for right in all_shapes(size - left_size - 1))


def from_shape(shape, values):
    if shape is None:
        return None
    left = from_shape(shape[0], values)
    root = TreeNode(next(values))
    root.left, root.right = left, from_shape(shape[1], values)
    return root


def insertion_tree(values):
    root = None
    for value in values:
        if root is None:
            root = TreeNode(value)
            continue
        node = root
        while True:
            side = 'left' if value < node.val else 'right'
            child = getattr(node, side)
            if child is None:
                setattr(node, side, TreeNode(value))
                break
            node = child
    return root


def preorder_nodes(root):
    stack, nodes = [root] if root else [], []
    while stack:
        node = stack.pop()
        nodes.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return nodes


def edges(root):
    return {node.val: (node.left.val if node.left else None, node.right.val if node.right else None)
            for node in preorder_nodes(root)}


class SplitBSTTests(unittest.TestCase):
    def check(self, root, target):
        original = preorder_nodes(root)
        nodes = {node.val: node for node in original}
        before_edges = edges(root)
        order = [node.val for node in original]
        expected = [insertion_tree(value for value in order if (value <= target) == small) for small in (True,False)]
        result = Solution().splitBST(root, target)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), 2)
        seen = set()
        for actual, wanted, small in zip(result, expected, (True,False)):
            stack = [actual] if actual else []
            while stack:
                node = stack.pop()
                self.assertNotIn(id(node), seen)
                seen.add(id(node))
                self.assertIs(node, nodes[node.val])
                self.assertEqual(node.val <= target, small)
                stack.extend(child for child in (node.left, node.right) if child)
            self.assertEqual(actual.val if actual else None, wanted.val if wanted else None)
            self.assertEqual(edges(actual), edges(wanted))
        self.assertEqual(seen, {id(node) for node in original})
        for value, (left, right) in before_edges.items():
            self.assertEqual(nodes[value].val, value)
            for side, child in (('left',left),('right',right)):
                if child is not None and (value <= target) == (child <= target):
                    self.assertIs(getattr(nodes[value], side), nodes[child])

    def test_all_small_bst_shapes_and_thresholds_against_filtered_preorder_reconstruction(self):
        shape_count = checked = 0
        for size in range(1, 8):
            for shape in all_shapes(size):
                shape_count += 1
                for target in range(2 * size + 2):
                    self.check(from_shape(shape, iter(range(1, 2 * size, 2))), target)
                    checked += 1
        self.assertEqual((shape_count, checked), (625, 9412))

    def test_official_examples_maximum_chains_value_bounds_and_separate_empty_extension(self):
        self.check(insertion_tree([4,2,6,1,3,5,7]), 2)
        self.check(insertion_tree([1]), 1)
        self.check(insertion_tree([0]), 0)
        for values in (list(range(0,1000,20)), list(reversed(range(0,1000,20)))):
            for target in (0,499,500,1000):
                self.check(insertion_tree(values), target)
        self.check(None, 0)  # Empty-root extension beyond the original node-count minimum.


if __name__ == '__main__':
    unittest.main()
