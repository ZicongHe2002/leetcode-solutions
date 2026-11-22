class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        pending = [(root, None, None)] if root is not None else []
        while pending:
            node, lower, upper = pending.pop()
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            if node.right is not None:
                pending.append((node.right, node.val, upper))
            if node.left is not None:
                pending.append((node.left, lower, node.val))
        return True
