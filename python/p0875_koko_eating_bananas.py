class Solution:
    def minEatingSpeed(self, piles, h):
        def feasible(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
                if hours > h:
                    return False
            return True

        left, right = 1, max(piles)
        while left < right:
            middle = left + (right - left) // 2
            if feasible(middle):
                right = middle
            else:
                left = middle + 1
        return left
