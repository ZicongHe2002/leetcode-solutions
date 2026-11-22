import unittest
from functools import lru_cache

from python.p0230_kth_smallest_element_bst import TreeNode, Solution


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right)
                 for left_size in range(size)
                 for left in shapes(left_size)
                 for right in shapes(size - 1 - left_size))


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


def build_search_tree(shape):
    next_value = 0

    def build(current):
        nonlocal next_value
        if current is None:
            return None
        left = build(current[0])
        node = TreeNode(next_value, left)
        next_value += 1
        node.right = build(current[1])
        return node

    return build(shape)


class KthSmallestTests(unittest.TestCase):
    def check(self, root, k):
        before = snapshot(root)
        expected = sorted(record[1] for record in before)[k - 1]
        self.assertEqual(Solution().kthSmallest(root, k), expected)
        assert_unchanged(self, before)

    def test_all_small_search_tree_shapes_and_ranks_against_global_sort(self):
        trees = checks = 0
        for size in range(1, 7):
            for shape in shapes(size):
                trees += 1
                root = build_search_tree(shape)
                for k in range(1, size + 1):
                    self.check(root, k)
                    checks += 1
        self.assertEqual((trees, checks), (196, 1078))

    def test_deep_chains_and_maximum_contract_without_recursion(self):
        right = TreeNode(0)
        current = right
        for value in range(1, 10000):
            current.right = TreeNode(value)
            current = current.right
        left = TreeNode(10000)
        current = left
        for value in range(9999, 0, -1):
            current.left = TreeNode(value)
            current = current.left
        for root in [right, left]:
            for k in [1, 5000, 10000]:
                self.check(root, k)
        self.check(TreeNode(0), 1)


if __name__ == '__main__':
    unittest.main()
