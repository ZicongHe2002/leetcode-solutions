class Solution:
    def longestPalindrome(self, s):
        odd = set()
        paired = 0
        for letter in s:
            if letter in odd:
                odd.remove(letter)
                paired += 2
            else:
                odd.add(letter)
        return paired + (1 if odd else 0)
