from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text):
        counts = Counter(text)
        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])
