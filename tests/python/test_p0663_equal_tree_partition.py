import unittest
from functools import lru_cache
from itertools import product

from python.p0663_equal_tree_partition import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for count in range(size) for left in shapes(count)
                 for right in shapes(size - count - 1))


def labeled(shape, values):
    if shape is None:
        return None
    value = next(values)
    return TreeNode(value, labeled(shape[0], values), labeled(shape[1], values))


def snapshot(root):
    pending, result = [root], {}
    while pending:
        node = pending.pop()
        if node is not None:
            result[id(node)] = node.val, id(node.left), id(node.right)
            pending.extend((node.left, node.right))
    return result


def every_actual_edge(root):
    entries = snapshot(root)
    graph = {key: [] for key in entries}
    edges = []
    for parent, (_, left, right) in entries.items():
        for child in (left, right):
            if child in graph:
                edges.append((parent, child))
                graph[parent].append(child)
                graph[child].append(parent)
    total = sum(value for value, _, _ in entries.values())
    for first, second in edges:
        cut = frozenset((first, second))
        pending, visited = [first], {first}
        component = 0
        while pending:
            node = pending.pop()
            component += entries[node][0]
            for neighbor in graph[node]:
                if neighbor not in visited and frozenset((node, neighbor)) != cut:
                    visited.add(neighbor)
                    pending.append(neighbor)
        if component == total - component:
            return True
    return False


def chain(size, value):
    root = None
    for _ in range(size):
        root = TreeNode(value, root, None)
    return root


class EqualPartitionTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = snapshot(root)
        if expected is None:
            expected = every_actual_edge(root)
        actual = Solution().checkEqualTree(root)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected)
        self.assertEqual(snapshot(root), before)

    def test_every_small_signed_and_zero_tree_against_removed_edge_components(self):
        checked = 0
        for size in range(6):
            for shape in shapes(size):
                for values in product((-1, 0, 1), repeat=size):
                    self.check(labeled(shape, iter(values)))
                    checked += 1
        self.assertEqual(checked, 11497)

    def test_maximum_depth_large_sums_zero_root_and_real_cut_requirement(self):
        self.check(chain(10000, 100000), True)
        self.check(chain(10000, -100000), True)
        self.check(chain(10000, 0), True)
        self.check(chain(9999, 1), False)
        self.check(TreeNode(0), False)
        self.check(TreeNode(0, TreeNode(0)), True)
        self.check(TreeNode(0, TreeNode(1), TreeNode(-1)), False)
        self.check(TreeNode(-1), False)


if __name__ == '__main__':
    unittest.main()
