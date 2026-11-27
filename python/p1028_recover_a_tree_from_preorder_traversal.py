class Solution:
    def recoverFromPreorder(self, traversal):
        position = 0
        stack = []
        root = None
        while position < len(traversal):
            depth = 0
            while position < len(traversal) and traversal[position] == '-':
                depth += 1
                position += 1
            value = 0
            while position < len(traversal) and traversal[position].isdigit():
                value = 10 * value + int(traversal[position])
                position += 1
            node = TreeNode(value)
            while len(stack) > depth:
                stack.pop()
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            else:
                root = node
            stack.append(node)
        return root
