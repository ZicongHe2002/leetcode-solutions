class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        tokens = []
        pending = [root]
        while pending:
            node = pending.pop()
            if node is None:
                tokens.append('#')
            else:
                tokens.append(str(node.val))
                pending.append(node.right)
                pending.append(node.left)
        return ','.join(tokens)

    def deserialize(self, data):
        tokens = iter(data.split(','))
        first = next(tokens)
        if first == '#':
            return None
        root = TreeNode(int(first))
        pending = [(root, 0)]
        for token in tokens:
            child = None if token == '#' else TreeNode(int(token))
            parent, side = pending[-1]
            if side == 0:
                parent.left = child
                pending[-1] = (parent, 1)
            else:
                parent.right = child
                pending.pop()
            if child is not None:
                pending.append((child, 0))
        return root
