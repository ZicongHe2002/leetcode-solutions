class Solution:
    def flipMatchVoyage(self, root, voyage):
        stack = [root] if root is not None else []
        position = 0
        flips = []
        while stack:
            node = stack.pop()
            if position >= len(voyage) or node.val != voyage[position]:
                return [-1]
            position += 1
            if node.left is not None and position < len(voyage) and node.left.val != voyage[position]:
                flips.append(node.val)
                stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            else:
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
        return flips if position == len(voyage) else [-1]
