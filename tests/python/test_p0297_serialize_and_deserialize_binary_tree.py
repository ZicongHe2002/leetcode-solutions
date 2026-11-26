from collections import deque
from functools import lru_cache
from itertools import product
import unittest

from python.p0297_serialize_and_deserialize_binary_tree import Codec, TreeNode


@lru_cache(None)
def shapes(size):
    if size == 0:
        return (None,)
    return tuple((left, right) for left_size in range(size)
                 for left in shapes(left_size) for right in shapes(size - 1 - left_size))


def build_shape(shape, values):
    source = iter(values)
    def build(current):
        if current is None:
            return None
        return TreeNode(next(source), build(current[0]), build(current[1]))
    return build(shape)


def level_signature(root):
    pending = deque([root])
    signature = []
    identities = set()
    while pending:
        node = pending.popleft()
        if node is None:
            signature.append(None)
        else:
            if id(node) in identities:
                raise AssertionError('cycle or shared child')
            identities.add(id(node))
            signature.append(node.val)
            pending.extend((node.left, node.right))
    return signature, identities


class CodecNullSlotTests(unittest.TestCase):
    def check(self, root):
        expected, original_ids = level_signature(root)
        data = Codec().serialize(root)
        self.assertIs(type(data), str)
        self.assertEqual(len(data.split(',')), 2 * len(original_ids) + 1)
        decoded = Codec().deserialize(data)
        actual, decoded_ids = level_signature(decoded)
        self.assertEqual(actual, expected)
        self.assertTrue(original_ids.isdisjoint(decoded_ids))
        self.assertEqual(level_signature(root), (expected, original_ids))
        self.assertEqual(Codec().serialize(decoded), data)

    def test_all_small_shapes_and_labels_against_level_order_structure(self):
        trees = 0
        for size in range(6):
            for shape in shapes(size):
                for values in product((-1, 0, 1), repeat=size):
                    self.check(build_shape(shape, values))
                    trees += 1
        self.assertEqual(trees, 11497)

    def test_fixed_protocol_and_left_and_right_maximum_depth(self):
        self.assertEqual(Codec().serialize(None), '#')
        self.assertIsNone(Codec().deserialize('#'))
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(Codec().serialize(root), '1,2,#,#,3,#,#')
        for direction in ('left', 'right'):
            root = None
            for value in range(10000):
                parent = TreeNode(value % 7 - 3)
                setattr(parent, direction, root)
                root = parent
            self.check(root)


if __name__ == '__main__':
    unittest.main()
