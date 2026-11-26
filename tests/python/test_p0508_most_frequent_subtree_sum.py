from collections import Counter
from functools import lru_cache
from itertools import product
import unittest

from python.p0508_most_frequent_subtree_sum import Solution


class Node:
    def __init__(self, value, left=None, right=None):
        self.val, self.left, self.right = value, left, right


@lru_cache(None)
def binary_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for count in range(size) for left in binary_shapes(count)
                 for right in binary_shapes(size - count - 1))


def fill_preorder(shape, labels):
    if shape is None:
        return None
    value = next(labels)
    return Node(value, fill_preorder(shape[0], labels), fill_preorder(shape[1], labels))


def snapshot(root):
    pending = [root] if root is not None else []
    result = {}
    while pending:
        node = pending.pop()
        if id(node) in result:
            raise AssertionError('input must remain a proper tree')
        result[id(node)] = (node.val, id(node.left) if node.left is not None else None,
                            id(node.right) if node.right is not None else None)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return result


def independently_resummed_subtrees(root):
    roots = [root] if root is not None else []
    counts = Counter()
    while roots:
        current = roots.pop()
        pending, total = [current], 0
        while pending:
            node = pending.pop()
            total += node.val
            pending.extend(child for child in (node.left, node.right) if child is not None)
        counts[total] += 1
        roots.extend(child for child in (current.left, current.right) if child is not None)
    maximum = max(counts.values(), default=0)
    return {total for total, count in counts.items() if count == maximum}


def chain(size, value):
    root = None
    for _ in range(size):
        root = Node(value, left=root)
    return root


class SubtreeSumPostorderTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = snapshot(root)
        actual = Solution().findFrequentTreeSum(root)
        self.assertIs(type(actual), list)
        self.assertTrue(all(type(total) is int for total in actual))
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(set(actual), independently_resummed_subtrees(root) if expected is None else expected)
        self.assertEqual(snapshot(root), before)

    def test_all_small_shapes_and_signed_labels_against_fresh_subtree_traversals(self):
        trees = 0
        for size in range(6):
            for labels in product((-1, 0, 1), repeat=size):
                for shape in binary_shapes(size):
                    self.check(fill_preorder(shape, iter(labels)))
                    trees += 1
        self.assertEqual(trees, 11497)

    def test_ten_thousand_node_chains_zero_negative_and_maximum_value(self):
        self.check(chain(10000, 0), {0})
        self.check(chain(10000, 1), set(range(1, 10001)))
        self.check(chain(10000, -1), set(range(-10000, 0)))
        self.check(chain(10000, 100000), {100000 * count for count in range(1, 10001)})
        self.check(Node(5, Node(2), Node(-3)), {2, -3, 4})
        self.check(Node(5, Node(2), Node(-5)), {2})


if __name__ == '__main__':
    unittest.main()
