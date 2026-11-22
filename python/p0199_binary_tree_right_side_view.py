class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        result = []
        pending = [(root, 0)] if root is not None else []
        while pending:
            node, depth = pending.pop()
            if depth == len(result):
                result.append(node.val)
            if node.left is not None:
                pending.append((node.left, depth + 1))
            if node.right is not None:
                pending.append((node.right, depth + 1))
        return result
