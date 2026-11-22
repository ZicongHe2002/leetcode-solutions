class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def sumOfLeftLeaves(self, root):
        total = 0
        pending = [(root, False)]
        while pending:
            node, is_left = pending.pop()
            if node.left is None and node.right is None:
                if is_left:
                    total += node.val
            else:
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, True))
        return total
