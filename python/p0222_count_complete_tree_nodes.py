class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def countNodes(self, root):
        def left_height(node):
            height = 0
            while node is not None:
                height += 1
                node = node.left
            return height

        count = 0
        current = root
        while current is not None:
            left = left_height(current.left)
            right = left_height(current.right)
            if left == right:
                count += 1 << left
                current = current.right
            else:
                count += 1 << right
                current = current.left
        return count
