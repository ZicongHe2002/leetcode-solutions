class Solution:
    def magicalString(self, n):
        sequence = [1, 2, 2]
        head = 2
        value = 1
        while len(sequence) < n:
            sequence.extend([value] * sequence[head])
            head += 1
            value = 3 - value
        return sequence[:n].count(1)
