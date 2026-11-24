class Solution:
    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        entry = 0
        while entry != slow:
            entry = nums[entry]
            slow = nums[slow]
        return entry
