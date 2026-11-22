class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def sumNumbers(self, root):
        pending = [(root, 0)]
        total = 0
        while pending:
            node, prefix = pending.pop()
            number = prefix * 10 + node.val
            if node.left is None and node.right is None:
                total += number
            else:
                if node.right is not None:
                    pending.append((node.right, number))
                if node.left is not None:
                    pending.append((node.left, number))
        return total
