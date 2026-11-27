class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            return TreeNode(val, root, None)
        frontier = [root]
        for _ in range(depth - 2):
            frontier = [child for node in frontier for child in (node.left, node.right)
                        if child is not None]
        for node in frontier:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root
