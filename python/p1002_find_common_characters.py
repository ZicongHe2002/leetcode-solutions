from collections import Counter


class Solution:
    def commonChars(self, words):
        common = Counter(words[0])
        for index in range(1,len(words)):
            common &= Counter(words[index])
        return list(common.elements())
