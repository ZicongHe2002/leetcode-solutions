class Solution:
    def toLowerCase(self, s):
        return ''.join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in s)
