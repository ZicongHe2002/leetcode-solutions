class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def binaryTreePaths(self, root):
        result, parts = [], []
        pending = [(root, False)]
        while pending:
            node, leaving = pending.pop()
            if leaving:
                parts.pop()
                continue
            parts.append(str(node.val))
            pending.append((node, True))
            if node.left is None and node.right is None:
                result.append('->'.join(parts))
            else:
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
        return result
