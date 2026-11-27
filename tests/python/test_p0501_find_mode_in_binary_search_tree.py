from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
import unittest

from python.p0501_find_mode_in_binary_search_tree import Solution


class Node:
    def __init__(self, value, left=None, right=None):
        self.val, self.left, self.right = value, left, right


@lru_cache(None)
def binary_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in binary_shapes(left_size) for right in binary_shapes(size - left_size - 1))


def fill_inorder(shape, values):
    if shape is None:
        return None
    left = fill_inorder(shape[0], values)
    value = next(values)
    return Node(value, left, fill_inorder(shape[1], values))


def node_identity_snapshot(root):
    pending = [root] if root is not None else []
    snapshot = {}
    while pending:
        node = pending.pop()
        if id(node) in snapshot:
            raise AssertionError('a proper tree cannot contain a cycle or shared child')
        snapshot[id(node)] = (node.val, id(node.left) if node.left is not None else None,
                              id(node.right) if node.right is not None else None)
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return snapshot


def right_chain(values):
    root = None
    for value in reversed(values):
        root = Node(value, right=root)
    return root


class MorrisModeRestorationTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = node_identity_snapshot(root)
        counts = Counter(record[0] for record in before.values())
        maximum = max(counts.values(), default=0)
        reference = sorted(value for value, count in counts.items() if count == maximum)
        actual = Solution().findMode(root)
        self.assertIs(type(actual), list)
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(sorted(actual), reference if expected is None else expected)
        self.assertEqual(node_identity_snapshot(root), before)

    def test_all_small_shapes_and_sorted_value_multisets_against_node_frequencies(self):
        trees = 0
        for size in range(7):
            for values in combinations_with_replacement((-1, 0, 1), size):
                for shape in binary_shapes(size):
                    self.check(fill_inorder(shape, iter(values)))
                    trees += 1
        self.assertEqual(trees, 4854)

    def test_ten_thousand_node_chains_value_limits_and_late_larger_frequency(self):
        values = list(range(-5000, 5000))
        self.check(right_chain(values), values)
        root = None
        for _ in range(10000):
            root = Node(100000, left=root)
        self.check(root, [100000])
        self.check(right_chain([-100000] * 5000 + [100000] * 5000), [-100000, 100000])
        self.check(right_chain(list(range(5000)) + [100000] * 5000), [100000])


if __name__ == '__main__':
    unittest.main()
