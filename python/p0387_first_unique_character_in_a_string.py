from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        counts = Counter(s)
        for index, letter in enumerate(s):
            if counts[letter] == 1:
                return index
        return -1
