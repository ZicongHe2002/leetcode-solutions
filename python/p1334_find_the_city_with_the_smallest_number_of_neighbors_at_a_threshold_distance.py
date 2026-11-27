class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        distance = [[10**9] * n for _ in range(n)]
        for node in range(n):
            distance[node][node] = 0
        for left, right, weight in edges:
            distance[left][right] = distance[right][left] = weight
        for via in range(n):
            for source in range(n):
                prefix = distance[source][via]
                for target in range(n):
                    candidate = prefix + distance[via][target]
                    if candidate < distance[source][target]:
                        distance[source][target] = candidate
        winner, fewest = -1, n
        for city in range(n):
            count = sum(other != city and distance[city][other] <= distanceThreshold
                        for other in range(n))
            if count <= fewest:
                winner, fewest = city, count
        return winner
