class Solution:
    def maximumAverageSubtree(self, root):
        totals = {}
        stack = [(root, False)]
        answer = float('-inf')
        while stack:
            node, ready = stack.pop()
            if not ready:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue
            left_sum, left_count = totals.get(node.left, (0, 0))
            right_sum, right_count = totals.get(node.right, (0, 0))
            subtotal = node.val + left_sum + right_sum
            count = 1 + left_count + right_count
            totals[node] = (subtotal, count)
            answer = max(answer, subtotal / count)
        return answer
