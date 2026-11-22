class Solution:
    def makeGood(self, s):
        remaining = []
        for letter in s:
            if remaining and abs(ord(remaining[-1]) - ord(letter)) == 32:
                remaining.pop()
            else:
                remaining.append(letter)
        return ''.join(remaining)
