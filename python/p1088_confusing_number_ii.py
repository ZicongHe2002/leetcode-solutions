class Solution:
    def confusingNumberII(self, n):
        digits = ((0, 0), (1, 1), (6, 9), (8, 8), (9, 6))

        def count(value, rotated, place):
            total = int(value != rotated)
            for digit, image in digits:
                if value == 0 and digit == 0:
                    continue
                following = value * 10 + digit
                if following > n:
                    break
                total += count(following, image * place + rotated, place * 10)
            return total

        return count(0, 0, 1)
