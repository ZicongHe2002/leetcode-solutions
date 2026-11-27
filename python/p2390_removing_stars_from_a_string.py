class Solution:
    def removeStars(self, s):
        remaining = []
        for letter in s:
            if letter == '*':
                remaining.pop()
            else:
                remaining.append(letter)
        return ''.join(remaining)
