class Solution:
    def findSecondMinimumValue(self, root):
        minimum = root.val
        second = None
        pending = [root]
        while pending:
            node = pending.pop()
            if node.val > minimum:
                if second is None or node.val < second:
                    second = node.val
            elif node.left is not None:
                pending.append(node.left)
                pending.append(node.right)
        return -1 if second is None else second
