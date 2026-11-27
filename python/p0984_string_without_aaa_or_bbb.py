class Solution:
    def strWithout3a3b(self, a, b):
        result = []
        while a or b:
            if len(result) >= 2 and result[-1] == result[-2]:
                char = 'b' if result[-1] == 'a' else 'a'
            else:
                char = 'a' if a >= b else 'b'
            result.append(char)
            if char == 'a':
                a -= 1
            else:
                b -= 1
        return ''.join(result)
