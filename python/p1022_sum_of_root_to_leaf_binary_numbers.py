class Solution:
    def sumRootToLeaf(self, root):
        stack = [(root,0)]
        answer = 0
        while stack:
            node,prefix = stack.pop()
            value = (prefix << 1) | node.val
            if node.left is None and node.right is None:
                answer += value
            else:
                if node.right is not None:
                    stack.append((node.right,value))
                if node.left is not None:
                    stack.append((node.left,value))
        return answer
