class Solution:
    def countSegments(self, s):
        count = 0
        for index, character in enumerate(s):
            if character != ' ' and (index == 0 or s[index - 1] == ' '):
                count += 1
        return count
