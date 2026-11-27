class Solution:
    def largestIsland(self, grid):
        size = len(grid)
        labels = [row[:] for row in grid]
        areas = {0:0}
        identifier = 2
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        for row in range(size):
            for column in range(size):
                if labels[row][column] != 1:
                    continue
                labels[row][column] = identifier
                stack = [(row,column)]
                area = 0
                while stack:
                    current_row,current_column = stack.pop()
                    area += 1
                    for dr,dc in directions:
                        nr,nc = current_row + dr,current_column + dc
                        if 0 <= nr < size and 0 <= nc < size and labels[nr][nc] == 1:
                            labels[nr][nc] = identifier
                            stack.append((nr,nc))
                areas[identifier] = area
                identifier += 1
        best = max(areas.values())
        for row in range(size):
            for column in range(size):
                if labels[row][column] == 0:
                    neighboring = {labels[row + dr][column + dc] for dr,dc in directions
                                   if 0 <= row + dr < size and 0 <= column + dc < size}
                    best = max(best,1 + sum(areas[label] for label in neighboring))
        return best
