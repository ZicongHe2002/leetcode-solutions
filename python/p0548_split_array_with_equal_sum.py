class Solution:
    def splitArray(self, nums):
        size = len(nums)
        if size < 7:
            return False
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        for middle in range(3, size - 3):
            equal_left = set()
            for first in range(1, middle - 1):
                if prefix[first] == prefix[middle] - prefix[first + 1]:
                    equal_left.add(prefix[first])
            for last in range(middle + 2, size - 1):
                third = prefix[last] - prefix[middle + 1]
                fourth = prefix[size] - prefix[last + 1]
                if third == fourth and third in equal_left:
                    return True
        return False
