class Solution:
    def minAddToMakeValid(self, s):
        missing = opened = 0
        for letter in s:
            if letter == '(':
                opened += 1
            elif opened:
                opened -= 1
            else:
                missing += 1
        return missing + opened
