from collections import Counter


class Solution:
    def isPossible(self, nums):
        remaining = Counter(nums)
        endings = Counter()
        for value in nums:
            if remaining[value] == 0:
                continue
            remaining[value] -= 1
            if endings[value - 1]:
                endings[value - 1] -= 1
                endings[value] += 1
            elif remaining[value + 1] and remaining[value + 2]:
                remaining[value + 1] -= 1
                remaining[value + 2] -= 1
                endings[value + 2] += 1
            else:
                return False
        return True
