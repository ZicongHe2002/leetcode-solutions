class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def buildTree(self, inorder, postorder):
        root = TreeNode(postorder[-1])
        pending = [root]
        inorder_index = len(inorder) - 1
        for index in range(len(postorder) - 2, -1, -1):
            node = pending[-1]
            child = TreeNode(postorder[index])
            if node.val != inorder[inorder_index]:
                node.right = child
            else:
                while pending and pending[-1].val == inorder[inorder_index]:
                    node = pending.pop()
                    inorder_index -= 1
                node.left = child
            pending.append(child)
        return root
