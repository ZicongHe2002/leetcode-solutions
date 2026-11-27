from collections import deque
from functools import lru_cache
import unittest

from python.p0449_serialize_and_deserialize_bst import Codec, TreeNode


@lru_cache(None)
def binary_shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in binary_shapes(left_size) for right in binary_shapes(size - 1 - left_size))


def bst_from_shape(shape, size):
    labels = iter(range(size))
    def build(current):
        if current is None:
            return None
        left = build(current[0])
        root = TreeNode(next(labels), left)
        root.right = build(current[1])
        return root
    return build(shape)


def breadth_tree_facts(root):
    queue = deque([root])
    tokens, identities, links = [], set(), []
    while queue:
        node = queue.popleft()
        if node is None:
            tokens.append(None)
            continue
        if id(node) in identities:
            raise AssertionError('tree contains a cycle or shared node')
        identities.add(id(node))
        tokens.append(node.val)
        links.append((id(node), node.val, id(node.left) if node.left is not None else None,
                      id(node.right) if node.right is not None else None))
        queue.extend((node.left, node.right))
    return tuple(tokens), frozenset(identities), tuple(links)


class BstCodecStructuralRoundtripTests(unittest.TestCase):
    def check(self, root, codec=None):
        codec = Codec() if codec is None else codec
        before = breadth_tree_facts(root)
        text = codec.serialize(root)
        self.assertIs(type(text), str)
        restored = codec.deserialize(text)
        after = breadth_tree_facts(restored)
        self.assertEqual(after[0], before[0])
        self.assertFalse(after[1] & before[1])
        self.assertEqual(breadth_tree_facts(root), before)
        self.assertEqual(codec.serialize(restored), text)

    def test_every_small_bst_shape_with_independent_breadth_signature(self):
        trees = 0
        for size in range(9):
            for shape in binary_shapes(size):
                self.check(bst_from_shape(shape, size))
                trees += 1
        self.assertEqual(trees, 2056)

    def test_maximum_nodes_skew_directions_value_bounds_and_reuse(self):
        codec = Codec()
        self.assertEqual(codec.serialize(None), '')
        self.assertIsNone(codec.deserialize(''))
        self.check(TreeNode(0), codec)
        self.check(TreeNode(10000), codec)
        left = None
        for value in range(10000):
            left = TreeNode(value, left)
        self.check(left, codec)
        right = None
        for value in range(9999, -1, -1):
            right = TreeNode(value, None, right)
        self.check(right, codec)
        self.check(None, codec)


if __name__ == '__main__':
    unittest.main()
