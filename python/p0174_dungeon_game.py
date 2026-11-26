class Solution:
    def calculateMinimumHP(self, dungeon):
        columns = len(dungeon[0])
        needed = [float('inf')] * (columns + 1)
        needed[columns - 1] = 1
        for row in range(len(dungeon) - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                needed[column] = max(1, min(needed[column], needed[column + 1]) - dungeon[row][column])
        return needed[0]
