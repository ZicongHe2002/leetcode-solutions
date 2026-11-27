class Solution:
    def maxAncestorDiff(self, root):
        stack = [(root,root.val,root.val)]
        answer = 0
        while stack:
            node,minimum,maximum = stack.pop()
            minimum = min(minimum,node.val)
            maximum = max(maximum,node.val)
            answer = max(answer,maximum - minimum)
            if node.left is not None:
                stack.append((node.left,minimum,maximum))
            if node.right is not None:
                stack.append((node.right,minimum,maximum))
        return answer
