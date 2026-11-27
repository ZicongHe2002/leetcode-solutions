class Solution:
    def reachNumber(self, target):
        distance = abs(target)
        steps = total = 0
        while total < distance or (total - distance) % 2:
            steps += 1
            total += steps
        return steps
