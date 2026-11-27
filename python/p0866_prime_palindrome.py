class Solution:
    def primePalindrome(self, n):
        for small in (2,3,5,7,11):
            if small >= n:
                return small

        def prime(value):
            if value < 2 or value % 2 == 0:
                return value == 2
            divisor = 3
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return False
                divisor += 2
            return True

        prefix = 10**((len(str(n)) - 1) // 2)
        while True:
            text = str(prefix)
            candidate = int(text + text[-2::-1])
            if candidate >= n and prime(candidate):
                return candidate
            prefix += 1
