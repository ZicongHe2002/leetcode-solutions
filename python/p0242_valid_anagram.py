class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for first, second in zip(s, t):
            counts[ord(first) - ord('a')] += 1
            counts[ord(second) - ord('a')] -= 1
        return all(count == 0 for count in counts)
