class Solution:
    def smallestFactorization(self, num):
        if num < 10:
            return num
        answer, place = 0, 1
        for digit in range(9, 1, -1):
            while num % digit == 0:
                num //= digit
                answer += digit * place
                if answer > 2**31 - 1:
                    return 0
                place *= 10
        return answer if num == 1 else 0
