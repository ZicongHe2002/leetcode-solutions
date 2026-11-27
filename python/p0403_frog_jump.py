class Solution:
    def canCross(self, stones):
        if not stones:
            return False
        arrivals = {position: set() for position in stones}
        arrivals[0].add(0)
        for position in stones:
            for previous in arrivals[position]:
                for step in (previous - 1, previous, previous + 1):
                    destination = position + step
                    if step > 0 and destination in arrivals:
                        arrivals[destination].add(step)
        return bool(arrivals[stones[-1]])
