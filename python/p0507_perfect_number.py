class Solution:
    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        total = 1
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                total += factor
                partner = num // factor
                if partner != factor:
                    total += partner
                if total > num:
                    return False
            factor += 1
        return total == num
