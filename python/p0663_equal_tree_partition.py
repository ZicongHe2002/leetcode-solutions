class Solution:
    def checkEqualTree(self, root):
        if root is None:
            return False
        totals = {id(None): 0}
        proper_sums = set()
        pending = [(root, False)]
        while pending:
            node, expanded = pending.pop()
            if node is None:
                continue
            if not expanded:
                pending.append((node, True))
                pending.append((node.right, False))
                pending.append((node.left, False))
                continue
            subtotal = node.val + totals[id(node.left)] + totals[id(node.right)]
            totals[id(node)] = subtotal
            if node is not root:
                proper_sums.add(subtotal)
        total = totals[id(root)]
        return total % 2 == 0 and total // 2 in proper_sums
