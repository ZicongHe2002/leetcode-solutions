class Solution:
    def isUnivalTree(self, root):
        expected = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != expected:
                return False
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return True
