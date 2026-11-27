class Solution:
    def circularArrayLoop(self, nums):
        size = len(nums)

        def advance(index, positive):
            if nums[index] == 0 or (nums[index] > 0) != positive:
                return -1
            following = (index + nums[index]) % size
            return -1 if following == index else following

        for start in range(size):
            if nums[start] == 0:
                continue
            positive = nums[start] > 0
            slow = fast = start
            while True:
                slow = advance(slow, positive)
                fast = advance(fast, positive)
                if fast != -1:
                    fast = advance(fast, positive)
                if slow == -1 or fast == -1:
                    break
                if slow == fast:
                    return True
            current = start
            while nums[current] != 0 and (nums[current] > 0) == positive:
                following = (current + nums[current]) % size
                nums[current] = 0
                current = following
        return False
