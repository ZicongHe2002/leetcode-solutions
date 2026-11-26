class Solution:
    def longestConsecutive(self, root):
        lengths = {}
        pending = [(root, False)]
        answer = 1
        while pending:
            node, ready = pending.pop()
            if not ready:
                pending.append((node, True))
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
                continue
            increasing = decreasing = 1
            for child in (node.left, node.right):
                if child is None:
                    continue
                child_increasing, child_decreasing = lengths[id(child)]
                if child.val == node.val + 1:
                    increasing = max(increasing, child_increasing + 1)
                elif child.val == node.val - 1:
                    decreasing = max(decreasing, child_decreasing + 1)
            lengths[id(node)] = increasing, decreasing
            answer = max(answer, increasing + decreasing - 1)
        return answer
