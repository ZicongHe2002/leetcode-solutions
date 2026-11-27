class Solution:
    def minCostClimbingStairs(self, cost):
        two_back = previous = 0
        for step in range(2, len(cost) + 1):
            current = min(previous + cost[step - 1], two_back + cost[step - 2])
            two_back, previous = previous, current
        return previous
