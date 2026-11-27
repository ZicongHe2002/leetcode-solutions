def _canonical(points):
    forms = [[] for _ in range(8)]
    for x, y in points:
        transformed = ((x, y), (x, -y), (-x, y), (-x, -y),
                       (y, x), (y, -x), (-y, x), (-y, -x))
        for form, point in zip(forms, transformed):
            form.append(point)
    normalized = []
    for form in forms:
        minimum_x = min(x for x, _ in form)
        minimum_y = min(y for _, y in form)
        normalized.append(tuple(sorted((x - minimum_x, y - minimum_y) for x, y in form)))
    return min(normalized)


class Solution:
    def numDistinctIslands2(self, grid):
        rows, columns = len(grid), len(grid[0])
        visited, shapes = set(), set()
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0 or (row, column) in visited:
                    continue
                pending = [(row, column)]
                visited.add((row, column))
                points = []
                while pending:
                    r, c = pending.pop()
                    points.append((r, c))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < columns
                                and grid[nr][nc] == 1 and (nr, nc) not in visited):
                            visited.add((nr, nc))
                            pending.append((nr, nc))
                shapes.add(_canonical(points))
        return len(shapes)
