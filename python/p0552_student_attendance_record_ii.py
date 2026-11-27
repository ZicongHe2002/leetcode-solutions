class Solution:
    def checkRecord(self, n):
        modulus = 10**9 + 7
        zero_absence = (1, 0, 0)
        one_absence = (0, 0, 0)
        for _ in range(n):
            zero_total = sum(zero_absence) % modulus
            one_total = sum(one_absence) % modulus
            zero_absence, one_absence = (
                (zero_total, zero_absence[0], zero_absence[1]),
                ((zero_total + one_total) % modulus, one_absence[0], one_absence[1]),
            )
        return (sum(zero_absence) + sum(one_absence)) % modulus
