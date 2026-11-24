class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parents = {root: None}
        pending = [root]
        while p not in parents or q not in parents:
            node = pending.pop()
            if node.left is not None:
                parents[node.left] = node
                pending.append(node.left)
            if node.right is not None:
                parents[node.right] = node
                pending.append(node.right)
        ancestors = set()
        while p is not None:
            ancestors.add(p)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]
        return q
