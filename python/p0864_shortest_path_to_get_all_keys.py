from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid):
        rows,columns = len(grid),len(grid[0])
        required = 0
        for row in range(rows):
            for column in range(columns):
                char = grid[row][column]
                if char == '@':
                    start = row,column
                elif 'a' <= char <= 'z':
                    required |= 1 << (ord(char) - ord('a'))
        queue = deque([(start[0],start[1],0,0)])
        seen = {(start[0],start[1],0)}
        while queue:
            row,column,keys,distance = queue.popleft()
            if keys == required:
                return distance
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = row + dr,column + dc
                if not (0 <= nr < rows and 0 <= nc < columns):
                    continue
                char = grid[nr][nc]
                if char == '#':
                    continue
                if 'A' <= char <= 'Z' and not keys & (1 << (ord(char) - ord('A'))):
                    continue
                following = keys
                if 'a' <= char <= 'z':
                    following |= 1 << (ord(char) - ord('a'))
                state = nr,nc,following
                if state not in seen:
                    seen.add(state)
                    queue.append((nr,nc,following,distance + 1))
        return -1
