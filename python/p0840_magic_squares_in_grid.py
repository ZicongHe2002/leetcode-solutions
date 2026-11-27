class Solution:
    def numMagicSquaresInside(self, grid):
        answer = 0
        for row in range(len(grid) - 2):
            for column in range(len(grid[0]) - 2):
                if grid[row + 1][column + 1] != 5:
                    continue
                values = [[grid[row + dr][column + dc] for dc in range(3)] for dr in range(3)]
                if {value for line in values for value in line} != set(range(1,10)):
                    continue
                if (all(sum(line) == 15 for line in values)
                        and all(sum(values[dr][dc] for dr in range(3)) == 15 for dc in range(3))
                        and sum(values[index][index] for index in range(3)) == 15
                        and sum(values[index][2 - index] for index in range(3)) == 15):
                    answer += 1
        return answer
