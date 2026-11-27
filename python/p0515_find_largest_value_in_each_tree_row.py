from collections import deque


class Solution:
    def largestValues(self, root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            maximum = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                maximum = max(maximum, node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(maximum)
        return result
