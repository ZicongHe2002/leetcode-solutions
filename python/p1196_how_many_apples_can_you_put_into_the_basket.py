class Solution:
    def maxNumberOfApples(self, weight):
        total = count = 0
        for value in sorted(weight):
            if total + value > 5000:
                break
            total += value
            count += 1
        return count
