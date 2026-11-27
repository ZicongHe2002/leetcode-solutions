class Solution:
    def countDigitOne(self, n):
        total = 0
        place = 1
        while place <= n:
            higher = n // (place * 10)
            current = (n // place) % 10
            lower = n % place
            total += higher * place
            if current == 1:
                total += lower + 1
            elif current > 1:
                total += place
            place *= 10
        return total
