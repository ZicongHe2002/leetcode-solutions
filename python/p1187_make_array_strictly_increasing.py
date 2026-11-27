from bisect import bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        replacements = sorted(set(arr2))
        best = {float('-inf'): 0}
        for value in arr1:
            following = {}
            for previous, cost in best.items():
                if value > previous:
                    following[value] = min(following.get(value, float('inf')), cost)
                position = bisect_right(replacements, previous)
                if position < len(replacements):
                    candidate = replacements[position]
                    following[candidate] = min(following.get(candidate, float('inf')), cost + 1)
            if not following:
                return -1
            best = following
        return min(best.values())
