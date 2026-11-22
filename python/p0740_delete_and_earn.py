class Solution:
    def deleteAndEarn(self, nums):
        points = [0] * (max(nums) + 1)
        for value in nums:
            points[value] += value
        previous2 = previous1 = 0
        for earned in points:
            previous2, previous1 = previous1, max(previous1, previous2 + earned)
        return previous1
