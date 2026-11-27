class Solution:
    def newInteger(self, n):
        result = 0
        place = 1
        while n:
            result += (n % 9) * place
            n //= 9
            place *= 10
        return result
