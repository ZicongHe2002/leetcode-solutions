class Solution:
    def isMatch(self, s, p):
        previous = [False] * (len(p) + 1)
        previous[0] = True
        for end in range(1, len(p) + 1):
            previous[end] = previous[end - 1] and p[end - 1] == '*'
        for character in s:
            current = [False] * (len(p) + 1)
            for end, token in enumerate(p, 1):
                if token == '*':
                    current[end] = current[end - 1] or previous[end]
                else:
                    current[end] = previous[end - 1] and (token == '?' or token == character)
            previous = current
        return previous[-1]
