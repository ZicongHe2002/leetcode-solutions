import unittest
from functools import lru_cache
from itertools import combinations

from python.p0653_two_sum_iv_input_is_a_bst import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for count in range(size) for left in shapes(count)
                 for right in shapes(size - count - 1))


def inorder_labeled(shape, values):
    if shape is None:
        return None
    left = inorder_labeled(shape[0], values)
    value = next(values)
    return TreeNode(value, left, inorder_labeled(shape[1], values))


def snapshot(root):
    result = {}
    pending = [root]
    while pending:
        node = pending.pop()
        if node is not None:
            result[id(node)] = node.val, id(node.left), id(node.right)
            pending.extend((node.left, node.right))
    return result


class BstPairTests(unittest.TestCase):
    def check(self, root, target, expected=None):
        before = snapshot(root)
        if expected is None:
            values = [entry[0] for entry in before.values()]
            expected = any(a + b == target for a, b in combinations(values, 2))
        actual = Solution().findTarget(root, target)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected, target)
        self.assertEqual(snapshot(root), before)

    def test_every_small_bst_and_target_against_distinct_index_pairs(self):
        trees = queries = 0
        for size in range(1, 6):
            for values in combinations((-4, -1, 0, 2, 5), size):
                for shape in shapes(size):
                    root = inorder_labeled(shape, iter(values))
                    trees += 1
                    for target in range(-10, 12):
                        self.check(root, target)
                        queries += 1
        self.assertEqual((trees, queries), (187, 4114))

    def test_maximum_chains_extreme_targets_and_no_self_pair(self):
        positive = None
        for value in reversed(range(10000)):
            positive = TreeNode(value, None, positive)
        self.check(positive, 19997, True)
        self.check(positive, 100000, False)
        self.check(positive, -100000, False)
        negative = None
        for value in range(-10000, 0):
            negative = TreeNode(value, negative, None)
        self.check(negative, -19999, True)
        self.check(negative, -20000, False)
        self.check(TreeNode(10000), 20000, False)
        self.check(TreeNode(0), 0, False)
        self.check(None, 0, False)


if __name__ == '__main__':
    unittest.main()
