from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []
        result = []
        pending = deque([root])
        while pending:
            count = len(pending)
            total = 0
            for _ in range(count):
                node = pending.popleft()
                total += node.val
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
            result.append(total / count)
        return result
