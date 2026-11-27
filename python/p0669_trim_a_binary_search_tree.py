class Solution:
    def trimBST(self, root, low, high):
        while root is not None and not low <= root.val <= high:
            root = root.right if root.val < low else root.left
        node = root
        while node is not None:
            while node.left is not None and node.left.val < low:
                node.left = node.left.right
            node = node.left
        node = root
        while node is not None:
            while node.right is not None and node.right.val > high:
                node.right = node.right.left
            node = node.right
        return root
