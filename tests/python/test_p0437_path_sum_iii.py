import unittest
from functools import lru_cache
from itertools import product

from python.p0437_path_sum_iii import TreeNode, Solution


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


def all_start_downward_count(records, target):
    answer = 0
    for start, _, _, _ in records:
        pending = [(start, 0)]
        while pending:
            node, total = pending.pop()
            total += node.val
            answer += total == target
            if node.left is not None:
                pending.append((node.left, total))
            if node.right is not None:
                pending.append((node.right, total))
    return answer


class PathSumThreeTests(unittest.TestCase):
    def check(self, root, target):
        before = snapshot(root)
        expected = all_start_downward_count(before, target)
        result = Solution().pathSum(root, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        assert_unchanged(self, before)
        return result

    def test_all_small_shapes_values_and_targets_against_all_start_walks(self):
        trees = checks = 0
        for size in range(6):
            for shape in shapes(size):
                for values in product(range(-1, 2), repeat=size):
                    root = build_tree(shape, values)
                    trees += 1
                    for target in range(-2, 3):
                        self.check(root, target)
                        checks += 1
        self.assertEqual((trees, checks), (11497, 57485))

    def test_maximum_chains_zero_paths_and_sibling_prefix_rollback(self):
        zero = TreeNode(0)
        current = zero
        for _ in range(999):
            current.left = TreeNode(0)
            current = current.left
        self.assertEqual(self.check(zero, 0), 500500)
        alternating = TreeNode(10**9)
        current = alternating
        for index in range(1, 1000):
            current.right = TreeNode(-(10**9) if index % 2 else 10**9)
            current = current.right
        self.check(alternating, 0)
        self.check(alternating, 1000)
        self.check(TreeNode(1, TreeNode(-1), TreeNode(-1)), 0)
        self.check(TreeNode(1000, TreeNode(-1000), TreeNode(0)), -1000)
        self.check(None, 0)


if __name__ == '__main__':
    unittest.main()
