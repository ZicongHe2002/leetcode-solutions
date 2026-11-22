class _DisjointSet:
    def __init__(self, count):
        self.parent = list(range(count))
        self.size = [1] * count

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
        return True



class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        groups = _DisjointSet(len(s))
        for first, second in pairs:
            groups.union(first, second)
        positions = {}
        for index in range(len(s)):
            positions.setdefault(groups.find(index), []).append(index)
        result = list(s)
        for indices in positions.values():
            letters = sorted(s[index] for index in indices)
            for index, letter in zip(indices, letters):
                result[index] = letter
        return ''.join(result)
