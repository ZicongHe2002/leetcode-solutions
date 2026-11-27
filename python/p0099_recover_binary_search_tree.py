class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def recoverTree(self, root):
        first = second = previous = None
        current = root
        while current is not None:
            if current.left is not None:
                predecessor = current.left
                while predecessor.right is not None and predecessor.right is not current:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                    continue
                predecessor.right = None
            if previous is not None and previous.val > current.val:
                if first is None:
                    first = previous
                second = current
            previous = current
            current = current.right
        if first is not None:
            first.val, second.val = second.val, first.val
