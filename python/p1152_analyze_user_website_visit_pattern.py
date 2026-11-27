from collections import defaultdict
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        visits = defaultdict(list)
        for time, user, site in sorted(zip(timestamp, username, website)):
            visits[user].append(site)
        scores = defaultdict(int)
        for sites in visits.values():
            for pattern in set(combinations(sites, 3)):
                scores[pattern] += 1
        return list(min(scores, key=lambda pattern: (-scores[pattern], pattern)))
