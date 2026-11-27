class Solution:
    def checkValidString(self, s):
        lowest = highest = 0
        for letter in s:
            if letter == '(':
                lowest += 1
                highest += 1
            elif letter == ')':
                lowest = max(0, lowest - 1)
                highest -= 1
            else:
                lowest = max(0, lowest - 1)
                highest += 1
            if highest < 0:
                return False
        return lowest == 0
