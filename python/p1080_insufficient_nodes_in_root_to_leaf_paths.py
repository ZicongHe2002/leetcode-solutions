class Solution:
    def sufficientSubset(self, root, limit):
        if root is None:
            return None
        kept = {}
        stack = [(root, 0, False)]
        while stack:
            node, prefix, ready = stack.pop()
            path_sum = prefix + node.val
            if not ready:
                if node.left is None and node.right is None:
                    kept[node] = node if path_sum >= limit else None
                    continue
                stack.append((node, prefix, True))
                if node.right is not None:
                    stack.append((node.right, path_sum, False))
                if node.left is not None:
                    stack.append((node.left, path_sum, False))
            else:
                node.left = kept[node.left] if node.left is not None else None
                node.right = kept[node.right] if node.right is not None else None
                kept[node] = node if node.left is not None or node.right is not None else None
        return kept[root]
