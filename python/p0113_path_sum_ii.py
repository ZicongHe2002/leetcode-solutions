class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def pathSum(self, root, targetSum):
        if root is None:
            return []
        result, path = [], []
        stack = [(root, targetSum, False)]
        while stack:
            node, remaining, exiting = stack.pop()
            if exiting:
                path.pop()
                continue
            path.append(node.val)
            remaining -= node.val
            stack.append((node, remaining, True))
            if node.left is None and node.right is None and remaining == 0:
                result.append(path[:])
            if node.right is not None:
                stack.append((node.right, remaining, False))
            if node.left is not None:
                stack.append((node.left, remaining, False))
        return result
