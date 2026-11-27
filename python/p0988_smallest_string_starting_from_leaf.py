class Solution:
    def smallestFromLeaf(self, root):
        path = []
        best = None
        stack = [(root,False)]
        while stack:
            node,leaving = stack.pop()
            if leaving:
                path.pop()
                continue
            path.append(chr(ord('a') + node.val))
            stack.append((node,True))
            if node.left is None and node.right is None:
                candidate = ''.join(reversed(path))
                if best is None or candidate < best:
                    best = candidate
            if node.right is not None:
                stack.append((node.right,False))
            if node.left is not None:
                stack.append((node.left,False))
        return best
