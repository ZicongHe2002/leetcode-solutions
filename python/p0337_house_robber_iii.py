class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        if root is None:
            return 0
        states = {}
        pending = [(root, False)]
        while pending:
            node, ready = pending.pop()
            if not ready:
                pending.append((node, True))
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
                continue
            left = (0, 0) if node.left is None else states[id(node.left)]
            right = (0, 0) if node.right is None else states[id(node.right)]
            skip = max(left) + max(right)
            take = node.val + left[0] + right[0]
            states[id(node)] = (skip, take)
        return max(states[id(root)])
