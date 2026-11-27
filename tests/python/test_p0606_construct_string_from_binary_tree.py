from functools import lru_cache
from itertools import product
import unittest

from python.p0606_construct_string_from_binary_tree import Solution


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for k in range(size)
                 for left in shapes(k) for right in shapes(size - 1 - k))


def materialize(shape, values):
    if shape is None:
        return None
    node = TreeNode(next(values))
    node.left = materialize(shape[0], values)
    node.right = materialize(shape[1], values)
    return node


def recursive_canonical(root):
    if root is None:
        return ''
    if root.left is None and root.right is None:
        return str(root.val)
    left = '(' + recursive_canonical(root.left) + ')'
    right = '' if root.right is None else '(' + recursive_canonical(root.right) + ')'
    return str(root.val) + left + right


def structure(root):
    return None if root is None else (root.val, structure(root.left), structure(root.right))


def parse_small(text):
    position = 0

    def element():
        nonlocal position
        if position >= len(text) or text[position] == ')':
            return None
        start = position
        if text[position] == '-':
            position += 1
        while position < len(text) and text[position].isdigit():
            position += 1
        value = int(text[start:position])
        children = []
        while position < len(text) and text[position] == '(':
            position += 1
            children.append(element())
            if position >= len(text) or text[position] != ')':
                raise ValueError('Missing child closing parenthesis')
            position += 1
        if len(children) > 2:
            raise ValueError('More than two children')
        children.extend([None] * (2 - len(children)))
        return value, children[0], children[1]

    result = element()
    if position != len(text):
        raise ValueError('Unconsumed output')
    return result


def snapshot(root):
    pending = [] if root is None else [root]
    records = {}
    while pending:
        node = pending.pop()
        records[node] = (node.val, node.left, node.right)
        pending.extend(child for child in (node.left, node.right) if child is not None)
    return records


class TreeParenthesesTests(unittest.TestCase):
    def check(self, root, expected):
        before = snapshot(root)
        result = Solution().tree2str(root)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(snapshot(root), before)
        return result

    def test_all_small_labeled_shapes_canonical_text_and_structural_roundtrip(self):
        cases = 0
        for size in range(6):
            for shape in shapes(size):
                for labels in product((-1, 0, 12), repeat=size):
                    root = materialize(shape, iter(labels))
                    result = self.check(root, recursive_canonical(root))
                    self.assertEqual(parse_small(result), structure(root))
                    cases += 1
        self.assertEqual(cases, 11497)

    def test_ten_thousand_depth_both_missing_child_cases_and_signed_values(self):
        left = right = None
        for _ in range(10000):
            left = TreeNode(1, left)
            right = TreeNode(-1000, None, right)
        self.check(left, '1(' * 9999 + '1' + ')' * 9999)
        self.check(right, '-1000()(' * 9999 + '-1000' + ')' * 9999)
        self.check(TreeNode(0), '0')
        self.check(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), '1(2(4))(3)')
        self.check(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)), '1(2()(4))(3)')


if __name__ == '__main__':
    unittest.main()
