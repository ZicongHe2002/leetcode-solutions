class Solution:
    def robotSim(self, commands, obstacles):
        blocked = {tuple(point) for point in obstacles}
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        direction = x = y = best = 0
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                dx,dy = directions[direction]
                for _ in range(command):
                    following = x + dx,y + dy
                    if following in blocked:
                        break
                    x,y = following
                    best = max(best,x * x + y * y)
        return best
