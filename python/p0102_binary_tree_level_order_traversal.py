from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        pending = deque([root])
        result = []
        while pending:
            layer = []
            for _ in range(len(pending)):
                node = pending.popleft()
                layer.append(node.val)
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
            result.append(layer)
        return result
