from functools import lru_cache


class Solution:
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        words = set(wordDict)
        maximum = max(map(len, words))

        @lru_cache(None)
        def sentences(start):
            if start == len(s):
                return ('',)
            result = []
            for end in range(start + 1, min(len(s), start + maximum) + 1):
                word = s[start:end]
                if word in words:
                    for suffix in sentences(end):
                        result.append(word + (' ' + suffix if suffix else ''))
            return tuple(result)

        return list(sentences(0))
