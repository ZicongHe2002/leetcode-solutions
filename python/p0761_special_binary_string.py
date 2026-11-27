class Solution:
    def makeLargestSpecial(self, s):
        balance = start = 0
        parts = []
        for index, char in enumerate(s):
            balance += 1 if char == '1' else -1
            if balance == 0:
                parts.append('1' + self.makeLargestSpecial(s[start + 1:index]) + '0')
                start = index + 1
        return ''.join(sorted(parts, reverse=True))
