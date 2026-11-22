import unittest

from python.p0222_count_complete_tree_nodes import TreeNode, Solution



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



def complete(size, repeated=False):
    nodes = [TreeNode(7 if repeated else index) for index in range(size)]
    for index, node in enumerate(nodes):
        if 2 * index + 1 < size:
            node.left = nodes[2 * index + 1]
        if 2 * index + 2 < size:
            node.right = nodes[2 * index + 2]
    return nodes[0] if nodes else None


class CompleteTreeCountTests(unittest.TestCase):
    def check(self, root):
        before = tree_records(root)
        result = Solution().countNodes(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, len(before))
        self.assertEqual(tree_records(root), before)

    def test_every_small_complete_tree_size_against_full_scan(self):
        for size in range(1024):
            self.check(complete(size))

    def test_maximum_size_level_boundaries_duplicate_and_value_limits(self):
        self.check(complete(50000))
        self.check(complete(50000, repeated=True))
        for height in range(1, 16):
            for size in (2**height - 2, 2**height - 1, 2**height):
                self.check(complete(size))
        self.check(TreeNode(50000))


if __name__ == '__main__':
    unittest.main()
