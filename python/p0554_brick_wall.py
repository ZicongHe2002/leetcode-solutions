class Solution:
    def leastBricks(self, wall):
        edges = {}
        for row in wall:
            position = 0
            for width in row[:-1]:
                position += width
                edges[position] = edges.get(position, 0) + 1
        return len(wall) - max(edges.values(), default=0)
