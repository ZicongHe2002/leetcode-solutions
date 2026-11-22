class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        clones = {node: Node(node.val)}
        pending = [node]
        while pending:
            original = pending.pop()
            for neighbor in original.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    pending.append(neighbor)
                clones[original].neighbors.append(clones[neighbor])
        return clones[node]
