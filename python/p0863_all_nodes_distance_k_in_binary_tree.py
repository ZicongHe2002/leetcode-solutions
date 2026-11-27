from collections import deque


class Solution:
    def distanceK(self, root, target, k):
        parent = {root:None}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in (node.left,node.right):
                if child is not None:
                    parent[child] = node
                    stack.append(child)
        queue = deque([target])
        seen = {target}
        for _ in range(k):
            for _ in range(len(queue)):
                node = queue.popleft()
                for following in (node.left,node.right,parent[node]):
                    if following is not None and following not in seen:
                        seen.add(following)
                        queue.append(following)
            if not queue:
                break
        return [node.val for node in queue]
