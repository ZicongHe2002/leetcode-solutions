class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def lowestCommonAncestor(self, root, p, q):
        low, high = min(p.val, q.val), max(p.val, q.val)
        current = root
        while current is not None:
            if current.val > high:
                current = current.left
            elif current.val < low:
                current = current.right
            else:
                return current
