class Solution:
    def rangeSumBST(self, root, low, high):
        answer = 0
        stack = [root] if root is not None else []
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                answer += node.val
            if node.left is not None and node.val > low:
                stack.append(node.left)
            if node.right is not None and node.val < high:
                stack.append(node.right)
        return answer
