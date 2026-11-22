class Solution:
    def numDistinct(self, s, t):
        if len(t) > len(s):
            return 0
        counts = [0] * (len(t) + 1)
        counts[0] = 1
        for character in s:
            for length in range(len(t), 0, -1):
                if character == t[length - 1]:
                    counts[length] += counts[length - 1]
        return counts[-1]
