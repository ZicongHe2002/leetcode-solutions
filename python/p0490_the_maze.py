from collections import deque


class Solution:
    def hasPath(self, maze, start, destination):
        rows, columns = len(maze), len(maze[0])
        origin, target = tuple(start), tuple(destination)
        queue = deque([origin])
        seen = {origin}
        while queue:
            row, column = queue.popleft()
            if (row, column) == target:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row, column
                while 0 <= nr + dr < rows and 0 <= nc + dc < columns and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                following = (nr, nc)
                if following not in seen:
                    seen.add(following)
                    queue.append(following)
        return False
