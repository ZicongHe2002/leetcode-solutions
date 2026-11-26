class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        values = []
        pending = [] if root is None else [root]
        while pending:
            node = pending.pop()
            values.append(str(node.val))
            if node.right is not None:
                pending.append(node.right)
            if node.left is not None:
                pending.append(node.left)
        return ' '.join(values)

    def deserialize(self, data):
        if not data:
            return None
        values = map(int, data.split())
        root = TreeNode(next(values))
        ancestors = [root]
        for value in values:
            node = TreeNode(value)
            if value < ancestors[-1].val:
                ancestors[-1].left = node
            else:
                parent = ancestors.pop()
                while ancestors and value > ancestors[-1].val:
                    parent = ancestors.pop()
                parent.right = node
            ancestors.append(node)
        return root
