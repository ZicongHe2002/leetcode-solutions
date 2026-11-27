from math import isqrt


class Solution:
    def superpalindromesInRange(self, left, right):
        lower,upper = int(left),int(right)
        first_root = isqrt(lower - 1) + 1
        last_root = isqrt(upper)
        answer = 0
        seed = 1
        while True:
            text = str(seed)
            odd = int(text + text[-2::-1])
            if odd > last_root:
                break
            even = int(text + text[::-1])
            for root in (odd,even):
                if first_root <= root <= last_root:
                    squared = str(root * root)
                    if squared == squared[::-1]:
                        answer += 1
            seed += 1
        return answer
