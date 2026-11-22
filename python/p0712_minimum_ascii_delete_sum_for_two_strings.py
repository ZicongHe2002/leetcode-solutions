class Solution:
    def minimumDeleteSum(self, s1, s2):
        cost = [0]
        for character in s2:
            cost.append(cost[-1] + ord(character))
        for first in s1:
            diagonal = cost[0]
            cost[0] += ord(first)
            for j, second in enumerate(s2, 1):
                previous = cost[j]
                if first == second:
                    cost[j] = diagonal
                else:
                    cost[j] = min(cost[j] + ord(first), cost[j - 1] + ord(second))
                diagonal = previous
        return cost[-1]
