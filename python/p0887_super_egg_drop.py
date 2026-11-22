class Solution:
    def superEggDrop(self, k, n):
        covered = [0] * (k + 1)
        moves = 0
        while covered[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                covered[eggs] += covered[eggs - 1] + 1
        return moves
