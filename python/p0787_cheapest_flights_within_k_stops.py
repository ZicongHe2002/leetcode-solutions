class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        infinity = float('inf')
        cost = [infinity] * n
        cost[src] = 0
        for _ in range(k + 1):
            updated = cost[:]
            for first, second, price in flights:
                candidate = cost[first] + price
                if candidate < updated[second]:
                    updated[second] = candidate
            cost = updated
        return -1 if cost[dst] == infinity else cost[dst]
