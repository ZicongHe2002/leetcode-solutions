class Solution:
    def getMinimumDifference(self, root):
        stack = []
        node = root
        previous = None
        best = 100000
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if previous is not None:
                best = min(best, node.val - previous)
            previous = node.val
            node = node.right
        return best
