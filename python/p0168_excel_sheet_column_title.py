class Solution:
    def convertToTitle(self, columnNumber):
        letters = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            letters.append(chr(ord('A') + remainder))
        return ''.join(reversed(letters))
