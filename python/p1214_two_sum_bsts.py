class Solution:
    def twoSumBSTs(self, root1, root2, target):
        values = set()
        pending = [root1] if root1 is not None else []
        while pending:
            node = pending.pop()
            values.add(node.val)
            if node.left is not None:
                pending.append(node.left)
            if node.right is not None:
                pending.append(node.right)
        pending = [root2] if root2 is not None else []
        while pending:
            node = pending.pop()
            if target - node.val in values:
                return True
            if node.left is not None:
                pending.append(node.left)
            if node.right is not None:
                pending.append(node.right)
        return False
