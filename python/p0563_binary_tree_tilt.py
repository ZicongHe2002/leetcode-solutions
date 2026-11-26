class Solution:
    def findTilt(self, root):
        pending = [(root, False)]
        sums = []
        tilt = 0
        while pending:
            node, expanded = pending.pop()
            if node is None:
                sums.append(0)
            elif expanded:
                right_sum = sums.pop()
                left_sum = sums.pop()
                tilt += abs(left_sum - right_sum)
                sums.append(left_sum + right_sum + node.val)
            else:
                pending.append((node, True))
                pending.append((node.right, False))
                pending.append((node.left, False))
        return tilt
