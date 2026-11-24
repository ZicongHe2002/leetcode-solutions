import unittest
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import isclose

from python.p0637_average_of_levels_binary_tree import TreeNode, Solution


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right)
                 for left_size in range(size)
                 for left in shapes(left_size)
                 for right in shapes(size - 1 - left_size))


def build_tree(shape, values):
    remaining = iter(values)

    def build(current):
        if current is None:
            return None
        node = TreeNode(next(remaining))
        node.left = build(current[0])
        node.right = build(current[1])
        return node

    return build(shape)


def snapshot(root):
    records = []
    pending = [root] if root is not None else []
    while pending:
        node = pending.pop()
        records.append((node, node.val, node.left, node.right))
        if node.right is not None:
            pending.append(node.right)
        if node.left is not None:
            pending.append(node.left)
    return records


def assert_unchanged(test, records):
    for node, value, left, right in records:
        test.assertEqual(node.val, value)
        test.assertIs(node.left, left)
        test.assertIs(node.right, right)


class AverageLevelsTests(unittest.TestCase):
    def check(self, root):
        before = snapshot(root)
        layers = []
        pending = [(root, 0)] if root is not None else []
        while pending:
            node, depth = pending.pop()
            if depth == len(layers):
                layers.append([])
            layers[depth].append(node.val)
            if node.right is not None:
                pending.append((node.right, depth + 1))
            if node.left is not None:
                pending.append((node.left, depth + 1))
        expected = [float(Fraction(sum(layer), len(layer))) for layer in layers]
        result = Solution().averageOfLevels(root)
        self.assertEqual(len(result), len(expected))
        for actual, wanted in zip(result, expected):
            self.assertIs(type(actual), float)
            self.assertTrue(isclose(actual, wanted, rel_tol=1e-12, abs_tol=1e-12))
        assert_unchanged(self, before)

    def test_all_small_shapes_and_extreme_values_against_exact_fractions(self):
        checks = 0
        for size in range(7):
            for shape in shapes(size):
                for values in product((-(2**31), 2**31 - 1), repeat=size):
                    self.check(build_tree(shape, values))
                    checks += 1
        self.assertEqual(checks, 10067)

    def test_maximum_depth_width_cancellation_and_empty_extension(self):
        values = [-(2**31) if index % 2 else 2**31 - 1 for index in range(10000)]
        root = TreeNode(values[0])
        current = root
        for value in values[1:]:
            current.left = TreeNode(value)
            current = current.left
        self.check(root)
        nodes = [TreeNode(value) for value in values]
        for index in range(10000):
            if 2 * index + 1 < 10000:
                nodes[index].left = nodes[2 * index + 1]
            if 2 * index + 2 < 10000:
                nodes[index].right = nodes[2 * index + 2]
        self.check(nodes[0])
        self.check(TreeNode(1, TreeNode(-(2**31)), TreeNode(2**31 - 1)))
        self.check(None)


if __name__ == '__main__':
    unittest.main()
