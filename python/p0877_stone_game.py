class Solution:
    def stoneGame(self, piles):
        best = piles[:]
        for length in range(2,len(piles) + 1):
            for left in range(len(piles) - length + 1):
                right = left + length - 1
                best[left] = max(piles[left] - best[left + 1],piles[right] - best[left])
        return best[0] > 0
