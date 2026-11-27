from functools import lru_cache
import unittest

from python.p0173_binary_search_tree_iterator import BSTIterator, TreeNode



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



class LazyBSTIteratorTests(unittest.TestCase):
    def check_complete_iteration(self, root, expected):
        before = tree_records(root)
        iterator = BSTIterator(root)
        actual = []
        for value in expected:
            for _ in range(2):
                result = iterator.hasNext()
                self.assertIs(type(result), bool)
                self.assertTrue(result)
            result = iterator.next()
            self.assertIs(type(result), int)
            self.assertEqual(result, value)
            actual.append(result)
        self.assertIs(iterator.hasNext(), False)
        self.assertEqual(actual, expected)
        self.assertEqual(tree_records(root), before)

    def test_all_small_bst_shapes_and_repeated_has_next(self):
        checks = 0
        for size in range(1, 8):
            for shape in shapes(size):
                self.check_complete_iteration(bst_from_shape(shape, range(size)), list(range(size)))
                checks += 1
        self.assertEqual(checks, 625)

    def test_maximum_nodes_height_and_exact_100000_call_prefix(self):
        for descending in (False, True):
            values = range(99999, -1, -1) if descending else range(100000)
            values = iter(values)
            root = current = TreeNode(next(values))
            for value in values:
                child = TreeNode(value)
                if descending:
                    current.left = child
                else:
                    current.right = child
                current = child
            before = tree_records(root)
            iterator = BSTIterator(root)
            calls = 0
            for expected in range(50000):
                self.assertIs(iterator.hasNext(), True)
                calls += 1
                self.assertEqual(iterator.next(), expected)
                calls += 1
            self.assertEqual(calls, 100000)
            self.assertEqual(tree_records(root), before)
        self.check_complete_iteration(TreeNode(10**6), [10**6])


if __name__ == '__main__':
    unittest.main()
