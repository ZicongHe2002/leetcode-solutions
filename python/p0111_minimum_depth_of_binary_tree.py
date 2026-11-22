class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        from collections import deque

        pending = deque([(root, 1)])
        while pending:
            node, depth = pending.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                pending.append((node.left, depth + 1))
            if node.right is not None:
                pending.append((node.right, depth + 1))
