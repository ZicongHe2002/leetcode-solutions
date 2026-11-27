class Solution:
    def minimumLengthEncoding(self, words):
        remaining = set(words)
        for word in words:
            for start in range(1,len(word)):
                remaining.discard(word[start:])
        return sum(len(word) + 1 for word in remaining)
