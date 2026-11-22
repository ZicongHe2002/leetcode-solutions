class Solution:
    def numRescueBoats(self, people, limit):
        weights = sorted(people)
        left, right = 0, len(weights) - 1
        boats = 0
        while left <= right:
            if left < right and weights[left] + weights[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
