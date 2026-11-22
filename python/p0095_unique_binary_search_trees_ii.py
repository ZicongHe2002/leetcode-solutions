from functools import lru_cache



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def generateTrees(self, n):
        @lru_cache(None)
        def shapes(size):
            if size == 0:
                return (None,)
            return tuple((left_size, left, right)
                         for left_size in range(size)
                         for left in shapes(left_size)
                         for right in shapes(size - 1 - left_size))

        def materialize(shape, start):
            if shape is None:
                return None
            left_size, left, right = shape
            value = start + left_size
            return TreeNode(value, materialize(left, start), materialize(right, value + 1))

        return [materialize(shape, 1) for shape in shapes(n)]
