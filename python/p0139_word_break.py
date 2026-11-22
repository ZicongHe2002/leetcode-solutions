class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        longest = max(map(len, words), default=0)
        reachable = [False] * (len(s) + 1)
        reachable[0] = True
        for end in range(1, len(s) + 1):
            for start in range(max(0, end - longest), end):
                if reachable[start] and s[start:end] in words:
                    reachable[end] = True
                    break
        return reachable[-1]
