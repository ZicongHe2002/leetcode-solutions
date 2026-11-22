import unittest
from functools import lru_cache
from itertools import product

from python.p0114_flatten_binary_tree_linked_list import TreeNode, Solution


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


class FlattenTests(unittest.TestCase):
    def check(self, root):
        before = snapshot(root)
        self.assertIsNone(Solution().flatten(root))
        current = root
        for node, value, _, _ in before:
            self.assertIs(current, node)
            self.assertIsNone(node.left)
            self.assertEqual(node.val, value)
            current = node.right
        self.assertIsNone(current)

    def test_all_small_shapes_and_values_against_original_preorder_identities(self):
        checks = 0
        for size in range(7):
            for shape in shapes(size):
                for values in product((-1, 1), repeat=size):
                    self.check(build_tree(shape, values))
                    checks += 1
        self.assertEqual(checks, 10067)

    def test_maximum_chains_comb_and_terminal_links(self):
        for direction in ['left', 'right']:
            root = TreeNode(-100)
            current = root
            for _ in range(1999):
                child = TreeNode(100)
                setattr(current, direction, child)
                current = child
            self.check(root)
        root = TreeNode(0)
        current = root
        for _ in range(999):
            current.left = TreeNode(-100)
            current.right = TreeNode(100)
            current = current.left
        self.check(root)
        self.check(None)


if __name__ == '__main__':
    unittest.main()
