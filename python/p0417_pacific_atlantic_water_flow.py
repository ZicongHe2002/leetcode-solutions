class Solution:
    def pacificAtlantic(self, heights):
        rows, columns = len(heights), len(heights[0])

        def reverse_reachable(starts):
            visited = set(starts)
            pending = list(visited)
            while pending:
                row, column = pending.pop()
                for next_row, next_column in [(row - 1, column), (row + 1, column),
                                               (row, column - 1), (row, column + 1)]:
                    if 0 <= next_row < rows and 0 <= next_column < columns:
                        position = (next_row, next_column)
                        if position not in visited and heights[next_row][next_column] >= heights[row][column]:
                            visited.add(position)
                            pending.append(position)
            return visited

        pacific = reverse_reachable([(row, 0) for row in range(rows)] + [(0, column) for column in range(columns)])
        atlantic = reverse_reachable([(row, columns - 1) for row in range(rows)] + [(rows - 1, column) for column in range(columns)])
        return [[row, column] for row in range(rows) for column in range(columns)
                if (row, column) in pacific and (row, column) in atlantic]
