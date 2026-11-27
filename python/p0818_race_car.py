from functools import cache


class Solution:
    def racecar(self, target):
        @cache
        def minimum(distance):
            if distance == 0:
                return 0
            accelerations = distance.bit_length()
            beyond = (1 << accelerations) - 1
            if beyond == distance:
                return accelerations
            best = accelerations + 1 + minimum(beyond - distance)
            before = (1 << (accelerations - 1)) - 1
            for backward in range(accelerations - 1):
                retreat = (1 << backward) - 1
                remaining = distance - before + retreat
                cost = accelerations + backward + 1 + minimum(remaining)
                best = min(best,cost)
            return best

        return minimum(target)
