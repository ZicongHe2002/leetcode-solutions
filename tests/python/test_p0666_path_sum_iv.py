import unittest
from functools import lru_cache

from python.p0666_path_sum_iv import Solution


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right


@lru_cache(None)
def bounded_shapes(levels):
    if levels == 0:
        return (None,)
    return (None,) + tuple((left, right) for left in bounded_shapes(levels - 1)
                          for right in bounded_shapes(levels - 1))


def tree_and_encoding(shape, pattern, depth=1, position=1):
    if shape is None:
        return None, []
    value = 0 if pattern == 0 else 9 if pattern == 1 else (3 * depth + position) % 10
    left, first = tree_and_encoding(shape[0], pattern, depth + 1, 2 * position - 1)
    right, second = tree_and_encoding(shape[1], pattern, depth + 1, 2 * position)
    return TreeNode(value, left, right), [100 * depth + 10 * position + value, *first, *second]


def explicit_leaf_paths(root):
    total = 0
    pending = [(root, 0)]
    while pending:
        node, prefix = pending.pop()
        current = prefix + node.value
        if node.left is None and node.right is None:
            total += current
        else:
            if node.left is not None:
                pending.append((node.left, current))
            if node.right is not None:
                pending.append((node.right, current))
    return total


class EncodedPathTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        actual = Solution().pathSum(nums)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertEqual(nums, before)

    def test_every_bounded_tree_shape_with_three_value_patterns_against_real_trees(self):
        checked = 0
        for shape in bounded_shapes(4):
            if shape is None:
                continue
            for pattern in range(3):
                tree, nums = tree_and_encoding(shape, pattern)
                self.check(sorted(nums), explicit_leaf_paths(tree))
                checked += 1
        self.assertEqual(checked, 2028)

    def test_maximum_tree_rightmost_sparse_positions_and_zero_values(self):
        full = [100 * depth + 10 * position + 9 for depth in range(1, 5)
                for position in range(1, (1 << (depth - 1)) + 1)]
        self.assertEqual(len(full), 15)
        self.check(full, 288)
        self.check([119, 229, 349, 489], 36)
        self.check([113, 215, 221], 12)
        self.check([113, 221], 4)
        self.check([110], 0)
        self.check([119], 9)


if __name__ == '__main__':
    unittest.main()
