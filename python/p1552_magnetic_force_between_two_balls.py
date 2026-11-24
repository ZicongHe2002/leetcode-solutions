class Solution:
    def maxDistance(self, position, m):
        ordered = sorted(position)

        def feasible(distance):
            placed, last = 1, ordered[0]
            for value in ordered[1:]:
                if value - last >= distance:
                    placed += 1
                    last = value
                    if placed >= m:
                        return True
            return False

        low, high = 1, (ordered[-1] - ordered[0]) // (m - 1)
        while low < high:
            middle = (low + high + 1) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle - 1
        return low
