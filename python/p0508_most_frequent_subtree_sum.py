class Solution:
    def findFrequentTreeSum(self, root):
        if root is None:
            return []
        subtotals = {}
        frequencies = {}
        pending = [(root, False)]
        while pending:
            node, expanded = pending.pop()
            if not expanded:
                pending.append((node, True))
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
                continue
            left = subtotals[id(node.left)] if node.left is not None else 0
            right = subtotals[id(node.right)] if node.right is not None else 0
            total = node.val + left + right
            subtotals[id(node)] = total
            frequencies[total] = frequencies.get(total, 0) + 1
        maximum = max(frequencies.values())
        return [total for total, count in frequencies.items() if count == maximum]
