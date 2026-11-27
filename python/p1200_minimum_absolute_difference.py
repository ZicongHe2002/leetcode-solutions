class Solution:
    def minimumAbsDifference(self, arr):
        ordered = sorted(arr)
        best = float('inf')
        answer = []
        for index in range(1, len(ordered)):
            difference = ordered[index] - ordered[index - 1]
            pair = [ordered[index - 1], ordered[index]]
            if difference < best:
                best = difference
                answer = [pair]
            elif difference == best:
                answer.append(pair)
        return answer
