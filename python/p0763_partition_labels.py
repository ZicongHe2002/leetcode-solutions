class Solution:
    def partitionLabels(self, s):
        last = {letter: index for index, letter in enumerate(s)}
        result = []
        start = end = 0
        for index, letter in enumerate(s):
            end = max(end, last[letter])
            if index == end:
                result.append(index - start + 1)
                start = index + 1
        return result
