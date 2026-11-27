from functools import lru_cache
import unittest

from python.p0450_delete_node_in_a_bst import TreeNode, Solution



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



class IterativeBSTDeletionTests(unittest.TestCase):
    def check(self, root, key):
        before = tree_records(root)
        values = inorder_values(root)
        result = Solution().deleteNode(root, key)
        after = tree_records(result)
        self.assertTrue(set(after).issubset(before))
        self.assertEqual(inorder_values(result), [value for value in values if value != key])
        self.assertEqual(len(after), len(before) - (key in values))
        if key not in values:
            self.assertIs(result, root)
            self.assertEqual(after, before)

    def test_all_small_bsts_existing_and_absent_keys(self):
        checks = 0
        for size in range(8):
            for shape in shapes(size):
                for key in range(-1, size + 1):
                    self.check(bst_from_shape(shape, range(size)), key)
                    checks += 1
        self.assertEqual(checks, 5333)

    def test_maximum_depth_root_middle_leaf_absent_and_value_limits(self):
        for descending in (False, True):
            for key in (0, 5000, 9999, -100000):
                values = iter(range(9999, -1, -1) if descending else range(10000))
                root = current = TreeNode(next(values))
                for value in values:
                    child = TreeNode(value)
                    if descending:
                        current.left = child
                    else:
                        current.right = child
                    current = child
                self.check(root, key)
        self.check(TreeNode(0, TreeNode(-100000), TreeNode(100000)), 0)


if __name__ == '__main__':
    unittest.main()
