class Solution:
    def checkPossibility(self, nums):
        previous = nums[0]
        changed = False
        for index in range(1, len(nums)):
            value = nums[index]
            if value < previous:
                if changed:
                    return False
                changed = True
                if index >= 2 and value < nums[index - 2]:
                    continue
            previous = value
        return True
