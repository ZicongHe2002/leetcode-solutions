class Solution:
    def fib(self, n):
        current, following = 0, 1
        for bit in range(n.bit_length() - 1, -1, -1):
            doubled = current * (2 * following - current)
            doubled_next = current * current + following * following
            if (n >> bit) & 1:
                current, following = doubled_next, doubled + doubled_next
            else:
                current, following = doubled, doubled_next
        return current
