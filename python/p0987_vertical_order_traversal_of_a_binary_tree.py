class Solution:
    def verticalTraversal(self, root):
        if root is None:
            return []
        entries = []
        stack = [(root,0,0)]
        while stack:
            node,row,column = stack.pop()
            entries.append((column,row,node.val))
            if node.right is not None:
                stack.append((node.right,row + 1,column + 1))
            if node.left is not None:
                stack.append((node.left,row + 1,column - 1))
        result = []
        previous = None
        for column,row,value in sorted(entries):
            if column != previous:
                result.append([])
                previous = column
            result[-1].append(value)
        return result
