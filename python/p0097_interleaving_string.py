class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        possible = [False] * (len(s2) + 1)
        possible[0] = True
        for j, character in enumerate(s2, 1):
            possible[j] = possible[j - 1] and character == s3[j - 1]
        for i, first in enumerate(s1, 1):
            possible[0] = possible[0] and first == s3[i - 1]
            for j, second in enumerate(s2, 1):
                needed = s3[i + j - 1]
                possible[j] = (possible[j] and first == needed) or (possible[j - 1] and second == needed)
        return possible[-1]
