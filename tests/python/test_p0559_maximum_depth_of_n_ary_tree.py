from functools import lru_cache
from itertools import count
import unittest

from python.p0559_maximum_depth_of_n_ary_tree import Solution


class Node:
    def __init__(self, val, children=None):
        self.val, self.children = val, children


@lru_cache(None)
def ordered_forests(total):
    if total == 0:
        return ((),)
    return tuple((first,) + remainder for size in range(1, total + 1)
                 for first in ordered_tree_shapes(size)
                 for remainder in ordered_forests(total - size))


@lru_cache(None)
def ordered_tree_shapes(size):
    return ordered_forests(size - 1)


def materialize(shape, labels):
    return Node(next(labels), [materialize(child, labels) for child in shape])


def recursive_definition_oracle(root):
    if root is None:
        return 0
    return 1 + max((recursive_definition_oracle(child) for child in (root.children or ())), default=0)


def snapshot(root):
    pending = [] if root is None else [root]
    records = {}
    while pending:
        node = pending.pop()
        if id(node) in records:
            raise AssertionError('Repeated node or cycle')
        children = node.children
        records[id(node)] = (node.val, id(children), None if children is None else tuple(map(id, children)))
        pending.extend(children or ())
    return records


class NaryLevelDepthTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = snapshot(root)
        actual = Solution().maxDepth(root)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, recursive_definition_oracle(root) if expected is None else expected)
        self.assertEqual(snapshot(root), before)

    def test_every_small_ordered_nary_shape_against_recursive_definition(self):
        trees = 0
        for size in range(1, 9):
            for shape in ordered_tree_shapes(size):
                self.check(materialize(shape, count()))
                trees += 1
        self.assertEqual(trees, 626)

    def test_maximum_node_count_depth_empty_and_nullable_leaf_children(self):
        wide = Node(0, [Node(value, []) for value in range(1, 10000)])
        self.assertEqual(len(snapshot(wide)), 10000)
        self.check(wide, 2)
        root = Node(0, [])
        node = root
        for value in range(1, 1000):
            child = Node(value, [])
            node.children.append(child)
            node = child
        self.assertEqual(len(snapshot(root)), 1000)
        self.check(root, 1000)
        self.check(None, 0)
        self.check(Node(7), 1)
        self.check(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]), 3)


if __name__ == '__main__':
    unittest.main()
