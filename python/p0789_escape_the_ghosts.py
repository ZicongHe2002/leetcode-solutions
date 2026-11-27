class Solution:
    def escapeGhosts(self, ghosts, target):
        x, y = target
        distance = abs(x) + abs(y)
        return all(abs(gx - x) + abs(gy - y) > distance for gx, gy in ghosts)
