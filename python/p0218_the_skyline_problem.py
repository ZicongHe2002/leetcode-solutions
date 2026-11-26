from heapq import heappop, heappush


class Solution:
    def getSkyline(self, buildings):
        starts = sorted((left, -height, right) for left, right, height in buildings)
        positions = sorted({position for left, right, height in buildings for position in (left, right)})
        active = []
        answer = []
        index = 0
        for position in positions:
            while index < len(starts) and starts[index][0] == position:
                left, negative_height, right = starts[index]
                heappush(active, (negative_height, right))
                index += 1
            while active and active[0][1] <= position:
                heappop(active)
            height = -active[0][0] if active else 0
            if not answer or answer[-1][1] != height:
                answer.append([position, height])
        return answer
