class Solution:
    def findTarget(self, root, k):
        seen = set()
        pending = [root]
        while pending:
            node = pending.pop()
            if node is None:
                continue
            if k - node.val in seen:
                return True
            seen.add(node.val)
            pending.append(node.right)
            pending.append(node.left)
        return False
