class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def deleteNode(self, root, key):
        dummy = TreeNode(0, root)
        parent, current = dummy, root
        while current is not None and current.val != key:
            parent = current
            current = current.left if key < current.val else current.right
        if current is None:
            return root
        if current.left is not None and current.right is not None:
            parent, successor = current, current.right
            while successor.left is not None:
                parent = successor
                successor = successor.left
            current.val = successor.val
            current = successor
        child = current.left if current.left is not None else current.right
        if parent.left is current:
            parent.left = child
        else:
            parent.right = child
        return dummy.left
