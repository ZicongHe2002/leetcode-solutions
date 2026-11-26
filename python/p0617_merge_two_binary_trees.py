class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None and root2 is None:
            return None

        def value(node):
            return node.val if node is not None else 0

        merged = TreeNode(value(root1) + value(root2))
        pending = [(root1, root2, merged)]
        while pending:
            first, second, target = pending.pop()
            for side in ('left', 'right'):
                a = getattr(first, side) if first is not None else None
                b = getattr(second, side) if second is not None else None
                if a is None and b is None:
                    continue
                child = TreeNode(value(a) + value(b))
                setattr(target, side, child)
                pending.append((a, b, child))
        return merged
