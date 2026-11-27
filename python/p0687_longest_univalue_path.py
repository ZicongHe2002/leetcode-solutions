class Solution:
    def longestUnivaluePath(self, root):
        if root is None:
            return 0
        pending = [(root, False)]
        arms = {}
        best = 0
        while pending:
            node, expanded = pending.pop()
            if not expanded:
                pending.append((node, True))
                if node.left is not None:
                    pending.append((node.left, False))
                if node.right is not None:
                    pending.append((node.right, False))
            else:
                left = arms[id(node.left)] + 1 if node.left is not None and node.left.val == node.val else 0
                right = arms[id(node.right)] + 1 if node.right is not None and node.right.val == node.val else 0
                best = max(best, left + right)
                arms[id(node)] = max(left, right)
        return best
