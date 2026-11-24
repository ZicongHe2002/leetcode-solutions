class Solution:
    def shipWithinDays(self, weights, days):
        def feasible(capacity):
            used, load = 1, 0
            for weight in weights:
                if load + weight > capacity:
                    used += 1
                    load = 0
                load += weight
            return used <= days

        low, high = max(weights), sum(weights)
        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1
        return low
