class Solution:
    def printTree(self, root):
        if root is None:
            return []
        rows = 0
        pending = [(root, 0)]
        while pending:
            node, depth = pending.pop()
            rows = max(rows, depth + 1)
            if node.left is not None:
                pending.append((node.left, depth + 1))
            if node.right is not None:
                pending.append((node.right, depth + 1))
        width = (1 << rows) - 1
        result = [[''] * width for _ in range(rows)]
        pending = [(root, 0, 0, width - 1)]
        while pending:
            node, depth, left, right = pending.pop()
            middle = (left + right) // 2
            result[depth][middle] = str(node.val)
            if node.left is not None:
                pending.append((node.left, depth + 1, left, middle - 1))
            if node.right is not None:
                pending.append((node.right, depth + 1, middle + 1, right))
        return result
