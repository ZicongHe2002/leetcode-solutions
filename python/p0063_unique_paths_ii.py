class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        ways = [0] * len(obstacleGrid[0])
        ways[0] = 1
        for row in obstacleGrid:
            for column, blocked in enumerate(row):
                if blocked:
                    ways[column] = 0
                elif column:
                    ways[column] += ways[column - 1]
        return ways[-1]
