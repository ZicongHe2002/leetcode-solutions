from functools import lru_cache
from itertools import count, cycle
import unittest

from python.p0590_n_ary_tree_postorder_traversal import Solution


class Node:
    def __init__(self, val, children=None):
        self.val, self.children = val, children


@lru_cache(None)
def forests(total):
    if total == 0:
        return ((),)
    return tuple((first,) + rest for size in range(1, total + 1)
                 for first in shapes(size) for rest in forests(total - size))


@lru_cache(None)
def shapes(size):
    return forests(size - 1)


def materialize(shape, values):
    node = Node(next(values))
    node.children = [materialize(child, values) for child in shape]
    return node


def recursive_definition(root):
    if root is None:
        return []
    return [value for child in (root.children or ()) for value in recursive_definition(child)] + [root.val]


def snapshot(root):
    pending = [] if root is None else [root]
    records = {}
    while pending:
        node = pending.pop()
        records[node] = (node.val, id(node.children), tuple(node.children or ()))
        pending.extend(node.children or ())
    return records


class NaryPostorderTests(unittest.TestCase):
    def check(self, root, expected):
        before = snapshot(root)
        result = Solution().postorder(root)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, expected)
        self.assertEqual(snapshot(root), before)

    def test_all_ordered_small_shapes_unique_and_repeated_values(self):
        cases = 0
        for size in range(1, 9):
            for shape in shapes(size):
                for labels in (count(), cycle((0, 10000))):
                    root = materialize(shape, labels)
                    self.check(root, recursive_definition(root))
                    cases += 1
        self.assertEqual(cases, 1252)

    def test_maximum_width_height_empty_and_nullable_leaf(self):
        self.check(Node(10000, [Node(value, []) for value in range(9999)]), list(range(9999)) + [10000])
        root = None
        for value in reversed(range(1000)):
            root = Node(value, [] if root is None else [root])
        self.check(root, list(reversed(range(1000))))
        self.check(None, [])
        self.check(Node(0), [0])
        root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        self.check(root, [5, 6, 3, 2, 4, 1])


if __name__ == '__main__':
    unittest.main()
