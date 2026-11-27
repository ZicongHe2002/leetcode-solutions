class Solution:
    def maxVacationDays(self, flights, days):
        cities = len(flights)
        scores = [0] + [-1] * (cities - 1)
        for week in range(len(days[0])):
            next_scores = [-1] * cities
            for source, score in enumerate(scores):
                if score < 0:
                    continue
                for destination in range(cities):
                    if source == destination or flights[source][destination]:
                        next_scores[destination] = max(
                            next_scores[destination], score + days[destination][week])
            scores = next_scores
        return max(scores)
