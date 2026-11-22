class NumArray:
    def __init__(self, nums):
        self._prefix = [0]
        for value in nums:
            self._prefix.append(self._prefix[-1] + value)

    def sumRange(self, left, right):
        return self._prefix[right + 1] - self._prefix[left]
