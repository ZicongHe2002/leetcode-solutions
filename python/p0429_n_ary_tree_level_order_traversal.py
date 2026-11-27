from collections import deque


class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = [] if children is None else children


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        levels = []
        pending = deque([root])
        while pending:
            level = []
            for _ in range(len(pending)):
                node = pending.popleft()
                level.append(node.val)
                pending.extend(node.children or [])
            levels.append(level)
        return levels
