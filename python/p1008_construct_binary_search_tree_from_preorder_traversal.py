class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for index in range(1,len(preorder)):
            node = TreeNode(preorder[index])
            if node.val < stack[-1].val:
                stack[-1].left = node
            else:
                parent = None
                while stack and stack[-1].val < node.val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root
