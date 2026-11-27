from functools import lru_cache
import unittest

from python.p0429_n_ary_tree_level_order_traversal import Node, Solution


@lru_cache(None)
def ordered_forests(size):
    if size == 0:
        return ((),)
    return tuple((first, *rest) for first_size in range(1, size + 1)
                 for first in ordered_trees(first_size) for rest in ordered_forests(size - first_size))


@lru_cache(None)
def ordered_trees(size):
    return ordered_forests(size - 1)


def labeled_tree(shape):
    labels = iter(range(10000))
    def build(children):
        node = Node(next(labels))
        node.children = [build(child) for child in children]
        return node
    return build(shape)


def depth_first_group_oracle(root):
    levels = []
    def visit(node, depth):
        if len(levels) == depth:
            levels.append([])
        levels[depth].append(node.val)
        for child in node.children or []:
            visit(child, depth + 1)
    if root is not None:
        visit(root, 0)
    return levels


def graph_snapshot(root):
    pending = [] if root is None else [root]
    result = []
    while pending:
        node = pending.pop()
        children = None if node.children is None else tuple(id(child) for child in node.children)
        result.append((id(node), node.val, children))
        pending.extend(reversed(node.children or []))
    return result


class NaryLevelBoundaryTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = graph_snapshot(root)
        expected = depth_first_group_oracle(root) if expected is None else expected
        actual = Solution().levelOrder(root)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, expected)
        self.assertEqual(graph_snapshot(root), before)

    def test_all_small_ordered_rooted_tree_shapes(self):
        trees = 1
        self.check(None)
        for size in range(1, 9):
            for shape in ordered_trees(size):
                self.check(labeled_tree(shape))
                trees += 1
        self.assertEqual(trees, 627)

    def test_maximum_nodes_depth_and_external_none_children(self):
        self.check(Node(0, [Node(value) for value in range(1, 10000)]), [[0], list(range(1, 10000))])
        root = None
        for value in range(999, -1, -1):
            root = Node(value, [] if root is None else [root])
        self.check(root, [[value] for value in range(1000)])
        external = Node(5)
        external.children = None
        self.check(external, [[5]])


if __name__ == '__main__':
    unittest.main()
