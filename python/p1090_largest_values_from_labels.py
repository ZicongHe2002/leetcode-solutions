class Solution:
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        used = {}
        total = selected = 0
        for value, label in sorted(zip(values, labels), reverse=True):
            if selected == numWanted:
                break
            if used.get(label, 0) < useLimit:
                used[label] = used.get(label, 0) + 1
                total += value
                selected += 1
        return total
