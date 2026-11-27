class Solution:
    def thirdMax(self, nums):
        best = []
        for value in nums:
            if value in best:
                continue
            best.append(value)
            best.sort(reverse=True)
            if len(best) > 3:
                best.pop()
        return best[2] if len(best) == 3 else best[0]
