class Solution:
    def convertBST(self, root):
        stack = []
        node = root
        total = 0
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root
