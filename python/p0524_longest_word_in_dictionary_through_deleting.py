class Solution:
    def findLongestWord(self, s, dictionary):
        best = ''
        for word in dictionary:
            if len(word) > len(s) or len(word) < len(best):
                continue
            if len(word) == len(best) and word >= best:
                continue
            matched = 0
            for char in s:
                if matched < len(word) and word[matched] == char:
                    matched += 1
            if matched == len(word):
                best = word
        return best
