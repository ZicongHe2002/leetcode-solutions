from heapq import heapify, heappop, heappush


class Solution:
    def connectSticks(self, sticks):
        pending = list(sticks)
        heapify(pending)
        answer = 0
        while len(pending) > 1:
            combined = heappop(pending) + heappop(pending)
            answer += combined
            heappush(pending, combined)
        return answer
