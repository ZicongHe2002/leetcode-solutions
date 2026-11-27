class Solution:
    def colorBorder(self, grid, row, col, color):
        rows,columns = len(grid),len(grid[0])
        original = grid[row][col]
        seen = {(row,col)}
        stack = [(row,col)]
        border = []
        while stack:
            current_row,current_column = stack.pop()
            edge = False
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = current_row + dr,current_column + dc
                if not (0 <= nr < rows and 0 <= nc < columns):
                    edge = True
                elif grid[nr][nc] != original:
                    edge = True
                elif (nr,nc) not in seen:
                    seen.add((nr,nc))
                    stack.append((nr,nc))
            if edge:
                border.append((current_row,current_column))
        result = [values[:] for values in grid]
        for current_row,current_column in border:
            result[current_row][current_column] = color
        return result
