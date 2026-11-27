class Solution:
    def insertIntoMaxTree(self, root, val):
        node = TreeNode(val)
        if root is None or val > root.val:
            node.left = root
            return node
        current = root
        while current.right is not None and current.right.val > val:
            current = current.right
        node.left = current.right
        current.right = node
        return root
