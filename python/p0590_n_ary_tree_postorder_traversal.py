class Solution:
    def postorder(self, root):
        if root is None:
            return []
        result = []
        pending = [(root, iter(root.children or ()))]
        while pending:
            node, children = pending[-1]
            child = next(children, None)
            if child is None:
                result.append(node.val)
                pending.pop()
            else:
                pending.append((child, iter(child.children or ())))
        return result
