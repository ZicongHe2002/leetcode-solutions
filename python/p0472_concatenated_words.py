class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        dictionary = set(words)
        result = []
        for word in words:
            parts = [-1] * (len(word) + 1)
            parts[0] = 0
            for end in range(1, len(word) + 1):
                for start in range(end):
                    if parts[start] >= 0 and word[start:end] in dictionary:
                        parts[end] = max(parts[end], parts[start] + 1)
            if parts[-1] >= 2:
                result.append(word)
        return result
