from collections import deque


class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        queue = deque([(rCenter,cCenter)])
        seen = {(rCenter,cCenter)}
        answer = []
        while queue:
            row,column = queue.popleft()
            answer.append([row,column])
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = row + dr,column + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    queue.append((nr,nc))
        return answer
