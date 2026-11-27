class Solution:
    def smallestGoodBase(self, n):
        value = int(n)
        bits = value.bit_length()
        for exponent in range(bits - 1, 1, -1):
            low = 2
            high = 1 << ((bits + exponent - 1) // exponent)
            while low <= high:
                base = (low + high) // 2
                total = 1
                for _ in range(exponent):
                    total = total * base + 1
                    if total > value:
                        break
                if total == value:
                    return str(base)
                if total < value:
                    low = base + 1
                else:
                    high = base - 1
        return str(value - 1)
