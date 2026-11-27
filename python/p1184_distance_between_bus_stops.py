class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        first, last = sorted((start, destination))
        direct = sum(distance[index] for index in range(first, last))
        return min(direct, sum(distance) - direct)
