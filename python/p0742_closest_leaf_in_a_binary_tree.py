from collections import deque


class Solution:
    def findClosestLeaf(self, root, k):
        graph, leaves = {}, set()
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            graph.setdefault(node.val, [])
            if parent is not None:
                graph[node.val].append(parent)
                graph[parent].append(node.val)
            if node.left is None and node.right is None:
                leaves.add(node.val)
            for child in (node.left, node.right):
                if child is not None:
                    stack.append((child, node.val))
        queue, seen = deque([k]), {k}
        while queue:
            value = queue.popleft()
            if value in leaves:
                return value
            for neighbor in graph[value]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
