class Solution:
    def fallingSquares(self, positions):
        landed = []
        answer = []
        tallest = 0
        for left, side in positions:
            right = left + side
            base = max((top for start, end, top in landed if left < end and start < right), default=0)
            top = base + side
            landed.append((left, right, top))
            tallest = max(tallest, top)
            answer.append(tallest)
        return answer
