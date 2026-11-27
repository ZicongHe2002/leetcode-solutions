class Solution:
    def subtreeWithAllDeepest(self, root):
        def deepest(node):
            if node is None:
                return 0,None
            left_height,left_root = deepest(node.left)
            right_height,right_root = deepest(node.right)
            if left_height == right_height:
                return left_height + 1,node
            if left_height > right_height:
                return left_height + 1,left_root
            return right_height + 1,right_root

        return deepest(root)[1]
