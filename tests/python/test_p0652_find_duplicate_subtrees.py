import unittest
from collections import Counter
from functools import lru_cache
from itertools import product

from python.p0652_find_duplicate_subtrees import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def tree_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in tree_shapes(left_size)
                 for right in tree_shapes(size - 1 - left_size))


def labeled(shape, values):
    if shape is None:
        return None
    value = next(values)
    return TreeNode(value, labeled(shape[0], values), labeled(shape[1], values))


def nodes_and_snapshot(root):
    pending, nodes = [root], []
    snapshot = {}
    while pending:
        node = pending.pop()
        if node is not None:
            nodes.append(node)
            snapshot[id(node)] = (node.val, id(node.left), id(node.right))
            pending.extend((node.left, node.right))
    return nodes, snapshot


def serialized(node):
    return None if node is None else (node.val, serialized(node.left), serialized(node.right))


def chain(size, value):
    root = None
    for _ in range(size):
        root = TreeNode(value, None, root)
    return root


def complete(height):
    return TreeNode(200, complete(height - 1), complete(height - 1)) if height else TreeNode(200)


class DuplicateSubtreeTests(unittest.TestCase):
    def checked(self, root):
        _, before = nodes_and_snapshot(root)
        result = Solution().findDuplicateSubtrees(root)
        self.assertIs(type(result), list)
        self.assertEqual(nodes_and_snapshot(root)[1], before)
        self.assertTrue(all(id(node) in before for node in result))
        self.assertEqual(len(result), len({id(node) for node in result}))
        return result

    def test_every_small_labeled_tree_against_full_nested_tuple_counts(self):
        checks = 0
        for size in range(7):
            for shape in tree_shapes(size):
                for values in product((-1, 1), repeat=size):
                    root = labeled(shape, iter(values))
                    nodes, _ = nodes_and_snapshot(root)
                    counts = Counter(serialized(node) for node in nodes)
                    expected = {key for key, count in counts.items() if count > 1}
                    actual = [serialized(node) for node in self.checked(root)]
                    self.assertEqual(len(actual), len(set(actual)))
                    self.assertEqual(set(actual), expected)
                    checks += 1
        self.assertEqual(checks, 10067)

    def test_maximum_depth_many_duplicate_types_and_complete_tree(self):
        self.assertEqual(self.checked(chain(5000, -200)), [])
        result = self.checked(complete(11))
        shape = None
        expected = set()
        for _ in range(11):
            shape = (200, shape, shape)
            expected.add(shape)
        self.assertEqual({serialized(node) for node in result}, expected)
        self.assertEqual(len(result), 11)
        root = TreeNode(0, chain(2499, 1), chain(2499, 1))
        result = self.checked(root)
        lengths = []
        for node in result:
            length = 0
            while node is not None:
                self.assertEqual(node.val, 1)
                self.assertIsNone(node.left)
                node = node.right
                length += 1
            lengths.append(length)
        self.assertEqual(sorted(lengths), list(range(1, 2500)))


if __name__ == '__main__':
    unittest.main()
