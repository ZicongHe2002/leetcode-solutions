class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        heights = {None: 0}
        pending = [(root, False)]
        while pending:
            node, expanded = pending.pop()
            if not expanded:
                pending.append((node, True))
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
                continue
            left, right = heights[node.left], heights[node.right]
            if abs(left - right) > 1:
                return False
            heights[node] = 1 + max(left, right)
        return True
