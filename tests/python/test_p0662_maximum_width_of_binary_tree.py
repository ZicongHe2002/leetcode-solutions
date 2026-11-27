from functools import lru_cache
import unittest

from python.p0662_maximum_width_of_binary_tree import Solution, TreeNode



@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in shapes(left_size) for right in shapes(size - 1 - left_size))


def materialize(shape, values):
    values = iter(values)

    def build(current):
        if current is None:
            return None
        node = TreeNode(next(values))
        node.left = build(current[0])
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



def expanded_null_level_width(root):
    level, best = [root], 0
    while any(node is not None for node in level):
        positions = [index for index, node in enumerate(level) if node is not None]
        best = max(best, positions[-1] - positions[0] + 1)
        following = []
        for node in level:
            following.extend((None, None) if node is None else (node.left, node.right))
        level = following
    return best


class TreeWidthExpandedLevelTests(unittest.TestCase):
    def check(self, root, expected=None):
        before = tree_records(root)
        if expected is None:
            expected = expanded_null_level_width(root)
        result = Solution().widthOfBinaryTree(root)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(tree_records(root), before)

    def test_all_small_shapes_against_complete_levels_with_nulls(self):
        checked = 0
        for size in range(1, 8):
            for shape in shapes(size):
                values = [(-100, 0, 100)[index % 3] for index in range(size)]
                self.check(materialize(shape, values))
                checked += 1
        self.assertEqual(checked, 625)

    def test_maximum_depth_full_level_and_largest_guaranteed_width(self):
        for direction in ('left', 'right'):
            root = current = TreeNode(0)
            for _ in range(2999):
                following = TreeNode(0)
                setattr(current, direction, following)
                current = following
            self.check(root, 1)
        nodes = [TreeNode(index % 201 - 100) for index in range(2047)]
        for index in range(1023):
            nodes[index].left = nodes[2 * index + 1]
            nodes[index].right = nodes[2 * index + 2]
        self.check(nodes[0], 1024)
        root = TreeNode(0)
        current = root
        for _ in range(31):
            current.left = TreeNode(0)
            current = current.left
        current = root
        for direction in ('right',) * 30 + ('left',):
            following = TreeNode(0)
            setattr(current, direction, following)
            current = following
        self.assertEqual(len(tree_records(root)), 63)
        self.check(root, 2**31 - 1)


if __name__ == '__main__':
    unittest.main()
