class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        ordered = sorted(nums)
        lengths = [1] * len(ordered)
        previous = [-1] * len(ordered)
        best = 0
        for end, value in enumerate(ordered):
            for start in range(end):
                if value % ordered[start] == 0 and lengths[start] + 1 > lengths[end]:
                    lengths[end] = lengths[start] + 1
                    previous[end] = start
            if lengths[end] > lengths[best]:
                best = end
        result = []
        while best != -1:
            result.append(ordered[best])
            best = previous[best]
        result.reverse()
        return result
