from bisect import bisect_left


class Solution:
    def mincostTickets(self, days, costs):
        best = [0] * (len(days) + 1)
        for index in range(len(days) - 1,-1,-1):
            best[index] = min(cost + best[bisect_left(days,days[index] + duration,lo=index)]
                              for duration,cost in zip((1,7,30),costs))
        return best[0]
