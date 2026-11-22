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
    def maxNumEdgesToRemove(self, n, edges):
        alice, bob = _DisjointSet(n), _DisjointSet(n)
        used = 0
        for kind, first, second in edges:
            if kind == 3:
                joined_alice = alice.union(first - 1, second - 1)
                joined_bob = bob.union(first - 1, second - 1)
                if joined_alice or joined_bob:
                    used += 1
        for kind, first, second in edges:
            if kind == 1 and alice.union(first - 1, second - 1):
                used += 1
            elif kind == 2 and bob.union(first - 1, second - 1):
                used += 1
        if alice.components == bob.components == 1:
            return len(edges) - used
        return -1
