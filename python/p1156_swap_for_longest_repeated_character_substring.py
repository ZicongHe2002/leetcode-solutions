from collections import Counter
from itertools import groupby


class Solution:
    def maxRepOpt1(self, text):
        counts = Counter(text)
        groups = [(letter, sum(1 for _ in group)) for letter, group in groupby(text)]
        answer = 0
        for index, (letter, length) in enumerate(groups):
            answer = max(answer, min(counts[letter], length + 1))
            if index + 2 < len(groups) and groups[index + 1][1] == 1 and groups[index + 2][0] == letter:
                joined = length + groups[index + 2][1] + 1
                answer = max(answer, min(counts[letter], joined))
        return answer
