class Solution:
    def nthUglyNumber(self, n):
        values = [1]
        next_two = next_three = next_five = 0
        while len(values) < n:
            candidate = min(2 * values[next_two], 3 * values[next_three],
                            5 * values[next_five])
            values.append(candidate)
            if candidate == 2 * values[next_two]:
                next_two += 1
            if candidate == 3 * values[next_three]:
                next_three += 1
            if candidate == 5 * values[next_five]:
                next_five += 1
        return values[-1]
