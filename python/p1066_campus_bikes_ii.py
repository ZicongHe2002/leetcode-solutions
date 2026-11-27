from functools import cache


class Solution:
    def assignBikes(self, workers, bikes):
        @cache
        def minimum(mask):
            worker = mask.bit_count()
            if worker == len(workers):
                return 0
            wx,wy = workers[worker]
            return min(abs(wx - bx) + abs(wy - by) + minimum(mask | (1 << bike))
                       for bike,(bx,by) in enumerate(bikes) if not mask & (1 << bike))

        return minimum(0)
