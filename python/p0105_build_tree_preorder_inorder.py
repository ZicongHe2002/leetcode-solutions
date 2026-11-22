class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        pending = [root]
        inorder_index = 0
        for index in range(1, len(preorder)):
            node = pending[-1]
            child = TreeNode(preorder[index])
            if node.val != inorder[inorder_index]:
                node.left = child
            else:
                while pending and pending[-1].val == inorder[inorder_index]:
                    node = pending.pop()
                    inorder_index += 1
                node.right = child
            pending.append(child)
        return root
