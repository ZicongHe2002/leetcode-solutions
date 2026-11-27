import random
import unittest
from itertools import permutations

from python import p0654_maximum_binary_tree as implementation


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


# LeetCode supplies this constructor when executing the Solution method.
implementation.TreeNode = TreeNode


def definition(values):
    if not values:
        return None
    index = values.index(max(values))
    return values[index], definition(values[:index]), definition(values[index + 1:])


def form(node):
    return None if node is None else (node.val, form(node.left), form(node.right))


class MaximumTreeTests(unittest.TestCase):
    def check(self, values, compare_definition=True):
        before = values[:]
        root = implementation.Solution().constructMaximumBinaryTree(values)
        self.assertEqual(values, before)
        pending, seen, labels = [root], set(), []
        while pending:
            node = pending.pop()
            if node is None:
                continue
            self.assertIsInstance(node, TreeNode)
            self.assertNotIn(id(node), seen)
            seen.add(id(node))
            labels.append(node.val)
            for child in (node.left, node.right):
                if child is not None:
                    self.assertGreater(node.val, child.val)
                    pending.append(child)
        self.assertEqual(sorted(labels), sorted(values))
        inorder, stack, current = [], [], root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            inorder.append(current.val)
            current = current.right
        self.assertEqual(inorder, values)
        if compare_definition:
            self.assertEqual(form(root), definition(values))

    def test_every_small_permutation_against_original_recursive_definition(self):
        checks = 0
        for length in range(1, 8):
            for values in permutations(range(length)):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 5913)

    def test_maximum_length_monotone_and_shuffled_unique_inputs(self):
        self.check(list(range(1, 1001)), compare_definition=False)
        self.check(list(range(1000, 0, -1)), compare_definition=False)
        values = list(range(1, 1001))
        random.Random(654).shuffle(values)
        self.check(values, compare_definition=False)
        self.check([])


if __name__ == '__main__':
    unittest.main()
