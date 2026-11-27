from collections import defaultdict


class Solution:
    def assignBikes(self, workers, bikes):
        pairs = defaultdict(list)
        for worker,(wx,wy) in enumerate(workers):
            for bike,(bx,by) in enumerate(bikes):
                pairs[abs(wx - bx) + abs(wy - by)].append((worker,bike))
        answer = [-1] * len(workers)
        used = set()
        remaining = len(workers)
        for distance in sorted(pairs):
            for worker,bike in pairs[distance]:
                if answer[worker] < 0 and bike not in used:
                    answer[worker] = bike
                    used.add(bike)
                    remaining -= 1
                    if remaining == 0:
                        return answer
        return answer
