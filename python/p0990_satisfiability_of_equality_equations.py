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
    def equationsPossible(self, equations):
        groups = _DisjointSet(26)
        for equation in equations:
            if equation[1] == '=':
                groups.union(ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a'))
        for equation in equations:
            if equation[1] == '!':
                first = ord(equation[0]) - ord('a')
                second = ord(equation[3]) - ord('a')
                if groups.find(first) == groups.find(second):
                    return False
        return True
