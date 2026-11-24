class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):
        answer = 0
        prefixes = {0: 1}
        pending = [(root, 0, False)] if root is not None else []
        while pending:
            node, total, leaving = pending.pop()
            if leaving:
                prefixes[total] -= 1
                if prefixes[total] == 0:
                    del prefixes[total]
                continue
            total += node.val
            answer += prefixes.get(total - targetSum, 0)
            prefixes[total] = prefixes.get(total, 0) + 1
            pending.append((node, total, True))
            if node.right is not None:
                pending.append((node.right, total, False))
            if node.left is not None:
                pending.append((node.left, total, False))
        return answer
