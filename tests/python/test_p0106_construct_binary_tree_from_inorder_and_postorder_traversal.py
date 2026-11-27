from functools import lru_cache
import unittest

from python.p0106_construct_binary_tree_from_inorder_and_postorder_traversal import TreeNode, Solution



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



def tree_signature(root):
    result, seen = [], set()
    pending = [root]
    while pending:
        node = pending.pop()
        if node is None:
            result.append(None)
            continue
        if node in seen:
            raise AssertionError('cycle or shared output node')
        seen.add(node)
        result.append(node.val)
        pending.extend((node.right, node.left))
    return result


def traversals(root):
    inorder, postorder = [], []
    stack, current = [], root
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        inorder.append(current.val)
        current = current.right
    pending = [(root, False)]
    while pending:
        node, ready = pending.pop()
        if node is None:
            continue
        if ready:
            postorder.append(node.val)
        else:
            pending.extend(((node, True), (node.right, False), (node.left, False)))
    return inorder, postorder


class InorderPostorderConstructionTests(unittest.TestCase):
    def check(self, root):
        inorder, postorder = traversals(root)
        before = (inorder[:], postorder[:])
        result = Solution().buildTree(inorder, postorder)
        self.assertEqual(tree_signature(result), tree_signature(root))
        self.assertEqual((inorder, postorder), before)

    def test_all_small_binary_tree_shapes_against_original_structure(self):
        checks = 0
        for size in range(1, 8):
            for shape in shapes(size):
                self.check(materialize(shape, range(size)))
                checks += 1
        self.assertEqual(checks, 625)

    def test_maximum_length_left_right_chains_balanced_tree_and_extremes(self):
        for side in ('left', 'right'):
            root = current = TreeNode(0)
            for value in range(1, 3000):
                child = TreeNode(value)
                setattr(current, side, child)
                current = child
            self.check(root)

        def balanced(low, high):
            if low >= high:
                return None
            middle = (low + high) // 2
            return TreeNode(middle, balanced(low, middle), balanced(middle + 1, high))

        self.check(balanced(0, 3000))
        self.check(TreeNode(0, TreeNode(-3000), TreeNode(3000)))


if __name__ == '__main__':
    unittest.main()
