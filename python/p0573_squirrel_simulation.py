class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def distance(first, second):
            return abs(first[0] - second[0]) + abs(first[1] - second[1])

        total = sum(2 * distance(tree, nut) for nut in nuts)
        saving = max(distance(tree, nut) - distance(squirrel, nut) for nut in nuts)
        return total - saving
