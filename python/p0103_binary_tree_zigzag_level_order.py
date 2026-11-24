from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result = []
        pending = deque([root])
        while pending:
            layer = []
            for _ in range(len(pending)):
                node = pending.popleft()
                layer.append(node.val)
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
            if len(result) % 2:
                layer.reverse()
            result.append(layer)
        return result
