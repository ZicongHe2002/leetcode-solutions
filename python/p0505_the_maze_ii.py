from heapq import heappop, heappush


class Solution:
    def shortestDistance(self, maze, start, destination):
        rows, columns = len(maze), len(maze[0])
        origin, target = tuple(start), tuple(destination)
        distances = {origin: 0}
        queue = [(0, origin[0], origin[1])]
        while queue:
            distance, row, column = heappop(queue)
            if distance != distances[row, column]:
                continue
            if (row, column) == target:
                return distance
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc, steps = row, column, 0
                while 0 <= nr + dr < rows and 0 <= nc + dc < columns and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1
                if steps == 0:
                    continue
                following = (nr, nc)
                candidate = distance + steps
                previous = distances.get(following)
                if previous is None or candidate < previous:
                    distances[following] = candidate
                    heappush(queue, (candidate, nr, nc))
        return -1
