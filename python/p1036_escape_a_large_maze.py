from collections import deque


class Solution:
    def isEscapePossible(self, blocked, source, target):
        barriers = {tuple(point) for point in blocked}
        enclosure = len(barriers) * (len(barriers) - 1) // 2
        start,finish = tuple(source),tuple(target)

        def escapes(first, second):
            if first == second:
                return True
            seen = {first}
            queue = deque([first])
            while queue and len(seen) <= enclosure:
                row,column = queue.popleft()
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    point = row + dr,column + dc
                    if (0 <= point[0] < 10**6 and 0 <= point[1] < 10**6
                            and point not in barriers and point not in seen):
                        if point == second:
                            return True
                        seen.add(point)
                        queue.append(point)
            return len(seen) > enclosure

        return escapes(start,finish) and escapes(finish,start)
