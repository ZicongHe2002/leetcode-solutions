class Solution:
    def numsSameConsecDiff(self, n, k):
        if n == 1:
            return list(range(10))
        values = list(range(1,10))
        for _ in range(n - 1):
            following = []
            for value in values:
                last = value % 10
                for digit in {last - k,last + k}:
                    if 0 <= digit <= 9:
                        following.append(10 * value + digit)
            values = following
        return values
