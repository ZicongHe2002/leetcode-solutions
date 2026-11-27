class Solution:
    def bstToGst(self, root):
        stack = []
        current = root
        total = 0
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.right
            node = stack.pop()
            total += node.val
            node.val = total
            current = node.left
        return root
