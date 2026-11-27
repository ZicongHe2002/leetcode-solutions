class Solution:
    def detectCapitalUse(self, word):
        uppercase = sum('A' <= char <= 'Z' for char in word)
        return (uppercase == 0 or uppercase == len(word) or
                (uppercase == 1 and 'A' <= word[0] <= 'Z'))
