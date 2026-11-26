class Solution:
    def numberOfBoomerangs(self, points):
        answer = 0
        for center, (x, y) in enumerate(points):
            distances = {}
            for other, (next_x, next_y) in enumerate(points):
                if center == other:
                    continue
                distance = (x - next_x) ** 2 + (y - next_y) ** 2
                previous = distances.get(distance, 0)
                answer += 2 * previous
                distances[distance] = previous + 1
        return answer
