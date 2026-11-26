class Solution:
    def findContestMatch(self, n):
        matches = [str(seed) for seed in range(1, n + 1)]
        while len(matches) > 1:
            size = len(matches)
            matches = [f'({matches[index]},{matches[size - 1 - index]})'
                       for index in range(size // 2)]
        return matches[0]
