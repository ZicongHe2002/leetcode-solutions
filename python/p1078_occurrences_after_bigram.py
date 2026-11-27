class Solution:
    def findOcurrences(self, text, first, second):
        words = text.split()
        return [words[index] for index in range(2,len(words))
                if words[index - 2] == first and words[index - 1] == second]
