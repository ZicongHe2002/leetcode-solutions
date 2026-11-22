from collections import deque


class Solution:
    def longestSubarray(self, nums, limit):
        maxima, minima = deque(), deque()
        left = best = 0
        for right, value in enumerate(nums):
            while maxima and nums[maxima[-1]] < value:
                maxima.pop()
            while minima and nums[minima[-1]] > value:
                minima.pop()
            maxima.append(right)
            minima.append(right)
            while nums[maxima[0]] - nums[minima[0]] > limit:
                if maxima[0] == left:
                    maxima.popleft()
                if minima[0] == left:
                    minima.popleft()
                left += 1
            best = max(best, right - left + 1)
        return best
