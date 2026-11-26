class Solution:
    def countArrangement(self, n):
        allowed = [0] * (n + 1)
        for position in range(1, n + 1):
            for value in range(1, n + 1):
                if value % position == 0 or position % value == 0:
                    allowed[position] |= 1 << (value - 1)
        counts = [0] * (1 << n)
        counts[0] = 1
        for mask in range(1 << n):
            position = mask.bit_count() + 1
            if position > n or counts[mask] == 0:
                continue
            choices = allowed[position] & ~mask
            while choices:
                bit = choices & -choices
                counts[mask | bit] += counts[mask]
                choices ^= bit
        return counts[-1]
