class Solution:
    def matrixScore(self, grid):
        rows,columns = len(grid),len(grid[0])
        answer = rows * (1 << (columns - 1))
        for column in range(1,columns):
            ones = sum(grid[row][column] == grid[row][0] for row in range(rows))
            answer += max(ones,rows - ones) * (1 << (columns - column - 1))
        return answer
