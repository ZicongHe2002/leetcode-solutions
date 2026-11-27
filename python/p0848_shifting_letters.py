class Solution:
    def shiftingLetters(self, s, shifts):
        result = list(s)
        accumulated = 0
        for index in range(len(s) - 1,-1,-1):
            accumulated = (accumulated + shifts[index]) % 26
            result[index] = chr(ord('a') + (ord(s[index]) - ord('a') + accumulated) % 26)
        return ''.join(result)
