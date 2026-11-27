from math import lcm


class Solution:
    def nthUglyNumber(self, n, a, b, c):
        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)

        def count(bound):
            return (bound // a + bound // b + bound // c
                    - bound // ab - bound // ac - bound // bc + bound // abc)

        low, high = 1, n * min(a, b, c)
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= n:
                high = middle
            else:
                low = middle + 1
        return low
