from collections import deque


class Solution:
    def isCousins(self, root, x, y):
        queue = deque([(root,None)])
        while queue:
            found = {}
            for _ in range(len(queue)):
                node,parent = queue.popleft()
                if node.val == x or node.val == y:
                    found[node.val] = parent
                if node.left is not None:
                    queue.append((node.left,node))
                if node.right is not None:
                    queue.append((node.right,node))
            if found:
                return len(found) == 2 and found[x] is not found[y]
        return False
