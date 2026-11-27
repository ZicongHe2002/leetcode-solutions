from collections import deque


class Solution:
    def cutOffTree(self, forest):
        rows, columns = len(forest), len(forest[0])
        if forest[0][0] == 0:
            return -1
        trees = sorted((height, row, column)
                       for row, values in enumerate(forest)
                       for column, height in enumerate(values) if height > 1)

        def distance(start, target):
            pending = deque([(start[0], start[1], 0)])
            visited = {start}
            while pending:
                row, column, steps = pending.popleft()
                if (row, column) == target:
                    return steps
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, column + dc
                    if (0 <= nr < rows and 0 <= nc < columns
                            and forest[nr][nc] > 0 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        pending.append((nr, nc, steps + 1))
            return -1

        current = (0, 0)
        total = 0
        for _, row, column in trees:
            target = (row, column)
            steps = distance(current, target)
            if steps < 0:
                return -1
            total += steps
            current = target
        return total
