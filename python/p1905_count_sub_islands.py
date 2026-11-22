from collections import deque


class Solution:
    def countSubIslands(self, grid1, grid2):
        rows, columns = len(grid2), len(grid2[0])
        seen = [[False] * columns for _ in range(rows)]
        count = 0
        for row in range(rows):
            for column in range(columns):
                if grid2[row][column] == 0 or seen[row][column]:
                    continue
                queue, covered = deque([(row, column)]), True
                seen[row][column] = True
                while queue:
                    current_row, current_column = queue.popleft()
                    if grid1[current_row][current_column] == 0:
                        covered = False
                    for nr, nc in ((current_row - 1, current_column), (current_row + 1, current_column),
                                   (current_row, current_column - 1), (current_row, current_column + 1)):
                        if (0 <= nr < rows and 0 <= nc < columns
                                and grid2[nr][nc] == 1 and not seen[nr][nc]):
                            seen[nr][nc] = True
                            queue.append((nr, nc))
                if covered:
                    count += 1
        return count
