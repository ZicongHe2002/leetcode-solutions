class Solution:
    def longestSubstring(self, s, k):
        if k <= 1:
            return len(s)
        if k > len(s):
            return 0
        best = 0
        for target in range(1, 27):
            counts = [0] * 26
            left = distinct = satisfied = 0
            for right, char in enumerate(s):
                index = ord(char) - ord('a')
                if counts[index] == 0:
                    distinct += 1
                counts[index] += 1
                if counts[index] == k:
                    satisfied += 1
                while distinct > target:
                    index = ord(s[left]) - ord('a')
                    if counts[index] == k:
                        satisfied -= 1
                    counts[index] -= 1
                    if counts[index] == 0:
                        distinct -= 1
                    left += 1
                if distinct == target and satisfied == target:
                    best = max(best, right - left + 1)
        return best
