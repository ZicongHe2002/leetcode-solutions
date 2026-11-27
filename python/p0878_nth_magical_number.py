from math import gcd


class Solution:
    def nthMagicalNumber(self, n, a, b):
        common = a // gcd(a,b) * b
        low,high = min(a,b),n * min(a,b)
        while low < high:
            middle = (low + high) // 2
            count = middle // a + middle // b - middle // common
            if count >= n:
                high = middle
            else:
                low = middle + 1
        return low % (10**9 + 7)
