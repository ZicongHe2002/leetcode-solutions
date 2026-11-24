class Solution:
    def minimumTotal(self, triangle):
        cost = triangle[-1][:]
        for row_index in range(len(triangle) - 2, -1, -1):
            for column, value in enumerate(triangle[row_index]):
                cost[column] = value + min(cost[column], cost[column + 1])
        return cost[0]
