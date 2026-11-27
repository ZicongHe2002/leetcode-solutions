class Solution:
    def delNodes(self, root, to_delete):
        if root is None:
            return []
        deleted_values = set(to_delete)
        forest = []
        stack = [(root, None, None, True)]
        while stack:
            node, parent, side, is_root = stack.pop()
            deleted = node.val in deleted_values
            if is_root and not deleted:
                forest.append(node)
            if deleted and parent is not None:
                setattr(parent, side, None)
            if node.right is not None:
                stack.append((node.right, node, 'right', deleted))
            if node.left is not None:
                stack.append((node.left, node, 'left', deleted))
        return forest
