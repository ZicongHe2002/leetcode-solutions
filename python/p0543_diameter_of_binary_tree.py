class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        heights = {None: 0}
        pending = [(root, False)]
        diameter = 0
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
            diameter = max(diameter, left + right)
            heights[node] = 1 + max(left, right)
        return diameter
