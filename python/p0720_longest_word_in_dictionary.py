class Solution:
    def longestWord(self, words):
        buildable = {''}
        best = ''
        for word in sorted(words):
            if word[:-1] in buildable:
                buildable.add(word)
                if len(word) > len(best):
                    best = word
        return best
