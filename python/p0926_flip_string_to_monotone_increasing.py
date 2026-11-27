class Solution:
    def minFlipsMonoIncr(self, s):
        ones = flips = 0
        for char in s:
            if char == '1':
                ones += 1
            else:
                flips = min(flips + 1,ones)
        return flips
