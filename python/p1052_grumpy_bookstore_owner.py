class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        base = sum(count for count,bad in zip(customers,grumpy) if not bad)
        additional = best = 0
        for index,count in enumerate(customers):
            if grumpy[index]:
                additional += count
            if index >= minutes and grumpy[index - minutes]:
                additional -= customers[index - minutes]
            if index + 1 >= minutes:
                best = max(best,additional)
        return base + best
