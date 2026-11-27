class Solution:
    def minIncrementForUnique(self, nums):
        next_allowed = 0
        moves = 0
        for value in sorted(nums):
            assigned = max(value,next_allowed)
            moves += assigned - value
            next_allowed = assigned + 1
        return moves
