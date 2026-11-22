import unittest
from functools import lru_cache
from itertools import combinations

from python.p0236_lowest_common_ancestor_binary_tree import TreeNode, Solution


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right)
                 for left_size in range(size)
                 for left in shapes(left_size)
                 for right in shapes(size - 1 - left_size))


def build_tree(shape, values):
    remaining = iter(values)

    def build(current):
        if current is None:
            return None
        node = TreeNode(next(remaining))
        node.left = build(current[0])
        node.right = build(current[1])
        return node

    return build(shape)


def snapshot(root):
    records = []
    pending = [root] if root is not None else []
    while pending:
        node = pending.pop()
        records.append((node, node.val, node.left, node.right))
        if node.right is not None:
            pending.append(node.right)
        if node.left is not None:
            pending.append(node.left)
    return records


def assert_unchanged(test, records):
    for node, value, left, right in records:
        test.assertEqual(node.val, value)
        test.assertIs(node.left, left)
        test.assertIs(node.right, right)


def root_paths(root):
    result = {}
    pending = [(root, ())]
    while pending:
        node, prefix = pending.pop()
        path = prefix + (node,)
        result[node] = path
        if node.left is not None:
            pending.append((node.left, path))
        if node.right is not None:
            pending.append((node.right, path))
    return result


class LowestAncestorTests(unittest.TestCase):
    def check(self, root, p, q, expected):
        before = snapshot(root)
        self.assertIs(Solution().lowestCommonAncestor(root, p, q), expected)
        assert_unchanged(self, before)

    def test_all_small_shapes_and_node_pairs_against_common_path_prefix(self):
        trees = checks = 0
        for size in range(2, 7):
            for shape in shapes(size):
                root = build_tree(shape, range(size))
                paths = root_paths(root)
                trees += 1
                for p, q in combinations(paths, 2):
                    common = [left for left, right in zip(paths[p], paths[q]) if left is right]
                    expected = common[-1]
                    self.check(root, p, q, expected)
                    self.check(root, q, p, expected)
                    checks += 2
        self.assertEqual((trees, checks), (195, 5002))

    def test_maximum_chain_ancestor_query_and_value_extremes(self):
        nodes = [TreeNode(index) for index in range(100000)]
        for left, right in zip(nodes, nodes[1:]):
            left.right = right
        self.check(nodes[0], nodes[12345], nodes[-1], nodes[12345])
        self.check(nodes[0], nodes[-1], nodes[0], nodes[0])
        root = TreeNode(0, TreeNode(-(10**9)), TreeNode(10**9))
        self.check(root, root.left, root.right, root)


if __name__ == '__main__':
    unittest.main()
