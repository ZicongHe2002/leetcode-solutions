class Solution:
    def lcaDeepestLeaves(self, root):
        if root is None:
            return None
        results = {None: (0, None)}
        stack = [(root, False)]
        while stack:
            node, ready = stack.pop()
            if not ready:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue
            left_height, left_ancestor = results[node.left]
            right_height, right_ancestor = results[node.right]
            if left_height == right_height:
                ancestor = node
            elif left_height > right_height:
                ancestor = left_ancestor
            else:
                ancestor = right_ancestor
            results[node] = (max(left_height, right_height) + 1, ancestor)
        return results[root][1]
