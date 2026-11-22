class Solution:
    def increasingTriplet(self, nums):
        first = second = 2**31
        for value in nums:
            if value <= first:
                first = value
            elif value <= second:
                second = value
            else:
                return True
        return False
