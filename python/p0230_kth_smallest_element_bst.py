class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        pending = []
        current = root
        while current is not None or pending:
            while current is not None:
                pending.append(current)
                current = current.left
            current = pending.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right
