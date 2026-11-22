class Solution:
    def isMatch(self, s, p):
        previous = [False] * (len(p) + 1)
        previous[0] = True
        for end in range(2, len(p) + 1):
            if p[end - 1] == '*':
                previous[end] = previous[end - 2]
        for character in s:
            current = [False] * (len(p) + 1)
            for end in range(1, len(p) + 1):
                if p[end - 1] == '*':
                    matches = p[end - 2] == '.' or p[end - 2] == character
                    current[end] = current[end - 2] or (matches and previous[end])
                else:
                    current[end] = previous[end - 1] and (p[end - 1] == '.' or p[end - 1] == character)
            previous = current
        return previous[-1]
