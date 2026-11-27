from collections import deque


class Solution:
    def shortestSubarray(self, nums, k):
        candidates = deque([(0,0)])
        prefix = 0
        best = len(nums) + 1
        for end,value in enumerate(nums,1):
            prefix += value
            while candidates and prefix - candidates[0][1] >= k:
                start,_ = candidates.popleft()
                best = min(best,end - start)
            while candidates and candidates[-1][1] >= prefix:
                candidates.pop()
            candidates.append((end,prefix))
        return best if best <= len(nums) else -1
