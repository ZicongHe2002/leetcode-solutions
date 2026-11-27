class Solution:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        tail = dummy
        stack = []
        current = root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            node = stack.pop()
            following = node.right
            node.left = None
            node.right = None
            tail.right = node
            tail = node
            current = following
        return dummy.right
