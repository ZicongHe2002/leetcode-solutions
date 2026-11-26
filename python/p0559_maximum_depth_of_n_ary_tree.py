class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        frontier = [root]
        depth = 0
        while frontier:
            depth += 1
            frontier = [child for node in frontier for child in (node.children or ())]
        return depth
