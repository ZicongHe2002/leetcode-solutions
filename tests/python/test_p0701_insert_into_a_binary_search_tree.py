from functools import lru_cache
import unittest

from python.p0701_insert_into_a_binary_search_tree import TreeNode, Solution



@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in shapes(left_size) for right in shapes(size - 1 - left_size))



def bst_from_shape(shape, values):
    values = iter(values)

    def build(current):
        if current is None:
            return None
        left = build(current[0])
        node = TreeNode(next(values))
        node.left = left
        node.right = build(current[1])
        return node

    return build(shape)



def tree_records(root):
    records = {}
    pending = [root] if root is not None else []
    while pending:
        node = pending.pop()
        if node in records:
            raise AssertionError('cycle or shared input node')
        records[node] = (node.val, node.left, node.right)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return records



def inorder_values(root):
    result, stack = [], []
    current = root
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result



class IterativeBSTInsertionTests(unittest.TestCase):
    def check(self, root, value):
        before = tree_records(root)
        values = inorder_values(root)
        self.assertNotIn(value, values)
        result = Solution().insertIntoBST(root, value)
        after = tree_records(result)
        self.assertTrue(set(before).issubset(after))
        self.assertEqual(len(set(after) - set(before)), 1)
        self.assertEqual(inorder_values(result), sorted(values + [value]))
        for node in before:
            self.assertEqual(node.val, before[node][0])
        if root is not None:
            self.assertIs(result, root)

    def test_all_small_bsts_and_every_rank_gap(self):
        checks = 0
        for size in range(8):
            for shape in shapes(size):
                for gap in range(size + 1):
                    self.check(bst_from_shape(shape, range(0, 2 * size, 2)), 2 * gap - 1)
                    checks += 1
        self.assertEqual(checks, 4707)

    def test_maximum_input_size_deep_insertions_empty_and_value_limits(self):
        for descending in (False, True):
            root = current = TreeNode(0)
            for index in range(1, 10000):
                child = TreeNode(-index if descending else index)
                if descending:
                    current.left = child
                else:
                    current.right = child
                current = child
            self.check(root, -10000 if descending else 10000)
        self.check(None, -10**8)
        self.check(TreeNode(0), 10**8)
        self.check(TreeNode(0, TreeNode(-10**8)), 10**8)


if __name__ == '__main__':
    unittest.main()
