from heapq import heappop, heappush


class Solution:
    def findShortestWay(self, maze, ball, hole):
        rows, columns = len(maze), len(maze[0])
        origin, target = tuple(ball), tuple(hole)
        best = {origin: (0, '')}
        queue = [(0, '', origin[0], origin[1])]
        while queue:
            distance, path, row, column = heappop(queue)
            if best[row, column] != (distance, path):
                continue
            if (row, column) == target:
                return path
            for letter, dr, dc in (('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)):
                nr, nc, steps = row, column, 0
                while 0 <= nr + dr < rows and 0 <= nc + dc < columns and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1
                    if (nr, nc) == target:
                        break
                if steps == 0:
                    continue
                following = (nr, nc)
                candidate = (distance + steps, path + letter)
                previous = best.get(following)
                if previous is None or candidate < previous:
                    best[following] = candidate
                    heappush(queue, (candidate[0], candidate[1], nr, nc))
        return 'impossible'
