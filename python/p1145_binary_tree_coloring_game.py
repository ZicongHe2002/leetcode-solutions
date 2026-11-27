class Solution:
    def btreeGameWinningMove(self, root, n, x):
        sizes = {None: 0}
        stack = [(root, False)]
        left_count = right_count = 0
        while stack:
            node, ready = stack.pop()
            if not ready:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
            else:
                sizes[node] = 1 + sizes[node.left] + sizes[node.right]
                if node.val == x:
                    left_count, right_count = sizes[node.left], sizes[node.right]
        outside = n - 1 - left_count - right_count
        return max(left_count, right_count, outside) > n // 2
