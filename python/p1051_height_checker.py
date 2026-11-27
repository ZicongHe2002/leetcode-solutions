class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        return sum(actual != target for actual,target in zip(heights,expected))
