class Solution:
    def largestSumOfAverages(self, nums, k):
        size = len(nums)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        best = [0.0] + [prefix[end] / end for end in range(1,size + 1)]
        for groups in range(2,k + 1):
            following = [float('-inf')] * (size + 1)
            for end in range(groups,size + 1):
                following[end] = max(best[cut] + (prefix[end] - prefix[cut]) / (end - cut)
                                     for cut in range(groups - 1,end))
            best = following
        return best[size]
