class Solution:
    def constructFromPrePost(self, preorder, postorder):
        position = {value:index for index,value in enumerate(postorder)}

        def build(pre_start, post_start, size):
            if size == 0:
                return None
            root = TreeNode(preorder[pre_start])
            if size > 1:
                left_size = position[preorder[pre_start + 1]] - post_start + 1
                root.left = build(pre_start + 1,post_start,left_size)
                root.right = build(pre_start + 1 + left_size,post_start + left_size,size - 1 - left_size)
            return root

        return build(0,0,len(preorder))
