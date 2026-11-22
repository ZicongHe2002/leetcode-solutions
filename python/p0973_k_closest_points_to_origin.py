from heapq import heappush, heapreplace


class Solution:
    def kClosest(self, points, k):
        selected = []
        for index, (x, y) in enumerate(points):
            distance = x * x + y * y
            entry = (-distance, index)
            if len(selected) < k:
                heappush(selected, entry)
            elif distance < -selected[0][0]:
                heapreplace(selected, entry)
        return [points[index][:] for _, index in selected]
