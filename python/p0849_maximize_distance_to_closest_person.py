class Solution:
    def maxDistToClosest(self, seats):
        previous = -1
        best = 0
        for index,occupied in enumerate(seats):
            if occupied:
                if previous < 0:
                    best = index
                else:
                    best = max(best,(index - previous) // 2)
                previous = index
        return max(best,len(seats) - 1 - previous)
