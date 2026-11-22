class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxPathSum(self, root):
        gains = {None: 0}
        pending = [(root, False)]
        best = float('-inf')
        while pending:
            node, ready = pending.pop()
            if ready:
                left = max(0, gains[node.left])
                right = max(0, gains[node.right])
                best = max(best, node.val + left + right)
                gains[node] = node.val + max(left, right)
            else:
                pending.append((node, True))
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
        return best
