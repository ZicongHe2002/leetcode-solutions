class Solution:
    def inorderSuccessor(self, node):
        if node is None:
            return None
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        while node.parent is not None and node.parent.right is node:
            node = node.parent
        return node.parent
