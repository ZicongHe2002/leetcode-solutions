from collections import Counter


class Solution:
    def relativeSortArray(self, arr1, arr2):
        counts = Counter(arr1)
        answer = []
        for value in arr2:
            answer.extend([value] * counts.pop(value, 0))
        for value in sorted(counts):
            answer.extend([value] * counts[value])
        return answer
