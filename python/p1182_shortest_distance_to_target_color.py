from bisect import bisect_left


class Solution:
    def shortestDistanceColor(self, colors, queries):
        positions = {1: [], 2: [], 3: []}
        for index, color in enumerate(colors):
            positions[color].append(index)
        answer = []
        for index, color in queries:
            candidates = positions[color]
            if not candidates:
                answer.append(-1)
                continue
            following = bisect_left(candidates, index)
            distance = float('inf')
            if following < len(candidates):
                distance = candidates[following] - index
            if following:
                distance = min(distance, index - candidates[following - 1])
            answer.append(distance)
        return answer
