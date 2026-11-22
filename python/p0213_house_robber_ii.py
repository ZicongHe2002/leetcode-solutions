class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def linear(start, stop):
            previous_two = previous_one = 0
            for index in range(start, stop):
                previous_two, previous_one = previous_one, max(previous_one, previous_two + nums[index])
            return previous_one

        return max(linear(0, len(nums) - 1), linear(1, len(nums)))
