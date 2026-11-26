class Solution:
    def findRotateSteps(self, ring, key):
        positions = {}
        for index, char in enumerate(ring):
            positions.setdefault(char, []).append(index)
        size = len(ring)
        costs = {0: 0}
        for char in key:
            costs = {
                target: 1 + min(cost + min(abs(target - current), size - abs(target - current))
                                for current, cost in costs.items())
                for target in positions[char]
            }
        return min(costs.values())
