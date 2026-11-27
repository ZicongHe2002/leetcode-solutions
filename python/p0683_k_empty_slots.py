from collections import deque


class Solution:
    def kEmptySlots(self, bulbs, k):
        n = len(bulbs)
        if k + 1 >= n:
            return -1
        days = [0] * n
        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day
        minima = deque()
        for position in range(1, k + 1):
            while minima and days[minima[-1]] >= days[position]:
                minima.pop()
            minima.append(position)
        best = n + 1
        for left in range(n - k - 1):
            right = left + k + 1
            endpoint_day = max(days[left], days[right])
            if not minima or days[minima[0]] > endpoint_day:
                best = min(best, endpoint_day)
            while minima and minima[0] <= left + 1:
                minima.popleft()
            if k:
                while minima and days[minima[-1]] >= days[right]:
                    minima.pop()
                minima.append(right)
        return -1 if best == n + 1 else best
