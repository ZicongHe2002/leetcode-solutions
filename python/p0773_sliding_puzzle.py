from collections import deque


class Solution:
    def slidingPuzzle(self, board):
        start = tuple(value for row in board for value in row)
        target = (1, 2, 3, 4, 5, 0)
        neighbors = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        queue = deque([(start, start.index(0), 0)])
        seen = {start}
        while queue:
            state, zero, distance = queue.popleft()
            if state == target:
                return distance
            for following_zero in neighbors[zero]:
                moved = list(state)
                moved[zero], moved[following_zero] = moved[following_zero], moved[zero]
                following = tuple(moved)
                if following not in seen:
                    seen.add(following)
                    queue.append((following, following_zero, distance + 1))
        return -1
