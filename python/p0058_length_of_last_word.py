class Solution:
    def lengthOfLastWord(self, s):
        index = len(s) - 1
        while index >= 0 and s[index] == ' ':
            index -= 1
        end = index
        while index >= 0 and s[index] != ' ':
            index -= 1
        return end - index
