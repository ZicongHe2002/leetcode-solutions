class _DisjointSet:
    def __init__(self, count):
        self.parent = list(range(count))
        self.size = [1] * count
        self.components = count

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, first, second):
        first, second = self.find(first), self.find(second)
        if first == second:
            return False
        if self.size[first] < self.size[second]:
            first, second = second, first
        self.parent[second] = first
        self.size[first] += self.size[second]
        self.components -= 1
        return True



class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        groups = _DisjointSet(n)
        for first, second in connections:
            groups.union(first, second)
        return groups.components - 1
