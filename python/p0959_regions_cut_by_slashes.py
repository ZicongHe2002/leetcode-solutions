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
    def regionsBySlashes(self, grid):
        width = len(grid)
        groups = _DisjointSet(4 * width * width)
        for row in range(width):
            for column in range(width):
                base = 4 * (row * width + column)
                top, right, bottom, left = base, base + 1, base + 2, base + 3
                if row:
                    groups.union(top, base - 4 * width + 2)
                if column:
                    groups.union(left, base - 4 + 1)
                symbol = grid[row][column]
                if symbol == ' ':
                    groups.union(top, right)
                    groups.union(right, bottom)
                    groups.union(bottom, left)
                elif symbol == '/':
                    groups.union(top, left)
                    groups.union(right, bottom)
                else:
                    groups.union(top, right)
                    groups.union(bottom, left)
        return groups.components
