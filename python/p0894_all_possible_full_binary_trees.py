from functools import cache


class Solution:
    def allPossibleFBT(self, n):
        @cache
        def shapes(size):
            if size == 1:
                return (None,)
            result = []
            for left_size in range(1,size - 1,2):
                right_size = size - 1 - left_size
                for left in shapes(left_size):
                    for right in shapes(right_size):
                        result.append((left,right))
            return tuple(result)

        def materialize(shape):
            node = TreeNode(0)
            if shape is not None:
                node.left = materialize(shape[0])
                node.right = materialize(shape[1])
            return node

        if n % 2 == 0:
            return []
        return [materialize(shape) for shape in shapes(n)]
