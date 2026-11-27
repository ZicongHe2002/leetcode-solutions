class Solution:
    def findDuplicateSubtrees(self, root):
        node_ids = {id(None): 0}
        shapes = {}
        counts = {}
        duplicates = []
        pending = [(root, False)]
        while pending:
            node, expanded = pending.pop()
            if node is None:
                continue
            if not expanded:
                pending.append((node, True))
                pending.append((node.right, False))
                pending.append((node.left, False))
                continue
            shape = (node.val, node_ids[id(node.left)], node_ids[id(node.right)])
            if shape not in shapes:
                shapes[shape] = len(shapes) + 1
            identifier = shapes[shape]
            node_ids[id(node)] = identifier
            counts[identifier] = counts.get(identifier, 0) + 1
            if counts[identifier] == 2:
                duplicates.append(node)
        return duplicates
