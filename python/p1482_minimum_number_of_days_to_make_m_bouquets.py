class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        def feasible(day):
            run = bouquets = 0
            for bloom in bloomDay:
                if bloom <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0
                else:
                    run = 0
            return bouquets >= m

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1
        return low
