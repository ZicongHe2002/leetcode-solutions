from functools import lru_cache
import unittest

from python.p0510_inorder_successor_in_bst_ii import Solution


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.val, self.left, self.right, self.parent = value, left, right, parent


@lru_cache(None)
def binary_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for count in range(size) for left in binary_shapes(count)
                 for right in binary_shapes(size - count - 1))


def fill_bst(shape, values):
    if shape is None:
        return None
    left = fill_bst(shape[0], values)
    node = Node(next(values), left=left)
    if left is not None:
        left.parent = node
    node.right = fill_bst(shape[1], values)
    if node.right is not None:
        node.right.parent = node
    return node


def full_inorder_nodes(root):
    result, pending, current = [], [], root
    while current is not None or pending:
        while current is not None:
            pending.append(current)
            current = current.left
        current = pending.pop()
        result.append(current)
        current = current.right
    return result


def structural_snapshot(root):
    if root is not None and root.parent is not None:
        raise AssertionError('root parent must remain None')
    result, pending = {}, [root] if root is not None else []
    while pending:
        node = pending.pop()
        if id(node) in result:
            raise AssertionError('children must remain a proper tree')
        result[id(node)] = (node.val, id(node.left) if node.left is not None else None,
                            id(node.right) if node.right is not None else None,
                            id(node.parent) if node.parent is not None else None)
        for child in (node.left, node.right):
            if child is not None:
                if child.parent is not node:
                    raise AssertionError('parent and child links must agree')
                pending.append(child)
    return result


class ParentLinkSuccessorTests(unittest.TestCase):
    def check(self, root, node, expected):
        before = structural_snapshot(root)
        self.assertIs(Solution().inorderSuccessor(node), expected)
        self.assertEqual(structural_snapshot(root), before)

    def test_all_small_bst_shapes_and_every_node_against_full_inorder_identity(self):
        trees = queries = 0
        for size in range(1, 8):
            for shape in binary_shapes(size):
                root = fill_bst(shape, iter(range(size)))
                nodes = full_inorder_nodes(root)
                trees += 1
                for index, node in enumerate(nodes):
                    self.check(root, node, nodes[index + 1] if index + 1 < size else None)
                    queries += 1
        self.assertEqual((trees, queries), (625, 4081))

    def test_ten_thousand_node_upward_and_downward_chains_bounds_and_empty_extension(self):
        nodes = [Node(value) for value in range(-5000, 5000)]
        for left, right in zip(nodes, nodes[1:]):
            left.right, right.parent = right, left
        for index in (0, 1, 4999, 9998, 9999):
            self.check(nodes[0], nodes[index], nodes[index + 1] if index + 1 < len(nodes) else None)
        root = Node(-100000)
        nodes = [Node(value) for value in range(1, 10000)]
        for left, right in zip(nodes, nodes[1:]):
            right.left, left.parent = left, right
        root.right, nodes[-1].parent = nodes[-1], root
        self.check(root, root, nodes[0])
        self.check(root, nodes[0], nodes[1])
        self.check(root, nodes[-1], None)
        root = Node(-100000)
        root.right = Node(100000, parent=root)
        self.check(root, root, root.right)
        self.check(root, root.right, None)
        self.check(None, None, None)


if __name__ == '__main__':
    unittest.main()
