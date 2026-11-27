import heapq


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        reachable = startFuel
        available = []
        index = stops = 0
        while reachable < target:
            while index < len(stations) and stations[index][0] <= reachable:
                heapq.heappush(available,-stations[index][1])
                index += 1
            if not available:
                return -1
            reachable -= heapq.heappop(available)
            stops += 1
        return stops
