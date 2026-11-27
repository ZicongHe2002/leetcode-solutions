class Solution:
    def hitBricks(self, grid, hits):
        rows, columns = len(grid), len(grid[0])
        roof = rows * columns
        parent = list(range(roof + 1))
        sizes = [1] * (roof + 1)
        remaining = [row[:] for row in grid]
        for row,column in hits:
            remaining[row][column] = 0

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def join(first, second):
            first,second = find(first),find(second)
            if first == second:
                return
            if sizes[first] < sizes[second]:
                first,second = second,first
            parent[second] = first
            sizes[first] += sizes[second]

        for row in range(rows):
            for column in range(columns):
                if remaining[row][column]:
                    node = row * columns + column
                    if row == 0:
                        join(node,roof)
                    if row and remaining[row - 1][column]:
                        join(node,node - columns)
                    if column and remaining[row][column - 1]:
                        join(node,node - 1)

        answer = [0] * len(hits)
        for index in range(len(hits) - 1,-1,-1):
            row,column = hits[index]
            if not grid[row][column]:
                continue
            before = sizes[find(roof)]
            remaining[row][column] = 1
            node = row * columns + column
            if row == 0:
                join(node,roof)
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                neighbor_row,neighbor_column = row + dr,column + dc
                if (0 <= neighbor_row < rows and 0 <= neighbor_column < columns
                        and remaining[neighbor_row][neighbor_column]):
                    join(node,neighbor_row * columns + neighbor_column)
            answer[index] = max(0,sizes[find(roof)] - before - 1)
        return answer
