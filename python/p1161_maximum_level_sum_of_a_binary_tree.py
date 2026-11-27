from collections import deque


class Solution:
    def maxLevelSum(self, root):
        pending = deque([root])
        best_sum = float('-inf')
        best_level = level = 0
        while pending:
            level += 1
            total = 0
            for _ in range(len(pending)):
                node = pending.popleft()
                total += node.val
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
            if total > best_sum:
                best_sum, best_level = total, level
        return best_level
